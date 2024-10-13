import pandas as pd
import pprint

file = "test.xlsx"

res = {}
currPacket = ""

try:
    df = pd.read_excel(file)
    print("opening")
    
    newHeaders=df.iloc[0]
    df.columns = newHeaders
    df =df[1:]
    df = df.loc[:, df.columns.notna()]

    # print(df)
    for index, row in df.iterrows():
        # if section is not NaN - new packet
        if pd.isna(row["Section"]):
            details = []
            if row["Units"] == "bitflag":
                details = row["Details"].split(",")
            else:
                details = [row["Details"]]

            res[currPacket].append({"Name": row["Name"], 
                                    "Offset": row["Offset"], 
                                    "Type": row["Type"],
                                    "Unit": row["Units"],
                                    "Detail": details})
        else:
            currPacket = row["Section"]
            res[currPacket] = []
    pprint.pprint(res)
except FileNotFoundError:
    print("Not found") 
except Exception as e:
    print(f"Error occured: {e}")