import os
import json

class DataLayer:
    def __init__(self, json):
        self.parsedData = json
        # Make DataLayer Folder
        self.directory = "Output/DataLayer"
        self.current_directory = os.getcwd()
        # Generate Folder path 
        self.new_directory_path = os.path.join(self.current_directory, self.directory)
        # Make folder if not exist 
        os.makedirs(self.new_directory_path, exist_ok=True)


    def determineType(self,attribute):
        # If the Unit is boolean default to that as type
        if (attribute["Unit"] == "Boolean"):
                return "bool"
        if(attribute["Type"] == "short uint"):
            return "unsigned short"
        elif (attribute["Type"] == "uchar"):
            return "unsigned char"
        elif (attribute["Type"] == "uint"):
            return "unsigned int"
        elif (attribute["Type"] == "short uint"):
            return "unsigned short"
        elif (attribute["Type"] == "float"):
            return "float"
        
    def generateInterfaceForMultiUnits(self,packet):
        packetName = packet
        packetData = self.parsedData[packet]
        # Make the folder Name
        dataFolderNamePath = os.path.join(self.new_directory_path,packetName+"Data")
        os.makedirs(dataFolderNamePath,exist_ok=True)
        # Make the data interface file
        headerFileName = "I_{packetName}Data.h".format(packetName=packetName)
        filePath = os.path.join(dataFolderNamePath,headerFileName)
        with open(filePath, "w") as file:
            file.write("#pragma once\n")
            file.write('#include <QObject>\n')
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
            file.write('#include <QObject>\n')
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
                # This package contains an enum to generate (At moment not required for MPPT or Motor Details)
                if (attribute["Unit"] == "flag"):
                    file.write("\tenum {name}\n\t{{\n\t".format(name=attribute["Name"]))
                    for item in attribute["Detail"]:
                        value = attribute["Detail"][item]
                        file.write("\t{macroName} = {value},\n\t".format(macroName=item,value=value))
                    file.write("\n\t};\n")
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
            packetName = packet
            packetData = self.parsedData[packet]
            # Generate multiple data layout
            if(packetData[0]["Detail"]).get("Quantity",0) > 1:
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
                    file.write('#include <QObject>\n')
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
                        if (attribute["Unit"] == "flag"):
                            file.write("\tenum {name}\n\t{{\n\t".format(name=attribute["Name"]))
                            for item in attribute["Detail"]:
                                value = attribute["Detail"][item]
                                file.write("\t{macroName} = {value},\n\t".format(macroName=item,value=value))
                            file.write("\n\t};\n")

                        if(attribute["Unit"] == "bitflag" and attribute["Detail"]):
                            # Motor number empty by default, and given a value when motor data packet is detected
                            motorNum=""
                            if (packetName == "MotorFaults"):
                                # Get motor number
                                motorNum = attribute["Name"][:2]
                            # iterate through detail
                            for item in attribute["Detail"]:
                                value = attribute["Detail"][item]
                                file.write("\tvirtual bool get{motorNum}{value}() const = 0;\n".format(motorNum=motorNum,value = value))
                            continue
                        # Write getter for main field
                        name = attribute["Name"].replace(" ", "")
                        # Handle case if Unit is flag to use type as atribute name 
                        if (attribute["Unit"] == "flag"):
                            type=attribute["Name"]
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

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'output.json')
with open(file_path) as json_file:
    data = json.load(json_file)
test = DataLayer(json=data)
test.generateInterface()