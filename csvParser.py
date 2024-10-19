import pandas as pd
import pprint
import json

def castVal(val):
    if val.lower() in ['true', 'false']:
        return val.lower() == 'true'
    try:
        return int(val)
    except ValueError:
        return val

def genDetailsDict(cellString):
    details = {}
    commaSplitVals = cellString.split(",")
    for commaSplitVal in commaSplitVals:
        key, val = commaSplitVal.split(":")
        details[key] = castVal(val)

    return details


file = "test.xlsx"

res = {}
currPacket = ""

try:
    df = pd.read_excel(file)
    print("opening")

    # print(df)
    for index, row in df.iterrows():
        # if section is not NaN - new packet
        if pd.isna(row["Name"]):
            continue

        if pd.isna(row["Section"]):
            details = None
            if not pd.isna(row["Details"]):
                details = genDetailsDict(row["Details"])
                    
            res[currPacket].append({"Name": row["Name"].replace(" ", ""),
                                    "Offset": row["Offset"],
                                    "Type": row["Type"],
                                    "Unit": None if pd.isna(row["Units"]) else row["Units"],
                                    "Detail": details})
        else:
            currPacket = row["Section"]
            print(row)
            res[currPacket] = [{
                "Name": row["Name"].replace(" ", ""),
                "Offset": row["Offset"], 
                "Type": row["Type"],
                "Unit": None if pd.isna(row["Units"]) else row["Units"],
                "Detail": genDetailsDict(row["Details"])
            }]
    pprint.pprint(res)

    with open("output.json", "w") as f:
        json.dump(res, f, indent=4)
except FileNotFoundError:
    print("Not found") 
except Exception as e:
    print(f"Error occured: {e}")

