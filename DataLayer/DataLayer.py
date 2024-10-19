import os
import testData 
import json

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
        
    # def generateInterfaceForMultiUnits(self,packet):
    #     packetName = list(packet.keys())[0]
    #     packetData = packet[packetName]
    #     # Make the folder Name
    #     dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
    #     os.makedirs(dataFolderNamePath,exist_ok=True)
    #     # Make the data interface file
    #     headerFileName = "I_{packetName}Data.h".format(packetName=packetName)
    #     filePath = os.path.join(dataFolderNamePath,headerFileName)
    #     with open(filePath, "w") as file:
    #         file.write("#pragma once\n")
    #         file.write('#include "../qtMethods.h"\n')
    #         file.write('#include "I_{packetName}Unit.h"\n'.format(packetName = packetName)) 
    #         file.write("class I_{packetName}Data:public QObject \n{{\nQ_OBJECT\n".format(packetName=packetName))
    #         file.write("public:\n")  
    #         # Deconstructor
    #         file.write("\tvirtual ~I_{packetName}Data() {{}};\n".format(packetName=packetName))
    #         # Standard 2 getters among multiple unit data packet.
    #         file.write("\tvirtual unsigned char getNumberOfUnits() const = 0;\n")
    #         file.write("\tvirtual I_{packetName}Unit& get{packetName}Unit(const unsigned char & index) const = 0;".format(packetName=packetName))
    #         # Closing class off
    #         file.write("\n")
    #         file.write("};")
    #         file.close()
    #     # Make the data unit file
    #     headerFileName = "I_{packetName}Unit.h".format(packetName=packetName)
    #     filePath = os.path.join(dataFolderNamePath,headerFileName)
    #     with open(filePath, "w") as file:
    #         file.write("#pragma once\n")
    #         file.write('#include "../qtMethods.h"\n')
    #         file.write("class I_{packetName}Unit:public QObject \n{{\nQ_OBJECT\n".format(packetName=packetName))
    #         file.write("public:\n")  
    #         # Deconstructor
    #         file.write("\tvirtual ~I_{packetName}Unit() {{}};\n".format(packetName=packetName))
    #         # Write Getter
    #         for attribute in packetData:
    #             # Setting Type
    #             type = self.determineType(attribute)
    #             # Ignore PackageID parse, maybe can remove if parsed json recieve will never send this
    #             if(attribute["Name"] == "PackageID"):
    #                 continue
    #             # This package contains an enum to generate
    #             if(attribute["enum"]):
    #                 enumName = list(attribute["enum"].items())[0][0]
    #                 listValues = list(attribute["enum"].items())[0][1]
    #                 file.write("\t enum {enumName}\n{{\n".format(enumName=enumName))
    #                 for object in listValues:
    #                     key=(list(object.items())[0][0])
    #                     value =(list(object.items())[0][1])
    #                     file.write("\t{macroName}={macroValue},\n".format(macroName=value,macroValue=key))
    #                 file.write("};\n")  
    #             name = attribute["Name"].replace(" ", "")
    #             file.write("\tvirtual {type} get{name}() const = 0;\n".format(type = type, name = name))
    #         # Write out the setter for the function.
    #         for attribute in packetData:
    #             # Skip Package ID
    #             if(attribute["Name"] == "PackageID"):
    #                 continue
    #             # Determine type for data
    #             type = self.determineType(attribute)
    #             name = attribute["Name"].replace(" ", "")
    #             lname = name[:1].lower() + name[1:]
    #             file.write("\tvirtual void set{name}(const {type}& {lname}) = 0;\n".format(type = type, name = name, lname=lname))
    #         file.write("\n")
    #         file.write("\n};")
            
    def generateInterface(self):
        for packet in self.parsedData:
            packetName = packet
            packetData = self.parsedData[packet]
            # Generate multiple data layout
            if(packetData[0]["detail"]).get("Quantity",0) > 1:
                self.generateInterfaceForMultiUnits(packet)
            else:
                # Make the folder Name
                dataFolderNamePath = os.path.join(self.new_directory_path,packet+"Data")
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
                        # if(attribute["enum"]):
                        #     enumName = list(attribute["enum"].items())[0][0]
                        #     listValues = list(attribute["enum"].items())[0][1]
                        #     file.write("\t enum {enumName}\n{{\n".format(enumName=enumName))
                        #     for object in listValues:
                        #         key=(list(object.items())[0][0])
                        #         value =(list(object.items())[0][1])
                        #         file.write("\t{macroName}={macroValue},\n".format(macroName=value,macroValue=key))
                        #     file.write("};\n")    
                        # If has bitflag, need to iterate through list in details and create proper functions.
                        if(attribute["detail"]):
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

with open('output.json') as json_file:
    data = json.load(json_file)
test = DataLayer(json=data)
test.genQMethods()
test.generateInterface()