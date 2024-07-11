import os

data =[
    {
        "DriverControls": [
            {"Name": "PackageID", "Offset": 0, "Type": "uchar", "Unit": "", "detail": "ID=4"},
            {"Name": "DriverControlsBoardAlive", "Offset":1, "Type":"uchar", "Unit":"boolean","detail":""},
            {"Name": "LightsInputs", "Offset":2, "Type":"uchar", "Unit":"bitflag", "detail": [{"0x01":"Headlights Off"},{"0x02":"Headlights Low"},{"0x04":"Headlights High"},{"0x08":"Signal Right"},{"0x10":"Signal Left"},{"0x20":"Hazard"},{"0x40":"Interior"}]},
            {"Name": "MusicInput", "Offset":3,"Type":"uchar","Unit":"bitflag","detail": [
    { "0x01": "Volume Up" },
    { "0x02": "Volume Down" },
    { "0x04": "Next Song" },
    { "0x08": "Prev Song" }
  ]},
            {"Name": "Acceleration", "Offset": 4, "Type": "short uint", "Unit": "12bit uint", "detail": ""},
            {"Name": "RegenBraking", "Offset": 6, "Type": "short uint", "Unit": "12bit uint", "detail": "" },
            {"Name": "DriverInputs", "Offset": 8, "Type": "uchar", "Unit": "bitflag", "detail":[
    { "0x01": "Brakes" },
    { "0x02": "Forward" },
    { "0x04": "Reverse" },
    { "0x08": "Push to Talk" },
    { "0x10": "Horn" },
    { "0x20": "Reset" },
    { "0x40": "Aux" },
    { "0x80": "Lap" },
  ]},
        ]
    }
]

class DataLayer:
    def __init__(self, json=data):
        self.basicHeader = '#pragma once \n#include "qtMethods.h"\n'
        self.parsedData = json
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

    def generateInterface(self):
        for packet in self.parsedData:
            packetName = list(packet.keys())[0]
            packetData = packet[packetName]
            # Make the folder Name
            dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
            os.makedirs(dataFolderNamePath,exist_ok=True)
            # Make the interface file
            headerFileName = "I_{packetName}Data.h".format(packetName=packetName)
            filePath = os.path.join(dataFolderNamePath,headerFileName)
            with open(filePath, "w") as file:
                file.write("#pragma once\n")
                file.write("#include qtMethods.h\n")
                file.write("class I_{packetName}Data:public QObject \n{{\n\tQObject\n".format(packetName=packetName))
                file.write("public:\n")
                # Deconstructor
                file.write("\tvirtual ~I_{packetName}Data() {{}}\n".format(packetName=packetName))
                # Getter
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    if(attribute["Name"] == "PackageID"):
                        continue
                    if(attribute["Unit"] == "bitflag"):
                        # iterate through detail
                        for item in attribute["detail"]:
                            # Get Value 
                            value = list(item.values())[0]
                            noSpaceString = value.lstrip()
                            noSpaceString = noSpaceString.replace(" ", "")
                            # Write getter
                            file.write("\tvirtual bool get{noSpaceString}() const = 0;\n".format(noSpaceString = noSpaceString))
                        continue
                    
                    if(attribute["Type"] == "uchar" or attribute["Type"] == "short uint"):
                        type = "unsigned short"
                        if (attribute["Unit"] == "boolean"):
                            type = "bool"
                    else:
                        print("Other")
                    name = attribute["Name"].replace(" ", "")
                    file.write("\tvirtual {type} get{name}() const = 0;\n".format(type = type, name = name))
                file.write("\n")
                # Setter
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    if(attribute["Name"] == "PackageID"):
                        continue
                    if(attribute["Type"] == "uchar"):
                        type = "unsigned char"
                    elif (attribute["Type"] == "short uint"):
                        type = "unsigned short"
                    name = attribute["Name"].replace(" ", "")
                    file.write("\tvirtual void set{name}(const {type}& get{name}) = 0;\n".format(type = type, name = name))
                file.write("\n")
                file.write("\n};")

    def generateHeader(self):
        for packet in self.parsedData:
            packetName = list(packet.keys())[0]
            packetData = packet[packetName]
            # Make the folder Name
            dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
            os.makedirs(dataFolderNamePath,exist_ok=True)
            # Make the header file
            headerFileName = "{packetName}Data.h".format(packetName=packetName)
            filePath = os.path.join(dataFolderNamePath,headerFileName)
            with open(filePath, "w") as file:
                file.write("#pragma once\n")
                file.write('#include "I_{packetName}Data.h"\n'.format(packetName = packetName))
                file.write("class {packetName}Data:public I_{packetName}Data \n{{\n".format(packetName=packetName))
                file.write("public:\n")
                # Constructor
                file.write("\t{packetName}Data()\n".format(packetName = packetName))
                # Deconstructor
                file.write("\tvirtual ~{packetName}Data() {{}}\n".format(packetName=packetName))
                # Getter
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    if(attribute["Name"] == "PackageID"):
                        continue
                    if(attribute["Unit"] == "bitflag"):
                        # iterate through detail
                        for item in attribute["detail"]:
                            value = list(item.values())[0]
                            noSpaceString = value.lstrip()
                            noSpaceString = noSpaceString.replace(" ", "")
                            # Write getter
                            file.write("\t bool get{noSpaceString}() const;\n".format(noSpaceString = noSpaceString))
                        continue
                    
                    if(attribute["Type"] == "uchar" or attribute["Type"] == "short uint"):
                        type = "unsigned short"
                        if (attribute["Unit"] == "boolean"):
                            type = "bool"
                    name = attribute["Name"].replace(" ", "")
                    file.write("\t {type} get{name}() const;\n".format(type = type, name = name))
                # Setter
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    if(attribute["Name"] == "PackageID"):
                        continue
                    if(attribute["Type"] == "uchar"):
                        type = "unsigned char"
                    elif (attribute["Type"] == "short uint"):
                        type = "unsigned short"
                    name = attribute["Name"].replace(" ", "")
                    lower_first_letter = name[0].lower() + name[1:]
                    file.write("\t void set{name}(const {type}& {name});\n".format(type = type, name = lower_first_letter))
                # private variable
                file.write("private:\n")
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    if(attribute["Name"] == "PackageID"):
                        continue
                    if(attribute["Type"] == "uchar"):
                        type = "unsigned char"
                    elif (attribute["Type"] == "short uint"):
                        type = "unsigned short"
                    name = attribute["Name"].replace(" ", "")
                    lower_first_letter = name[0].lower() + name[1:]
                    file.write("\t {type} {name}_;\n".format(type = type, name = lower_first_letter))
                file.write("\n")
                file.write("};")
    def generateCppFile(self):
         for packet in self.parsedData:
                packetName = list(packet.keys())[0]
                packetData = packet[packetName]
                # Make the folder Name
                dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
                os.makedirs(dataFolderNamePath,exist_ok=True)
                # Make the cpp file
                cppFileName = "{packetName}Data.cpp".format(packetName=packetName)
                filePath = os.path.join(dataFolderNamePath,cppFileName)
                with open(filePath, "w") as file:
                    # Need include
                    file.write('include "{name}Data.h"\n'.format(name = packetName ))
                    # Name space
                    file.write("namespace\n{\n")
                    for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                        if(attribute["Name"] == "PackageID"):
                            continue
                        if(attribute["Unit"] == "bitflag"):
                            # iterate through detail
                            for item in attribute["detail"]:
                                value = list(item.values())[0].upper()
                                key = list(item.keys())[0]
                                noSpaceString = value.lstrip()
                                noSpaceString = noSpaceString.replace(" ", "_")
                                if(attribute["Type"] == "uchar"):
                                    type = "unsigned char"
                                if ( attribute["Type"] == "short uint"):
                                    type = "unsigh short"
                                file.write("const {type} {value}_OFFSET = {key}\n".format(type=type,value=value,key=key))
                    file.write("}")

                            
       
                        
                



test = DataLayer()
test.generateInterface()
test.generateHeader()
test.generateCppFile()