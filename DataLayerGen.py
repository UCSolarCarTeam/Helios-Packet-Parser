import os
import sys

example = [{"Mppt":[{"Name":"PackageID","Offset":0,"Type":"uchar","detail":""}]}]
# Data structure
data = [
    {
        "MPPT": [
            {"Name": "PackageID", "Offset": 0, "Type": "uchar", "detail": ""},
            {"Name": "MpptStatus", "Offset": 1, "Type": "uchar", "detail": "# bits 0-2 Channel Number 0 ≤ value ≤ 3, bit 7 Alive bit"},
            {"Name": "ArrayVoltage", "Offset": 2, "Type": "short uint", "detail": "10 mV"},
            {"Name": "ArrayCurrent", "Offset": 4, "Type": "short uint", "detail": "mA"},
            {"Name": "BatteryVoltage", "Offset": 6, "Type": "short uint", "detail": "10 mV"},
            {"Name": "Temperature", "Offset": 8, "Type": "short uint", "detail": "1/100th °C"}
        ]
    }
]
class DataLayerGen:
    
    def __init__ (self, parsedData=data):
        self.basicHeader = " #pragma once \n #include <QObject>\n"
        self.parsedData = parsedData
        self.type = ""
        # Make DataLayer Folder
        self.directory_name = "DataLayer"
        self.current_directory = os.getcwd()
        # Generate Folder path 
        self.new_directory_path = os.path.join(self.current_directory, self.directory_name)
        # Make folder if not exist 
        os.makedirs(self.new_directory_path, exist_ok=True)
        print(self.new_directory_path)
       
        

    def interfaceGen(self):
        for sectionObj in self.parsedData:
            sectionName = list(sectionObj.keys())
            header_file_name = "I_{section}Data.h".format(section=sectionName[0].lower().title())
            data_folder_name = "{section}Data".format(section=sectionName[0].lower().title())
            full_path = os.path.join(self.new_directory_path,data_folder_name)
            # Make new folder
            os.makedirs(full_path, exist_ok=True)
            full_path = os.path.join(full_path,header_file_name)
            # Create the header file
            with open(full_path,"w") as file:
                file.write(self.basicHeader)
                file.write("class {name} : public QObject \n{{\n    QOBJECT\npublic:\n".format(name=header_file_name[:-1]))
                # Destructor
                file.write("virtual ~{name}() {{}}\n".format(name=header_file_name[:-2]))
                # Write the getters
                for attribute in sectionObj.get(sectionName[0]):
                    if (attribute.get("Name") == "PackageID"):
                        continue
                    if (attribute.get("Type")== "uchar"):
                        self.type = "unsigned char"
                    file.write("virtual {type} get{attributeName}() const = 0\n".format(type=self.type,attributeName=attribute.get("Name")))
                # Write setter
                for attribute in sectionObj.get(sectionName[0]):
                    if (attribute.get("Name") == "PackageID"):
                        continue
                    if (attribute.get("Type")== "uchar"):
                        self.type = "unsigned char"
                    file.write("virtual void set{attributeName}(const {type}& {attributeName}) = 0\n".format(type=self.type,attributeName=attribute.get("Name")))

                file.write("}")
                file.close()
                
            
       
            

        
tmp = DataLayerGen()
tmp.interfaceGen()
