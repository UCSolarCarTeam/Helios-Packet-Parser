'''
Class responsible for converting the excel file into Json
'''

import pandas as pd
import json
import logging
import os

class Excel_Json_Converter:
    
    ## CONSTRUCTOR - takes in a filepath to the spreadsheet file
    def __init__(self, excel_filepath, saved_filePath):
        '''
        Constructor method to take the filepath for the excel file and the filepath in where the json will be saved.
            @params:
                self -> build in action\n
                excel_filepath -> String\n
                saved_filePath -> String
        '''
        self.excel_filepath = excel_filepath
        self.saved_filePath = saved_filePath

    ## parse - reads the spreadsheet file and returns a dictionary of the data
    # returns - dictionary of the data or status code -69 if an error occurs
    def parse(self):
        try:
            spreadsheetName = os.path.basename(self.excel_filepath)
            if '.xlsx' in spreadsheetName:
                spreadsheetName = spreadsheetName.replace('.xlsx', '')
                read_file = pd.read_excel(self.excel_filepath)
                read_file.to_csv(f"{self.saved_filePath}\\{spreadsheetName}.csv",  
                                 index=None, header=True)

            json_data = {}
            current_key = None
            current_entry = None

            with open(f"{self.saved_filePath}\\{spreadsheetName}.csv", mode='r') as file:
                lines = file.readlines()

                for line in lines[1:]:
                    fields = [field.strip() for field in line.split(",")]

                    if all(not field for field in fields):
                        continue

                    # Start a new group when fields[0] is non-empty
                    if fields[0]:
                        current_key = fields[0]
                        json_data[current_key] = []

                    if fields[1]:  # When `fields[1]` is non-empty, start a new entry
                        if current_entry:  # Save the previous entry
                            # Ensure proper `Detail` formatting
                            if current_entry["Detail"] and isinstance(current_entry["Detail"], list):
                                current_entry["Detail"] = {
                                    key: value for d in current_entry["Detail"] for key, value in d.items()
                                }
                            elif not current_entry["Detail"]:
                                current_entry["Detail"] = None
                            json_data[current_key].append(current_entry)

                        # Create a new entry
                        current_entry = {
                            "Name": fields[1],
                            "Offset": float(fields[2]) if len(fields) > 2 and fields[2] else None,
                            "Type": fields[3] if len(fields) > 3 and fields[3] else None,
                            "Unit": fields[4] if len(fields) > 4 and fields[4] else None,
                            "Detail": []  # Initialize the details as a list
                        }

                    # Append to the current entry's details if applicable
                    detail_field = fields[5] if len(fields) > 5 else ""
                    if detail_field:
                        if "=" in detail_field:
                            detail_label, detail_value = [part.strip() for part in detail_field.split("=", 1)]
                            current_entry["Detail"].append({detail_label: detail_value})
                        elif detail_field.startswith("0x"):
                            parts = detail_field.split(" ", 1)
                            if len(parts) == 2:
                                detail_label, detail_value = parts[0].strip(), parts[1].strip()
                                current_entry["Detail"].append({detail_label: detail_value})

                # Append the last entry
                if current_entry:
                    if current_entry["Detail"] and isinstance(current_entry["Detail"], list):
                        current_entry["Detail"] = {
                            key: value for d in current_entry["Detail"] for key, value in d.items()
                        }
                    elif not current_entry["Detail"]:
                        current_entry["Detail"] = None
                    json_data[current_key].append(current_entry)

            output_file_path = f"{self.saved_filePath}\\{spreadsheetName}.json"

            with open(output_file_path, mode='w') as json_file:
                json.dump(json_data, json_file, indent=4)

            return output_file_path
        except Exception as e:
            logging.error('Raised error while in parse. Error -> %s', e)
            return "Failed: To convert sheet to json"
