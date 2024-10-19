import pandas as pd
import pprint
import json

### Class for parsing a spreadsheet file and returning a dictionary of the data
class SpreadsheetParser:

    ## CONSTRUCTOR - takes in a filepath to the spreadsheet file
    def __init__(self, filepath):
        self.filepath = filepath

    ## parse - reads the spreadsheet file and returns a dictionary of the data
    # returns - dictionary of the data or status code -69 if an error occurs
    def parse(self):
        res = {}
        currPacket = ""

        try:
            df = pd.read_excel(self.filepath)

            # Iterate through the rows of the spreadsheet and populate res dictionary
            for index, row in df.iterrows():
                if pd.isna(row["Name"]): # skip null rows (no name)
                    continue

                if pd.isna(row["Section"]): #if no section value then add to current packet otherwise create new packet
                    details = None

                    # If there are details, generate a dictionary of them
                    if not pd.isna(row["Details"]):
                        details = self.__genDetailsDict(row["Details"])

                    #populate current packet with the row data
                    res[currPacket].append({"Name": row["Name"].replace(" ", ""),
                                            "Offset": row["Offset"],
                                            "Type": row["Type"],
                                            "Unit": None if pd.isna(row["Units"]) else row["Units"],
                                            "Detail": details})
                else: 
                    # new packet 
                    currPacket = row["Section"]
                    res[currPacket] = [{
                        "Name": row["Name"].replace(" ", ""),
                        "Offset": row["Offset"], 
                        "Type": row["Type"],
                        "Unit": None if pd.isna(row["Units"]) else row["Units"],
                        "Detail": self.__genDetailsDict(row["Details"])
                    }]
            return res
        
        except FileNotFoundError:
            print("Come on now, pick a file that exists")
            return -69
        except Exception as e:
            print(f"You've done ****ed up - {e}")
            return -69

    ## __genDetailsDict - generates a dictionary of the details from string in format "key1:val,key2:val,..."
    def __genDetailsDict(self, cellString):
        details = {}
        commaSplitVals = cellString.split(",")
        for commaSplitVal in commaSplitVals:
            key, val = commaSplitVal.split(":")
            details[key] = self.__castVal(val)
        return details
    
    ## __castVal - casts the value to the appropriate type (int, bool, or string)
    def __castVal(self, val):
        if val.lower() in ['true', 'false']:
            return val.lower() == 'true'
        try:
            return int(val)
        except ValueError:
            return val
