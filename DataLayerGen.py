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
data2 =[
    {
        "DriverControls": [
            {"Name": "PackageID", "Offset": 0, "Type": "uchar", "Unit": "", "detail": "ID=4"},
            {"Name": "DriverControlsBoardAlive", "Offset":1, "Type":"uchar", "Unit":"boolean","detail":""},
            {"Name": "LightsInputs", "Offset":2, "Type":"uchar", "Unit":"bitflag", "detail": ["0x01 Headlights Off","0x02 Headlights Low","0x04 Headlights High","0x08 Signal Right","0x10 Signal Left","0x20 Hazard","0x40 Interior"]},
            {"Name": "MusicInput", "Offset":3,"Type":"uchar","Unit":"bitflage","detail": ["0x01 Volume Up","0x02 Volume Down","0x04 Next Song","0x08 Prev Song"]},
            {"Name": "Acceleration", "Offset": 4, "Type": "short uint", "Unit": "12bit uint", "detail": ""},
            {"Name": "RegenBraking", "Offset": 6, "Type": "short uint", "Unit": "12bit uint", "detail": "" },
            {"Name": "DriverInputs", "Offset": 8, "Type": "uchar", "Unit": "bitflag", "detail": ["0x01 Brakes","0x02 Forward", "0x04 Reverse","0x08 Push to Talk","0x10 Horn","0x20 Reset","0x40 Aux","0x80 Lap"]},
        ]
    }
]

class DataLayerGen:
    
    def __init__ (self, parsedData=data):
        self.basicHeader = '#pragma once \n#include "qtMethods.h"\n' 
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
       
    def genQMethods(self,path):
        fileName = "qtMethods.h"
        fullPath = os.path.join(path,fileName)
        with open(fullPath, 'w') as file:
            file.write("#include <QObject>\n")
            file.write("#include <QPair>\n")
            file.write("#include <QString>\n")
            file.write("#include <QScopedArrayPointer>\n")
            file.close()

    def interfaceGen(self):
        for sectionObj in self.parsedData:
            sectionName = list(sectionObj.keys())
            data_folder_name = "{section}Data".format(section=sectionName[0].lower().title())
            full_path = os.path.join(self.new_directory_path,data_folder_name)
             # Make new folder
            os.makedirs(full_path, exist_ok=True)
            # Generate standard QMethod file
            self.genQMethods(full_path)
            # If MPPT need to gen unit
            if (sectionName[0] == 'MPPT'):
                header_file_name = "I_{section}Unit.h".format(section=sectionName[0].lower().title())
                filePath = os.path.join(full_path,header_file_name)
                with open(filePath,"w") as file:
                    file.write(self.basicHeader)
                    file.write("class {name} : public QObject \n{{\nQOBJECT\npublic:\n".format(name=header_file_name[:-2]))
                    # Destructor
                    file.write("\tvirtual ~{name}() {{}}\n".format(name=header_file_name[:-2]))
                    # Write the getters
                    for attribute in sectionObj.get(sectionName[0]):
                        if (attribute.get("Name") == "PackageID"):
                            continue
                        if (attribute.get("Type")== "uchar"):
                            self.type = "unsigned char"
                        file.write("\tvirtual {type} get{attributeName}() const = 0\n".format(type=self.type,attributeName=attribute.get("Name")))
                    # Write setter
                    for attribute in sectionObj.get(sectionName[0]):
                        if (attribute.get("Name") == "PackageID"):
                            continue
                        if (attribute.get("Type") == "uchar"):
                            self.type = "unsigned char"
                        elif (attribute.get("Type") == "short uint"):
                            self.type = "unsigned short"
                        file.write("\tvirtual void set{attributeName}(const {type}& {attributeName}) = 0\n".format(type=self.type,attributeName=attribute.get("Name")))
                    file.write("}")
                    file.close()
                filePath = ""
                # Header File gen
                header_file_name = "I_{section}Data.h".format(section=sectionName[0].lower().title())
                filePath = os.path.join(full_path,header_file_name)
                # Special case for MPPT
                with open(filePath,"w") as file:
                    file.write(self.basicHeader)
                    file.write('#include "I_{section}Unit.h"\n'.format(section=sectionName[0].lower().title()))
                    file.write("class {name} : public QObject \n{{\nQOBJECT\npublic:\n".format(name=header_file_name[:-2]))
                    # Destructor
                    file.write("\tvirtual ~{name}() {{}}\n".format(name=header_file_name[:-2]))
                    # Body
                    file.write("\tvirtual unsigned char getNumberOfUnits() const = 0;\n")
                    file.write("\tvirtual I_MpptUnit& getMpptUnit(const unsigned char& index) const = 0;")
                    file.write("}")
                    file.close()
                continue
           
            # Create the header file
            with open(full_path,"w") as file:
                file.write(self.basicHeader)
                file.write("class {name} : public QObject \n{{\nQOBJECT\npublic:\n".format(name=header_file_name[:-1]))
                # Destructor
                file.write("\tvirtual ~{name}() {{}}\n".format(name=header_file_name[:-2]))
                # Write the getters
                for attribute in sectionObj.get(sectionName[0]):
                    if (attribute.get("Name") == "PackageID"):
                        continue
                    if (attribute.get("Type")== "uchar"):
                        self.type = "unsigned char"
                    file.write("\tvirtual {type} get{attributeName}() const = 0\n".format(type=self.type,attributeName=attribute.get("Name")))
                # Write setter
                for attribute in sectionObj.get(sectionName[0]):
                    if (attribute.get("Name") == "PackageID"):
                        continue
                    if (attribute.get("Type")== "uchar"):
                        self.type = "unsigned char"
                    elif (attribute.get("Type" == "short uint")):
                        self.type = "unsigned short"
                    file.write("\tvirtual void set{attributeName}(const {type}& {attributeName}) = 0\n".format(type=self.type,attributeName=attribute.get("Name")))

                file.write("}")
                file.close()

    def headerFileGen(self):
        for sectionObj in self.parsedData:
            sectionName = list(sectionObj.keys())
            data_folder_name = "{section}Data".format(section=sectionName[0].lower().title())
            full_path = os.path.join(self.new_directory_path,data_folder_name)
            header_file_name = "{section}Data.h".format(section= sectionName[0].lower().Title)
            filePath = os.path.join(full_path,header_file_name)
            




                
tmp = DataLayerGen()
tmp.interfaceGen()
