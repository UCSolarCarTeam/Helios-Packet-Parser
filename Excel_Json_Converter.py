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
        '''
        Converts Excel file into Json file
            @params:
                self -> build in action
            @return:
                output_file_path -> String
        '''
        try:
            spreadsheetName = os.path.basename(self.excel_filepath)
            if('.xlsx' in spreadsheetName):
                spreadsheetName = spreadsheetName.replace('.xlsx', '')
                read_file = pd.read_excel (self.excel_filepath)  
                read_file.to_csv (f"{self.saved_filePath}\\{spreadsheetName}.csv",  
                                index = None, 
                                header=True,                          
                                ) 
                
            json_data = {}  # Final JSON structure
            current_key = None  # Current group key

            with open(f"{self.saved_filePath}\\{spreadsheetName}.csv", mode='r') as file:
                lines = file.readlines()

                for line in lines[1:]:  # Skip the first line (header)
                    fields = [field.strip() for field in line.split(",")]  # Strip whitespace from each field

                    # Skip the line if all fields are empty
                    if all(not field for field in fields):
                        continue

                    # If `fields[0]` is not empty, start a new group
                    if fields[0]:
                        current_key = fields[0]  # Set the new group key
                        json_data[current_key] = []  # Initialize a new list for this key

                    if current_key:  # Ensure there's an active group key
                        # Extract and process the detail field
                        detail_field = fields[5] if len(fields) > 5 else ""
                        detail_label = None
                        detail_value = None

                        if "=" in detail_field:
                            # Case: "value_1 = value_2"
                            detail_label, detail_value = [part.strip() for part in detail_field.split("=", 1)]
                        elif detail_field.startswith("0x"):
                            # Case: "0xValue1 value_2"
                            parts = detail_field.split(" ", 1)
                            if len(parts) == 2:
                                detail_label, detail_value = parts[0].strip(), parts[1].strip()

                        # Create the entry
                        entry = {
                            "Name": fields[1] if len(fields) > 1 and fields[1] else None,
                            "Offset": float(fields[2]) if len(fields) > 2 and fields[2] else None,
                            "Type": fields[3] if len(fields) > 3 and fields[3] else None,
                            "Unit": fields[4] if len(fields) > 4 and fields[4] else None,
                            "Detail": {
                                detail_label: detail_value
                            } if detail_label and detail_value else None  # Default to None if no detail matches
                        }

                        # Only add the entry if at least one field besides `fields[0]` is non-empty
                        if any(value for key, value in entry.items() if key != "Detail") or entry["Detail"] is not None:
                            json_data[current_key].append(entry)

            # Define the JSON output file path
            output_file_path = f"{self.saved_filePath}\\{spreadsheetName}.json"

            # Save JSON data to a file
            with open(output_file_path, mode='w') as json_file:
                json.dump(json_data, json_file, indent=4)

            # print(f"JSON data saved to {output_file_path}")
            return output_file_path
        except Exception as e:
            logging.error('Raised error while in parse. Error -> %s',e)
            return "Failed: To convert sheet to json"
