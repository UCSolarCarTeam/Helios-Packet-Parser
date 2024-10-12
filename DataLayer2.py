import os
import testData 

class DataLayer:
    def __init__(self, json=testData.data):
        self.basicHeader = '#pragma once \n#include <qtMethods.h>\n'
        self.parsedData = json
        # Make DataLayer Folder
        self.directory_name = "DataLayer"
        self.current_directory = os.getcwd()
        # Generate Folder path 
        self.new_directory_path = os.path.join(self.current_directory, self.directory_name)
        # Make folder if not exist 
        os.makedirs(self.new_directory_path, exist_ok=True)

    def genQMethods(self):
        fileName = "qtMethods.h"
        fullPath = os.path.join(self.new_directory_path,fileName)
        with open(fullPath, 'w') as file:
            file.write("#include <QObject>\n")
            file.write("#include <QPair>\n")
            file.write("#include <QString>\n")
            file.write("#include <QScopedArrayPointer>\n")
            file.close()

    def determineType(self,attribute):
        if(attribute["Type"] == "short uint"):
            return "unsigned short"
        elif (attribute["Type"] == "uchar"):
            # This could be simpler and have the csv simply indicate if they want boolean type.
            if (attribute["Unit"] == "Boolean"):
                return "bool"
            return "unsigned char"
        elif (attribute["Type"] == "uint"):
            return "unsigned int"
        elif (attribute["Type"] == "short uint"):
            return "unsigned short"
        elif (attribute["Type"] == "float"):
            return "float"
        
    def nameSpaceGenerator(self,packetName, packetData,file):
        for attribute in packetData:
            notSkip = True
            # Skip PackageID
            if(attribute["Name"] == "PackageID"):
                continue
            if (packetName == "MotorFaults"):
                # Skip other iteration for other motor number
                if (attribute["Name"][0:2] != "M0"):
                    notSkip = False
                else:
                    notSkip = True
                # looking for bitflag in unit
            if(attribute["Unit"] == "bitflag" and notSkip):
                #iterate through detail
                for item in attribute["detail"]:
                    type = self.determineType(attribute)
                    value = list(item.values())[0] 
                    key = list(item.keys())[0]
                    editedString = value.lstrip().replace(" ", "_").upper()
                    # Write namespace
                    file.write("\t const {type} {name}_OFFSET= {key};\n".format(type=type,name=editedString,key=key))
                continue

    def generateInterfaceForMultiUnits(self,packet):
        packetName = list(packet.keys())[0]
        packetData = packet[packetName]
        # Make the folder Name
        dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
        os.makedirs(dataFolderNamePath,exist_ok=True)
        # Make the data interface file
        headerFileName = "I_{packetName}Data.h".format(packetName=packetName)
        filePath = os.path.join(dataFolderNamePath,headerFileName)
        with open(filePath, "w") as file:
            file.write("#pragma once\n")
            file.write('#include "../qtMethods.h"\n')
            file.write('#include "I_{packetName}Unit.h"\n'.format(packetName = packetName)) 
            file.write("class I_{packetName}Data:public QObject \n{{\nQ_OBJECT\n".format(packetName=packetName))
            file.write("public:\n")  
            # Deconstructor
            file.write("\tvirtual ~I_{packetName}Data() {{}};\n".format(packetName=packetName))
            # Standard 2 getters among multiple unit data packet.
            file.write("\tvirtual unsigned char getNumberOfUnits() const = 0;\n")
            file.write("\tvirtual I_{packetName}Unit& get{packetName}Unit(const unsigned char & index) const = 0;".format(packetName=packetName))
            # Closing class off
            file.write("\n")
            file.write("};")
            file.close()
        # Make the data unit file
        headerFileName = "I_{packetName}Unit.h".format(packetName=packetName)
        filePath = os.path.join(dataFolderNamePath,headerFileName)
        with open(filePath, "w") as file:
            file.write("#pragma once\n")
            file.write('#include "../qtMethods.h"\n')
            file.write("class I_{packetName}Unit:public QObject \n{{\nQ_OBJECT\n".format(packetName=packetName))
            file.write("public:\n")  
            # Deconstructor
            file.write("\tvirtual ~I_{packetName}Unit() {{}};\n".format(packetName=packetName))
            # Write Getter
            for attribute in packetData:
                # Setting Type
                type = self.determineType(attribute)
                # Ignore PackageID parse, maybe can remove if parsed json recieve will never send this
                if(attribute["Name"] == "PackageID"):
                    continue
                # This package contains an enum to generate
                if(attribute["enum"]):
                    enumName = list(attribute["enum"].items())[0][0]
                    listValues = list(attribute["enum"].items())[0][1]
                    file.write("\t enum {enumName}\n{{\n".format(enumName=enumName))
                    for object in listValues:
                        key=(list(object.items())[0][0])
                        value =(list(object.items())[0][1])
                        file.write("\t{macroName}={macroValue},\n".format(macroName=value,macroValue=key))
                    file.write("};\n")  
                name = attribute["Name"].replace(" ", "")
                file.write("\tvirtual {type} get{name}() const = 0;\n".format(type = type, name = name))
            # Write out the setter for the function.
            for attribute in packetData:
                # Skip Package ID
                if(attribute["Name"] == "PackageID"):
                    continue
                # Determine type for data
                type = self.determineType(attribute)
                name = attribute["Name"].replace(" ", "")
                lname = name[:1].lower() + name[1:]
                file.write("\tvirtual void set{name}(const {type}& {lname}) = 0;\n".format(type = type, name = name, lname=lname))
            file.write("\n")
            file.write("\n};")


    def generateInterface(self):
        for packet in self.parsedData:
            packetName = list(packet.keys())[0]
            packetData = packet[packetName]
            # Generate multiple data layout
            if(packetData[0]["detail"]["isUnit"]) == True:
                self.generateInterfaceForMultiUnits(packet)
            else:
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
                        # Setting Type
                        type = self.determineType(attribute)
                        # Ignore PackageID parse, maybe can remove if parsed json recieve will never send this
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # This package contains an enum to generate
                        if(attribute["enum"]):
                            enumName = list(attribute["enum"].items())[0][0]
                            listValues = list(attribute["enum"].items())[0][1]
                            file.write("\t enum {enumName}\n{{\n".format(enumName=enumName))
                            for object in listValues:
                                key=(list(object.items())[0][0])
                                value =(list(object.items())[0][1])
                                file.write("\t{macroName}={macroValue},\n".format(macroName=value,macroValue=key))
                            file.write("};\n")    
                        # If has bitflag, need to iterate through list in details and create proper functions.
                        if(attribute["Unit"] == "bitflag"):
                            # Motor number empty by default, and given a value when motor data packet is detected
                            motorNum=""
                            if (packetName == "MotorFaults"):
                                # Get motor number
                                motorNum = attribute["Name"][:2]
                            # iterate through detail
                            for item in attribute["detail"]:
                                value = list(item.values())[0] 
                                noSpaceString = value.lstrip().replace(" ","")
                                file.write("\tvirtual bool get{motorNum}{noSpaceString}() const = 0;\n".format(motorNum=motorNum,noSpaceString = noSpaceString))
                            continue
                        # Write getter for main field
                        name = attribute["Name"].replace(" ", "")
                        file.write("\tvirtual {type} get{name}() const = 0;\n".format(type = type, name = name))
                    file.write("\n")
                    # Write out the setter for the function.
                    for attribute in packetData:
                        # Skip Package ID
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # Determine type for data
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        file.write("\tvirtual void set{name}(const {type}& get{name}) = 0;\n".format(type = type, name = name))
                    file.write("\n")
                    file.write("\n};")
    def generateHeaderMultipleUnits(self,packet):
        packetName = list(packet.keys())[0]
        packetData = packet[packetName]
        # Make the folder Name
        dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
        os.makedirs(dataFolderNamePath,exist_ok=True)
        # Make the data header file
        headerFileName = "{packetName}Data.h".format(packetName=packetName)
        filePath = os.path.join(dataFolderNamePath,headerFileName)
        with open(filePath, "w") as file:
            file.write("#pragma once\n")
            file.write('#include "../qtMethods.h"\n')
            file.write('#include "I_{packetName}Data.h"\n'.format(packetName=packetName))
            file.write('#include "{packetName}Unit.h"\n'.format(packetName = packetName)) 
            file.write("class {packetName}Data:public I_{packetName}Data \n{{\nQ_OBJECT\n".format(packetName=packetName))
            file.write("public:\n")  
            # Constructor
            file.write("\t{packetName}Data(QList<I_{packetName}Unit*>units);\n".format(packetName=packetName))
             # Standard 2 getters among multiple unit data packet.
            file.write("\tunsigned char getNumberOfUnits() const;\n")
            file.write("\tI_{packetName}Unit& get{packetName}Unit(const unsigned char& index) const;\n".format(packetName=packetName))
            # Private Method:
            file.write("private:\n")
            editedPacketName = packetName[:1].lower() + packetName [1:]
            file.write("\tQList<I_{packetName}Unit*> {editedPacketName}Units_;\n".format(packetName=packetName,editedPacketName=editedPacketName))
            # Closing class off
            file.write("\n")
            file.write("};")
            file.close()
        # Make Unit header file
        headerFileName = "{packetName}Unit.h".format(packetName=packetName)
        filePath = os.path.join(dataFolderNamePath,headerFileName)
        # Create a file to write to
        with open(filePath, "w") as file:
                    file.write("#pragma once\n")
                    file.write('#include "I_{packetName}Unit.h"\n'.format(packetName = packetName))
                    file.write("class {packetName}Unit:public I_{packetName}Unit \n{{\n".format(packetName=packetName))
                    file.write("public:\n")
                    # Write Constructor
                    file.write("\t{packetName}Unit();\n".format(packetName = packetName))
                    # Write Deconstructor
                    file.write("\t~{packetName}Unit();\n".format(packetName = packetName))
                     # Write the Getter Methods
                    for attribute in packetData:
                        # Skip Package ID
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # if bit flag unit, needs to make setter and getter for details list.
                        if(attribute["Unit"] == "bitflag"):
                            # iterate through detail
                            for item in attribute["detail"]:
                                motorNum = ""
                                value = list(item.values())[0] 
                                noSpaceString = value.lstrip().replace(" ", "")
                                # If we are packaging motor related data, need to get motor number.
                                if (packetName == "MotorFaults"):
                                    # Get motor number
                                    motorNum = attribute["Name"][:2]
                                file.write("\t bool get{motorNum}{noSpaceString}() const;\n".format(motorNum = motorNum,noSpaceString = noSpaceString))
                                                # Determine Type of Data
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        file.write("\t {type} get{name}() const;\n".format(type = type, name = name))
                    # Write out the Setter methods
                    for attribute in packetData:
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # Determining the type for data
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        file.write("\t void set{name}(const {type}& get{name});\n".format(type = type, name = name))
                    # Writing out the variables
                    file.write("private:\n")
                    if packetName == "MotorDetails":
                        # REVIST
                        file.write("\tstatic unsigned char newMotorNumber_;\n")
                    for attribute in packetData:
                        # Skip PackageID
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # Determine Data Type
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        lower_first_letter = name[0].lower() + name[1:]
                        file.write("\t {type} {name}_;\n".format(type = type, name = lower_first_letter))
                    file.write("\n")
                    file.write("};")
    def generateHeader(self):
        for packet in self.parsedData:
            packetName = list(packet.keys())[0]
            packetData = packet[packetName]
             # Generate multiple data layout
            if(packetData[0]["detail"]["isUnit"]) == True:
                self.generateHeaderMultipleUnits(packet)
            # Make the folder Name
            else:
                dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
                os.makedirs(dataFolderNamePath,exist_ok=True)
                # Make the header file
                headerFileName = "{packetName}Data.h".format(packetName=packetName)
                filePath = os.path.join(dataFolderNamePath,headerFileName)
                # Create a file to write to
                with open(filePath, "w") as file:
                    file.write("#pragma once\n")
                    file.write('#include "I_{packetName}Data.h"\n'.format(packetName = packetName))
                    file.write("class {packetName}Data:public I_{packetName}Data \n{{\n".format(packetName=packetName))
                    file.write("public:\n")
                    # Write Constructor
                    file.write("\t{packetName}Data();\n".format(packetName = packetName))
                    # Write Deconstructor
                    file.write("\tvirtual ~{packetName}Data();\n".format(packetName=packetName))
                    # Special Case for MotorFaults as they need QString, CONSIDERATION - write QString for all files, but only implement for what needs it?
                    if (packetName == "MotorFaults" or packetName == "BatteryFaults"):
                        file.write("\tQString toString() const;\n")
                    # Write the Getter Methods
                    for attribute in packetData:
                        # Skip Package ID
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # if bit flag unit, needs to make setter and getter for details list.
                        if(attribute["Unit"] == "bitflag"):
                            # iterate through detail
                            for item in attribute["detail"]:
                                motorNum = ""
                                value = list(item.values())[0] 
                                noSpaceString = value.lstrip().replace(" ", "")
                                # If we are packaging motor related data, need to get motor number.
                                if (packetName == "MotorFaults"):
                                    # Get motor number
                                    motorNum = attribute["Name"][:2]
                                file.write("\t bool get{motorNum}{noSpaceString}() const;\n".format(motorNum = motorNum,noSpaceString = noSpaceString))
                        # Determine Type of Data
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        file.write("\t {type} get{name}() const;\n".format(type = type, name = name))
                    # Write out the Setter methods
                    for attribute in packetData:
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # Determining the type for data
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        file.write("\t void set{name}(const {type}& get{name});\n".format(type = type, name = name))
                    # Writing out the variables
                    file.write("private:\n")
                    for attribute in packetData:
                        # Skip PackageID
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # Determine Data Type
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        lower_first_letter = name[0].lower() + name[1:]
                        file.write("\t {type} {name}_;\n".format(type = type, name = lower_first_letter))
                    file.write("\n")
                    file.write("};")
    def genCppForMultiUnits(self,packet):
        packetName = list(packet.keys())[0]
        lowerPacketName = packetName[0].lower() + packetName[1:]
        packetData = packet[packetName]
        # Make the folder Name
        dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
        os.makedirs(dataFolderNamePath,exist_ok=True)
        # Make the data CPP file
        headerFileName = "{packetName}Data.cpp".format(packetName=packetName)
        filePath = os.path.join(dataFolderNamePath,headerFileName)
        with open(filePath, "w") as file:
            file.write('#include "{packetName}Data.h"\n'.format(packetName=packetName))
            file.write('#include "{packetName}Unit.h"\n'.format(packetName=packetName))
            file.write("{packetName}Data::{packetName}Data(QList<I_{packetName}Unit*> units)\n : {lowerPacketName}Units_(units)\n {{}}\n".format(packetName=packetName,lowerPacketName=lowerPacketName))
            file.write("unsigned char {packetName}Data::getNumberOfUnits() const \n {{ \n \t return {lowerPacketName}Units_.length();\n }}\n".format(lowerPacketName=lowerPacketName,packetName=packetName))
            file.write("I_{packetName}Unit& {packetName}Data::get{packetName}Unit(const unsigned char& index) const\n {{ \n \treturn *{lowerPacketName}Units_[static_cast<int>(index)]; \n }}".format(packetName=packetName, lowerPacketName=lowerPacketName))
        # Make Unit CPP file
        headerFileName = "{packetName}Unit.cpp".format(packetName=packetName)
        filePath = os.path.join(dataFolderNamePath,headerFileName)
        # Create a file to write to
        with open(filePath, "w") as file:
            file.write('#include "{packetName}Unit.h"\n'.format(packetName = packetName))
            if packetName == "MotorDetails":
                    # REVIST
                    file.write("unsigned char MotorDetailsUnit::newMotorNumber_=0;\n")
            # write constructor
            file.write("{packetName}Unit::{packetName}Unit():\n\t".format(packetName=packetName))
            for i, attribute in enumerate(packetData):
                # Skip PackageID
                if attribute["Name"] == "PackageID":
                        continue
                name = attribute["Name"].replace(" ", "")
                lower_first_letter = name[0].lower() + name[1:]
                if i == len(packetData) - 1:
                    file.write("{name}_(0)\n\t".format(name=lower_first_letter))
                else:
                    file.write("{name}_(0)\n\t,".format(name=lower_first_letter))
            file.write("\n{\n")
            # DISCUSS THIS
            if packetName == "MotorDetails":
                file.write("\t motorNumber_ = newMotorNumber_++;\n")
            file.write("}")
            # Write Deconstructor
            file.write("\n{packetName}Unit::~{packetName}Unit(){{}}\n".format(packetName=packetName))
            # Write Getters
            for attribute in packetData:
                if(attribute["Name"] == "PackageID"):
                    continue
                # if bit flag unit, needs to make setter and getter for details.
                if(attribute["Unit"] == "bitflag"):
                    # iterate through detail
                    for item in attribute["detail"]:
                        value = list(item.values())[0] 
                        editedString = value.lstrip().replace(" ", "_").upper()
                        noSpaceString = value.lstrip().replace(" ", "")
                        name = attribute["Name"].replace(" ", "")
                        lower_first_letter = name[0].lower() + name[1:]
                        motorNum=""
                        # Write getter
                        if (packetName == "MotorFaults"):
                            # Get motor number
                            motorNum = attribute["Name"][:2]
                        file.write("bool {packetName}Unit::get{motorNum}{name}() const\n{{\n".format(type = type,packetName=packetName,name = noSpaceString, motorNum=motorNum))
                        file.write("\treturn static_cast<bool>({lower_first_letter}_ & {editedString}_OFFSET);\n".format(type=type,lower_first_letter=lower_first_letter,editedString=editedString))
                        file.write("}\n")
                value = list(attribute.values())[0] 
                noSpaceString = value.lstrip().replace(" ", "")
                type = self.determineType(attribute)
                name = attribute["Name"].replace(" ", "")
                lower_first_letter = name[0].lower() + name[1:]
                file.write("{type} {packetName}Unit::get{name}() const\n{{\n".format(type = type,packetName=packetName,name = name))
                file.write("\treturn static_cast<{type}>({lower_first_letter}_);\n".format(type=type,lower_first_letter=lower_first_letter))
                file.write("}\n")
            # Write Setter
            for attribute in packetData:
                # Skip PackageID
                if(attribute["Name"] == "PackageID"):
                    continue
                value = list(attribute.values())[0] 
                noSpaceString = value.lstrip().replace(" ", "")
                # Determine Data Type
                type = self.determineType(attribute)
                name = attribute["Name"].replace(" ", "")
                lower_first_letter = name[0].lower() + name[1:]
                file.write("void {packetName}Unit::set{name}(const {type}& {lower_first_letter})\n{{\n".format(type = type,packetName=packetName,name = name, lower_first_letter=lower_first_letter))
                file.write("\t{name}_  =  {name};\n".format(name=lower_first_letter))
                file.write("}\n")
    def genCppFile(self):
        for packet in self.parsedData: 
            packetName = list(packet.keys())[0]
            packetData = packet[packetName]
            if(packetData[0]["detail"]["isUnit"]) == True:
                self.genCppForMultiUnits(packet)
            else:
                # Make the folder Name
                dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
                os.makedirs(dataFolderNamePath,exist_ok=True)
                # Make the CPP file
                cppFileName = "{packetName}Data.cpp".format(packetName=packetName)
                filePath = os.path.join(dataFolderNamePath,cppFileName)
                with open(filePath, "w") as file:
                    file.write('#include "{packetName}Data.h"\n'.format(packetName = packetName))
                    file.write("namespace\n{")
                    # Write Namespace
                    self.nameSpaceGenerator(packetName,packetData,file)
                    file.write("}\n")
                    # write constructor
                    file.write("{packetName}Data::{packetName}Data():\n\t".format(packetName=packetName))
                    for i, attribute in enumerate(packetData):
                        # Skip PackageID
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
                        if(attribute["Name"] == "PackageID"):
                            continue
                        # if bit flag unit, needs to make setter and getter for details.
                        if(attribute["Unit"] == "bitflag"):
                            # iterate through detail
                            for item in attribute["detail"]:
                                value = list(item.values())[0] 
                                editedString = value.lstrip().replace(" ", "_").upper()
                                noSpaceString = value.lstrip().replace(" ", "")
                                name = attribute["Name"].replace(" ", "")
                                lower_first_letter = name[0].lower() + name[1:]
                                motorNum=""
                                # Write getter
                                if (packetName == "MotorFaults"):
                                    # Get motor number
                                    motorNum = attribute["Name"][:2]
                                file.write("bool {packetName}Data::get{motorNum}{name}() const\n{{\n".format(type = type,packetName=packetName,name = noSpaceString, motorNum=motorNum))
                                file.write("\treturn static_cast<bool>({lower_first_letter}_ & {editedString}_OFFSET);\n".format(type=type,lower_first_letter=lower_first_letter,editedString=editedString))
                                file.write("}\n")
                        value = list(attribute.values())[0] 
                        noSpaceString = value.lstrip().replace(" ", "")
                        type = self.determineType(attribute)
                        name = attribute["Name"].replace(" ", "")
                        lower_first_letter = name[0].lower() + name[1:]
                        file.write("{type} {packetName}Data::get{name}() const\n{{\n".format(type = type,packetName=packetName,name = name))
                        file.write("\treturn static_cast<{type}>({lower_first_letter}_);\n".format(type=type,lower_first_letter=lower_first_letter))
                        file.write("}\n")
                    # Write Setter
                    for attribute in packetData:
                        # Skip PackageID
                        if(attribute["Name"] == "PackageID"):
                            continue
                        value = list(item.values())[0] 
                        noSpaceString = value.lstrip().replace(" ", "")
                        # Determine Data Type
                        type = self.determineType(attribute)
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