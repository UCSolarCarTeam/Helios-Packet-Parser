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
},
{"AuxBms":[
    {
    "Name": "PackageID",
    "Offset": 0,
    "Type": "uchar",
    "Unit": "-",
    "detail": [
        {"ID=11": ""}
    ]
},
{
    "Name": "Precharge State",
    "Offset": 1,
    "Type": "uchar",
    "Unit": "flag",
    "detail": [
        {"0": "OFF"},
        {"1": "COMMON_ENGAGED"},
        {"2": "CHARGE_ENGAGED"},
        {"3": "DISCHARGE_ENGAGED"},
        {"4": "ALL_ENGAGED"},
        {"5": "INVALID_STATE"}
    ]
},
{
    "Name": "Aux Voltage",
    "Offset": 2,
    "Type": "uchar",
    "Unit": "mV",
    "detail": []
},
{
    "Name": "Aux Bms Alive",
    "Offset": 3,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
},
{
    "Name": "Strobe Bms Light",
    "Offset": 4,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
},
{
    "Name": "Allow Charge",
    "Offset": 5,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
},
{
    "Name": "High Voltage Enable State",
    "Offset": 6,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
},
{
    "Name": "Allow Discharge",
    "Offset": 7,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
},
{
    "Name": "Orion Can Received Recently",
    "Offset": 8,
    "Type": "uchar",
    "Unit": "Boolean",
    "detail": []
},
{
    "Name": "Aux Contactor Debug Info",
    "Offset": 9,
    "Type": "uchar",
    "Unit": "bitflag",
    "detail": [
        {"0x01": "Charge Contactor Error"},
        {"0x02": "Discharge Contactor Error"},
        {"0x04": "Common Contactor Error"},
        {"0x08": "Discharge Should Trip"},
        {"0x10": "Charge Should Trip"},
        {"0x20": "Charge Open But Should Be Closed"},
        {"0x40": "Discharge Open But Should Be Closed"}
    ]
},
{
    "Name": "Aux Trip",
    "Offset": 10,
    "Type": "short uint",
    "Unit": "bitflag",
    "detail": [
        {"0x0001": "Charge Trip Due To High Cell Voltage"},
        {"0x0002": "Charge Trip Due To High Temperature And Current"},
        {"0x0004": "Charge Trip Due To Pack Current"},
        {"0x0008": "Discharge Trip Due To Low Cell Voltage"},
        {"0x0010": "Discharge Trip Due To High Temperature And Current"},
        {"0x0020": "Discharge Trip Due To Pack Current"},
        {"0x0040": "Protection Trip"},
        {"0x0080": "Trip Due To Orion Message Timeout"},
        {"0x0100": "Charge Not Closed Due To High Current"},
        {"0x0200": "Discharge Not Closed Due To High Current"},
        {"0x0400": "Trip Due To Contactor Disconnected Unexpectedly"}
    ]
},
]},
{"BatteryFaults":[
    {
    "Name": "Error Flags",
    "Offset": 1,
    "Type": "uint",
    "Unit": "bitflag",
    "detail": [
        {"0x00000001": "Internal Communication Fault"},
        {"0x00000002": "Internal Conversion Fault"},
        {"0x00000004": "Weak Cell Fault"},
        {"0x00000008": "Low Cell Voltage Fault"},
        {"0x00000010": "Open Wiring Fault"},
        {"0x00000020": "Current Sensor Fault"},
        {"0x00000040": "Pack Voltage Sensor Fault"},
        {"0x00000080": "Weak Pack Fault"},
        {"0x00000100": "Voltage Redundancy Fault"},
        {"0x00000200": "Fan Monitor Fault"},
        {"0x00000400": "Thermistor Fault"},
        {"0x00000800": "Canbus Communications Fault"},
        {"0x00001000": "Always On Supply Fault"},
        {"0x00002000": "High Voltage Isolation Fault"},
        {"0x00004000": "Power Supply 12V Fault"},
        {"0x00008000": "Charge Limit Enforcement Fault"},
        {"0x00010000": "Discharge Limit Enforcement Fault"},
        {"0x00020000": "Charger Safety Relay Fault"},
        {"0x00040000": "Internal Memory Fault"},
        {"0x00080000": "Internal Thermistor Fault"},
        {"0x00100000": "Internal Logic Fault"}
    ]
},
{
    "Name": "Limit Flags",
    "Offset": 4,
    "Type": "short uint",
    "Unit": "bitflag",
    "detail": [
        {"0x0001": "Dcl Reduced Due To Low Soc"},
        {"0x0002": "Dcl Reduced Due To High Cell Resistence"},
        {"0x0004": "Dcl Reduced Due To Temperature"},
        {"0x0008": "Dcl Reduced Due To Low Cell Voltage"},
        {"0x0010": "Dcl Reduced Due To Low Pack Voltage"},
        {"0x0040": "Dcl And Ccl Reduced Due To Voltage Failsafe"},
        {"0x0080": "Dcl And Ccl Reduced Due To Communication Failsafe"},
        {"0x0200": "Ccl Reduced Due To High Soc"},
        {"0x0400": "Ccl Reduced Due To High Cell Resistence"},
        {"0x0800": "Ccl Reduced Due To Temperature"},
        {"0x1000": "Ccl Reduced Due To High Cell Voltage"},
        {"0x2000": "Ccl Reduced Due To High Pack Voltage"},
        {"0x4000": "Ccl Reduced Due To Charger Latch"},
        {"0x8000": "Ccl Reduced Due To Alternate Current Limit"}
    ]
}
]}
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
                if(packetName == "AuxBms"):
                    file.write(" \tenum PrechargeState\n{\n\tOFF=0,\n\tCOMMON_ENGAGED=1,\n\tCHARGE_ENGAGED=2,\n\tDISCHARGE_ENGAGED=3,\n\tALL_ENGAGED=4,\n\tINVALID_STATE=5,\n};\n")
                # Getter
                
                for attribute in packetData:
                    # if bit flag unit, needs to make setter and getter for details.
                    # Special Case for MotorFaults:
                    ranMotor = False
                    if(attribute["Type"] == "short uint"):
                        type = "unsigned short"
                    if (attribute["Unit"] == "boolean"):
                        type = "bool"
                    if (attribute["Type"] == "uchar"):
                        type = "unsigned char"
                    if (attribute["Type"] == "uint"):
                        type = "unsigned int"
                    if (packetName == "MotorFaults"):
                        # Generate Getter
                        name = attribute["Name"].replace(" ", "")
                        file.write("\tvirtual unsigned char get{name}() const = 0;\n".format( name = name))
                        ranMotor = True
                    if (packetName == "BatteryFaults"):
                        # Generate Getter
                        name = attribute["Name"].replace(" ", "")
                        file.write("\tvirtual  {type} get{name}() const = 0;\n".format( name = name, type=type))
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
                            elif (packetName == "BatteryFaults"):
                                noSpaceString = noSpaceString[0].lower() + noSpaceString[1:]
                                file.write("\tvirtual bool {noSpaceString}() const = 0;\n".format(noSpaceString = noSpaceString))
                            else:
                                file.write("\tvirtual bool get{noSpaceString}() const = 0;\n".format(noSpaceString = noSpaceString))
                        continue
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
                    elif(attribute["Type"] == "uint"):
                        type ="unsigned int"
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
                if (packetName == "MotorFaults" or packetName == "BatteryFaults"):
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
                            elif (packetName == "BatteryFaults"):
                                noSpaceString = noSpaceString[0].lower() + noSpaceString[1:]
                                file.write("\t bool {noSpaceString}() const;\n".format( noSpaceString = noSpaceString, type=type))
                            else:
                                file.write("\t bool get{noSpaceString}() const;\n".format(noSpaceString = noSpaceString))
                    if(attribute["Type"] == "short uint"):
                        type = "unsigned short"
                    elif(attribute["Type"] == "uint"):
                        type = "unsigned int"
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
                    elif (attribute["Type"] == "uint"):
                        type = "unsigned int"
                    name = attribute["Name"].replace(" ", "")
                    file.write("\t void set{name}(const {type}& get{name});\n".format(type = type, name = name))

                # private variable
                if (packetName == "BatteryFaults"):
                    file.write("protected:\n")
                else:
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
                if(packetName == "BatteryFaults"):
                        file.write("\t inline bool errorFlagPresent(const unsigned int errorMask) const;\n")
                        file.write("\t inline bool limitFlagPresent(const unsigned short limitMask) const;\n")
                        file.write("\t inline void appendIfPresent(QString& messageString, const unsigned int errorMask, QString errorDescription) const;\n")
                        file.write("\t inline void appendIfPresent(QString& messageString, const unsigned short limitMask, QString limitDescription) const;\n ")
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
                                    elif (attribute["Type"] == "uint"):
                                        type = "unsigned int"
                                    elif (attribute["Type"] == "short uint"):
                                        type = "unsigned short"
                                    value = list(item.values())[0] 
                                    key = list(item.keys())[0]
                                    editedString = value.lstrip()
                                    editedString = editedString.replace(" ", "_").upper()
                                    # Write getter
                                    file.write("\t const {type} {name}_OFFSET= {key};\n".format(type=type,name=editedString,key=key))
                                continue
                elif (packetName == "BatteryFaults"):
                    for attribute in packetData:
                    # looking for bitflag in unit
                        if(attribute["Type"] == "uchar"):
                            type = "unsigned char"
                        elif (attribute["Type"] == "uint"):
                            type = "unsigned int"
                        elif (attribute["Type"] == "short uint"):
                            type = "unsigned short"
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
                                    file.write("\t const {type} {name}_MASK= {key};\n".format(type=type,name=editedString,key=key))
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
                                elif (attribute["Type"]=="uint"):
                                    type = "unsigned int"
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
                  # Special case for BatteryFaults
                if (packetName == "BatteryFaults"):
                    file.write("bool BatteryFaultsData::errorFlagPresent(const unsigned int errorMask) const\n"
                                "{\n"
                                "\treturn static_cast<bool>(errorFlags_ & errorMask);\n"
                                "}\n\n"
                                "bool BatteryFaultsData::limitFlagPresent(const unsigned short limitMask) const\n"
                                "{\n"
                                "\treturn static_cast<bool>(limitFlags_ & limitMask);\n"
                                "}\n")
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
                            elif (packetName == "BatteryFaults"):
                                noSpaceString = noSpaceString[0].lower() + noSpaceString[1:]
                                file.write("bool {packetName}Data::{name}() const\n{{\n".format(type = type,packetName=packetName,name = noSpaceString))
                                file.write("\treturn static_cast<bool>({lower_first_letter}_ & {editedString}_MASK);\n".format(type=type,lower_first_letter=lower_first_letter,editedString=editedString))
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
                    elif(attribute["Type"] == "uint"):
                        type = "unsigned int"
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
                    elif (attribute["Type"] == "uint"):
                        type = "unsigned int"
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
                # Will need to discuss what we want to do about this
                if (packetName == "BatteryFaults"):
                    file .write("void BatteryFaultsData::appendIfPresent(QString& messageString, const unsigned int errorMask, QString errorDescription) const\n"
                                "{\n"
                                "\tif (errorFlagPresent(errorMask))\n"
                                "\t{\n"
                                "\t\tmessageString.append(errorDescription);\n"
                                "\t}\n"
                                "}\n")
                    file.write("void BatteryFaultsData::appendIfPresent(QString& messageString, const unsigned short limitMask, QString limitDescription) const\n"
                                "{\n"
                                "\tif (errorFlagPresent(limitMask))\n"
                                "\t{\n"
                                "\t\tmessageString.append(limitDescription);\n"
                                "\t}\n"
                                "}\n")
                    file.write("QString BatteryFaultsData::toString() const\n"
                                "{\n"
                                "\tQString messageString;\n\n"
                                "\tif (!static_cast<bool>(errorFlags_))\n"
                                "\t{\n"
                                "\t\tmessageString += \"NO_ERROR\";\n"
                                "\t}\n"
                                "\telse\n"
                                "\t{\n"
                                "\t\tappendIfPresent(messageString, INTERNAL_COMMUNICATION_FAULT_MASK, \"INTERNAL_COMMUNICATION_FAULT \");\n"
                                "\t\tappendIfPresent(messageString, INTERNAL_CONVERSION_FAULT_MASK, \"INTERNAL_CONVERSION_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, WEAK_CELL_FAULT_MASK, \"WEAK_CELL_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, LOW_CELL_VOLTAGE_FAULT_MASK, \"LOW_CELL_VOLTAGE_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, OPEN_WIRING_FAULT_MASK, \"OPEN_WIRING_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CURRENT_SENSOR_FAULT_MASK, \"CURRENT_SENSOR_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, PACK_VOLTAGE_SENSOR_FAULT_MASK, \"PACK_VOLTAGE_SENSOR_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, WEAK_PACK_FAULT_MASK, \"WEAK_PACK_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, VOLTAGE_REDUNDANCY_FAULT_MASK, \"VOLTAGE_REDUNDANCY_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, FAN_MONITOR_FAULT_MASK, \"FAN_MONITOR_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, THERMISTOR_FAULT_MASK, \"THERMISTOR_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CANBUS_COMMUNICATIONS_FAULT_MASK, \"CANBUS_COMMUNICATIONS_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, ALWAYS_ON_SUPPLY_FAULT_MASK, \"ALWAYS_ON_SUPPLY_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, HIGH_VOLTAGE_ISOLATION_FAULT_MASK, \"HIGH_VOLTAGE_ISOLATION_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, POWER_SUPPLY_12V_FAULT_MASK, \"POWER_SUPPLY_12V_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CHARGE_LIMIT_ENFORCEMENT_FAULT_MASK, \"CHARGE_LIMIT_ENFORCEMENT_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, DISCHARGE_LIMIT_ENFORCEMENT_FAULT_MASK, \"DISCHARGE_LIMIT_ENFORCEMENT_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CHARGER_SAFETY_RELAY_FAULT_MASK, \"CHARGER_SAFETY_RELAY_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, INTERNAL_MEMORY_FAULT_MASK, \"INTERNAL_MEMORY_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, INTERNAL_THERMISTOR_FAULT_MASK, \"INTERNAL_THERMISTOR_FAULT_MASK \");\n"
                                "\t\tappendIfPresent(messageString, INTERNAL_LOGIC_FAULT_MASK, \"INTERNAL_LOGIC_FAULT_MASK \");\n"
                                "\t}\n\n"
                                "\tif (!static_cast<bool>(limitFlags_))\n"
                                "\t{\n"
                                "\t\tmessageString += \"NO_LIMIT_FLAGS_PRESENT\";\n"
                                "\t}\n"
                                "\telse\n"
                                "\t{\n"
                                "\t\tappendIfPresent(messageString, DCL_REDUCED_DUE_TO_LOW_SOC_MASK, \"DCL_REDUCED_DUE_TO_LOW_SOC_MASK \");\n"
                                "\t\tappendIfPresent(messageString, DCL_REDUCED_DUE_TO_HIGH_CELL_RESISTENCE_MASK, \"DCL_REDUCED_DUE_TO_HIGH_CELL_RESISTENCE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, DCL_REDUCED_DUE_TO_TEMPERATURE_MASK, \"DCL_REDUCED_DUE_TO_TEMPERATURE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, DCL_REDUCED_DUE_TO_LOW_CELL_VOLTAGE_MASK, \"DCL_REDUCED_DUE_TO_LOW_CELL_VOLTAGE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, DCL_REDUCED_DUE_TO_LOW_PACK_VOLTAGE_MASK, \"DCL_REDUCED_DUE_TO_LOW_PACK_VOLTAGE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, DCL_AND_CCL_REDUCED_DUE_TO_VOLTAGE_FAILSAFE_MASK, \"DCL_AND_CCL_REDUCED_DUE_TO_VOLTAGE_FAILSAFE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, DCL_AND_CCL_REDUCED_DUE_TO_COMMUNICATION_FAILSAFE_MASK, \"DCL_AND_CCL_REDUCED_DUE_TO_COMMUNICATION_FAILSAFE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CCL_REDUCED_DUE_TO_HIGH_SOC_MASK, \"CCL_REDUCED_DUE_TO_HIGH_SOC_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CCL_REDUCED_DUE_TO_HIGH_CELL_RESISTENCE_MASK, \"CCL_REDUCED_DUE_TO_HIGH_CELL_RESISTENCE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CCL_REDUCED_DUE_TO_TEMPERATURE_MASK, \"CCL_REDUCED_DUE_TO_TEMPERATURE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CCL_REDUCED_DUE_TO_HIGH_CELL_VOLTAGE_MASK, \"CCL_REDUCED_DUE_TO_HIGH_CELL_VOLTAGE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CCL_REDUCED_DUE_TO_HIGH_PACK_VOLTAGE_MASK, \"CCL_REDUCED_DUE_TO_HIGH_PACK_VOLTAGE_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CCL_REDUCED_DUE_TO_CHARGER_LATCH_MASK, \"CCL_REDUCED_DUE_TO_CHARGER_LATCH_MASK \");\n"
                                "\t\tappendIfPresent(messageString, CCL_REDUCED_DUE_TO_ALTERNATE_CURRENT_LIMIT_MASK, \"CCL_REDUCED_DUE_TO_ALTERNATE_CURRENT_LIMIT_MASK \");\n"
                                "\t}\n\n"
                                "\treturn messageString;\n"
                                "}\n")
                    
                        
test = DataLayer()
test.genQMethods()
test.generateInterface()
test.generateHeader()
test.genCppFile()