import os

data =[
    {
        "DriverControls": [
            {"Name": "PackageID", "Offset": 0, "Type": "uchar", "Unit": "", "detail": "ID=4"},
            {"Name": "DriverControlsBoardAlive", "Offset":1, "Type":"uchar", "Unit":"boolean","detail":""},
            {"Name": "LightsInputs", "Offset":2, "Type":"uchar", "Unit":"bitflag", "detail": [  { "0x01": "Headlights Off" },
  { "0x02": "Headlights Low" },
  { "0x04": "Headlights High" },
  { "0x08": "Signal Right" },
  { "0x10": "Signal Left" },
  { "0x20": "Hazard" },
  { "0x40": "Interior" }]},
            {"Name": "MusicInputs", "Offset":3,"Type":"uchar","Unit":"bitflag","detail": [{ "0x01": "Volume Up" },
  { "0x02": "Volume Down" },
  { "0x04": "Next Song" },
  { "0x08": "Previous Song" }]},
            {"Name": "Acceleration", "Offset": 4, "Type": "short uint", "Unit": "12bit uint", "detail": ""},
            {"Name": "RegenBraking", "Offset": 6, "Type": "short uint", "Unit": "12bit uint", "detail": "" },
            {"Name": "DriverInputs", "Offset": 8, "Type": "uchar", "Unit": "bitflag", "detail": [ { "0x01": "Brakes" },
  { "0x02": "Forward" },
  { "0x04": "Reverse" },
  { "0x08": "Push To Talk" },
  { "0x10": "Horn" },
  { "0x20": "Reset" },
  { "0x40": "Aux" },
  { "0x80": "Lap"}]},
        ]
    },
    {
    "MotorFaults": [
        {"Name": "M0 Error Flags", "Offset": 1, "Type": "uchar", "Unit": "bitflag", "detail": [
            {"0x01": "Motor Over Speed"},
            {"0x02": "Software Over Current"},
            {"0x04": "Dc Bus Over Voltage"},
            {"0x08": "Bad Motor Position Hall Sequence"},
            {"0x10": "Watchdog Caused Last Reset"},
            {"0x20": "Config Read Error"},
            {"0x40": "Rail Under Voltage Lock Out"},
            {"0x80": "Desaturation Fault"}
        ]},
        {"Name": "M1 Error Flags", "Offset": 2, "Type": "uchar", "Unit": "bitflag", "detail": [
            {"0x01": "Motor Over Speed"},
            {"0x02": "Software Over Current"},
            {"0x04": "Dc Bus Over Voltage"},
            {"0x08": "Bad Motor Position Hall Sequence"},
            {"0x10": "Watchdog Caused Last Reset"},
            {"0x20": "Config Read Error"},
            {"0x40": "Rail Under Voltage Lock Out"},
            {"0x80": "Desaturation Fault"}
        ]},
        {"Name": "M0 Limit Flags", "Offset": 3, "Type": "uchar", "Unit": "bitflag", "detail": [
            {"0x01": "Output Voltage Pwm Limit"},
            {"0x02": "Motor Current Limit"},
            {"0x04": "Velocity Limit"},
            {"0x08": "Bus Current Limit"},
            {"0x10": "Bus Voltage Upper Limit"},
            {"0x20": "Bus Voltage Lower Limit"},
            {"0x40": "Ipm Or Motor Temperature Limit"}
        ]},
        {"Name": "M1 Limit Flags", "Offset": 4, "Type": "uchar", "Unit": "bitflag", "detail": [
            {"0x01": "Output Voltage Pwm Limit"},
            {"0x02": "Motor Current Limit"},
            {"0x04": "Velocity Limit"},
            {"0x08": "Bus Current Limit"},
            {"0x10": "Bus Voltage Upper Limit"},
            {"0x20": "Bus Voltage Lower Limit"},
            {"0x40": "Ipm Or Motor Temperature Limit"}
        ]},
        {"Name": "M0 Can Rx Error Count", "Offset": 5, "Type": "uchar", "Unit": "#", "detail": ""},
        {"Name": "M0 Can Tx Error Count", "Offset": 6, "Type": "uchar", "Unit": "#", "detail": ""},
        {"Name": "M1 Can Rx Error Count", "Offset": 7, "Type": "uchar", "Unit": "#", "detail": ""},
        {"Name": "M1 Can Tx Error Count", "Offset": 8, "Type": "uchar", "Unit": "#", "detail": ""}
    ]
}
]

class DataLayer:
    def __init__(self, json=data):
        self.basicHeader = '#pragma once \n#include <qtMethods.h>\n'
        self.parsedData = json
        # Make DataLayer Folder
        self.directory_name = "DataLayer"
        self.current_directory = os.getcwd()
        # Generate Folder path 
        self.new_directory_path = os.path.join(self.current_directory, self.directory_name)
        # Make folder if not exist 
        os.makedirs(self.new_directory_path, exist_ok=True)
        print(self.new_directory_path)

    def genQMethods(self):
        fileName = "qtMethods.h"
        fullPath = os.path.join(self.new_directory_path,fileName)
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
                file.write('#include "../qtMethods.h"\n')
                file.write("class I_{packetName}Data:public QObject \n{{\nQ_OBJECT\n".format(packetName=packetName))
                file.write("public:\n")
                # Deconstructor
                file.write("\tvirtual ~I_{packetName}Data() {{}};\n".format(packetName=packetName))
                # QString if motor faults:
                if(packetName == "MotorFaults"):
                    file.write("\tvirtual QString toString() const = 0;\n")
                # Getter
                
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    # Special Case for MotorFaults:
                    ranMotor = False
                    if (packetName == "MotorFaults"):
                        # Generate Getter
                        name = attribute["Name"].replace(" ", "")
                        file.write("\tvirtual unsigned char get{name}() const = 0;\n".format( name = name))
                        ranMotor = True
                        
                    if(attribute["Name"] == "PackageID"):
                        continue
                    if(attribute["Unit"] == "bitflag"):
                        # iterate through detail
                        for item in attribute["detail"]:
                            value = list(item.values())[0] 
                            noSpaceString = value.lstrip()
                            noSpaceString = noSpaceString.replace(" ", "")
                            
                            if (packetName == "MotorFaults"):
                                # Get motor number
                                motorNum = attribute["Name"][:2].lower()
                                file.write("\tvirtual bool {motorNum}{noSpaceString}() const = 0;\n".format(noSpaceString = noSpaceString,motorNum=motorNum))
                            else:
                                file.write("\tvirtual bool get{noSpaceString}() const = 0;\n".format(noSpaceString = noSpaceString))
                        continue
                    
                    if(attribute["Type"] == "short uint"):
                        type = "unsigned short"
                    if (attribute["Unit"] == "boolean"):
                        type = "bool"
                    if (attribute["Type"] == "uchar"):
                        type = "unsigned char"
                    if (ranMotor == False):
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
                file.write("\t{packetName}Data();\n".format(packetName = packetName))
                # Deconstructor
                file.write("\tvirtual ~{packetName}Data();\n".format(packetName=packetName))
                # Special Case for MotorFaults
                if (packetName == "MotorFaults"):
                    file.write("\tQString toString() const;\n")
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
                            if (packetName == "MotorFaults"):
                                # Get motor number
                                motorNum = attribute["Name"][:2].lower()
                                file.write("\t bool {motorNum}{noSpaceString}() const;\n".format(noSpaceString = noSpaceString,motorNum=motorNum))
                            else:
                                file.write("\t bool get{noSpaceString}() const;\n".format(noSpaceString = noSpaceString))
                    if(attribute["Type"] == "short uint"):
                        type = "unsigned short"
                        
                    elif(attribute["Type"] == "uchar"):
                        type = "unsigned char"
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
                    file.write("\t void set{name}(const {type}& get{name});\n".format(type = type, name = name))
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

    def genCppFile(self):
        for packet in self.parsedData:
            packetName = list(packet.keys())[0]
            packetData = packet[packetName]
            # Make the folder Name
            dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
            os.makedirs(dataFolderNamePath,exist_ok=True)
            # Make the header file
            cppFileName = "{packetName}Data.cpp".format(packetName=packetName)
            filePath = os.path.join(dataFolderNamePath,cppFileName)
            with open(filePath, "w") as file:
                file.write('#include "{packetName}Data.h"\n'.format(packetName = packetName))
                file.write("namespace\n{")
                # Write Namespace
                # Name space for motorFaults
                if (packetName == "MotorFaults"):
                    for attribute in packetData:
                    # looking for bitflag in unit
                        if(attribute["Name"] == "PackageID"):
                            continue
                        if(attribute["Unit"] == "bitflag"):
                            # iterate through detail
                            if(attribute["Name"] == "M0 Error Flags" or attribute["Name"] == "M0 Limit Flags"):
                                for item in attribute["detail"]:
                                    if(attribute["Type"] == "uchar"):
                                        type = "unsigned char"
                                    elif (attribute["Type"] == "short uint"):
                                        type = "unsigned short"
                                    value = list(item.values())[0] 
                                    key = list(item.keys())[0]
                                    editedString = value.lstrip()
                                    editedString = editedString.replace(" ", "_").upper()
                                    # Write getter
                                    file.write("\t const {type} {name}_OFFSET= {key};\n".format(type=type,name=editedString,key=key))
                                continue
                else:
                    for attribute in packetData:
                        # looking for bitflag in unit
                        if(attribute["Name"] == "PackageID"):
                            continue
                        if(attribute["Unit"] == "bitflag"):
                            # iterate through detail
                            for item in attribute["detail"]:
                                if(attribute["Type"] == "uchar"):
                                    type = "unsigned char"
                                elif (attribute["Type"] == "short uint"):
                                    type = "unsigned short"
                                value = list(item.values())[0] 
                                key = list(item.keys())[0]
                                editedString = value.lstrip()
                                editedString = editedString.replace(" ", "_").upper()
                                # Write getter
                                file.write("\t const {type} {name}_OFFSET= {key};\n".format(type=type,name=editedString,key=key))
                            continue
                    
                file.write("}\n")
                # write constructor
                file.write("{packetName}Data::{packetName}Data():\n\t".format(packetName=packetName))
                for i, attribute in enumerate(packetData):
                    if attribute["Name"] == "PackageID":
                            continue
                    
                    name = attribute["Name"].replace(" ", "")
                    lower_first_letter = name[0].lower() + name[1:]
        
                    if i == len(packetData) - 1:
                        file.write("{name}_(0)\n\t".format(name=lower_first_letter))
                    else:
                        file.write("{name}_(0)\n\t,".format(name=lower_first_letter))
                file.write("\n{}")
                # Write Deconstructor
                file.write("\n{packetName}Data::~{packetName}Data(){{}}\n".format(packetName=packetName))
                # Write Getters
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    if(attribute["Name"] == "PackageID"):
                        continue
                    if(attribute["Unit"] == "bitflag"):
                        # iterate through detail
                        for item in attribute["detail"]:
                            value = list(item.values())[0] 
                            editedString = value.lstrip()
                            editedString = editedString.replace(" ", "_").upper()
                            noSpaceString = value.lstrip()
                            noSpaceString = noSpaceString.replace(" ", "")
                            name = attribute["Name"].replace(" ", "")
                            lower_first_letter = name[0].lower() + name[1:]
                            # Write getter
                            if (packetName == "MotorFaults"):
                                # Get motor number
                                motorNum = attribute["Name"][:2].lower()
                                file.write("bool {packetName}Data::{motorNum}{name}() const\n{{\n".format(type = type,packetName=packetName,name = noSpaceString, motorNum=motorNum))
                                file.write("\treturn static_cast<bool>({lower_first_letter}_ & {editedString}_OFFSET);\n".format(type=type,lower_first_letter=lower_first_letter,editedString=editedString))
                                file.write("}\n")
                            else:    
                                file.write("bool {packetName}Data::get{name}() const\n{{\n".format(type = type,packetName=packetName,name = noSpaceString))
                                file.write("\treturn static_cast<bool>({lower_first_letter}_ & {editedString}_OFFSET);\n".format(type=type,lower_first_letter=lower_first_letter,editedString=editedString))
                                file.write("}\n")
                        
                    value = list(item.values())[0] 
                    editedString = value.lstrip()
                    editedString = editedString.replace(" ", "_").upper()
                    noSpaceString = value.lstrip()
                    noSpaceString = noSpaceString.replace(" ", "")
                    if(attribute["Type"] == "uchar"):
                        type = "unsigned char"
                    elif (attribute["Type"] == "short uint"):
                        type = "unsigned short"
                    name = attribute["Name"].replace(" ", "")
                    lower_first_letter = name[0].lower() + name[1:]
                    if (packetName == "MotorFaults"):
                        file.write("{type} {packetName}Data::get{name}() const\n{{\n".format(type = type,packetName=packetName,name = name))
                        file.write("\treturn {lower_first_letter}_;\n".format(type=type,lower_first_letter=lower_first_letter,editedString=editedString))
                    else:
                        file.write("{type} {packetName}Data::get{name}() const\n{{\n".format(type = type,packetName=packetName,name = name))
                        file.write("\treturn static_cast<{type}>({lower_first_letter}_);\n".format(type=type,lower_first_letter=lower_first_letter,editedString=editedString))
                    file.write("}\n")
                # Write Setter
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    if(attribute["Name"] == "PackageID"):
                        continue
                    value = list(item.values())[0] 
                    editedString = value.lstrip()
                    editedString = editedString.replace(" ", "_").upper()
                    noSpaceString = value.lstrip()
                    noSpaceString = noSpaceString.replace(" ", "")
                    if(attribute["Type"] == "uchar"):
                        type = "unsigned char"
                        
                    elif (attribute["Type"] == "short uint"):
                        type = "unsigned short"
            
                    name = attribute["Name"].replace(" ", "")
                    lower_first_letter = name[0].lower() + name[1:]
                    file.write("void {packetName}Data::set{name}(const {type}& {lower_first_letter})\n{{\n".format(type = type,packetName=packetName,name = name, lower_first_letter=lower_first_letter))
                    file.write("\t{name}_  =  {name};\n".format(name=lower_first_letter))
                    file.write("}\n")
                if (packetName == "MotorFaults"):
                    file.write("QString MotorFaultsData::toString() const\n{\n")
                    file.write('\treturn "0x" + QString::number(m0ErrorFlags_, 16) + " 0x" + QString::number(m0LimitFlags_, 16) + " 0x" + QString::number(m1ErrorFlags_, 16) + " 0x" + QString::number(m1LimitFlags_, 16);\n}')
                    
                        
                
                
                    
                



test = DataLayer()
test.genQMethods()
test.generateInterface()
test.generateHeader()
test.genCppFile()