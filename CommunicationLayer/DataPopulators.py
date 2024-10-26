import os

class DataPopulators:
    def __init__ (self, parsedData):
        self.basicHeader = '#pragma once\n\n#include <QObject>\n#include "../../CommunicationLayer/PacketDecoder/I_PacketDecoder.h"\n'
        self.parsedData = parsedData
        self.type = ""
        self.directory_name = "Output/CommunicationLayer/DataPopulators"
        self.current_directory = os.getcwd()
        # Generate Folder path
        self.directory_path = os.path.join(self.current_directory, self.directory_name)
        # Make folder if not exist
        os.makedirs(self.directory_path, exist_ok=True)

    def generateHeader(self, sectionName):
        className = f"{sectionName}Populator"
        fileName = f"{className}.h"
        # Make new folder
        filePath = os.path.join(self.directory_path, fileName)

        # Create the header file
        with open(filePath,"w") as file:
            file.write(self.basicHeader)
            file.write(f'#include "../../DataLayer/{sectionName}Data/I_{sectionName}Data.h"\n\n')
            file.write(f"class {className} : public QObject\n{{\n\tQOBJECT\npublic:\n")
            sectionLowercase = sectionName[0].lower() + sectionName[1:]
            file.write(f"\t{className}(I_PacketDecoder& packetDecoder, I_{sectionName}Data& {sectionLowercase})\n\n")
            file.write(f"public slots:\n\tvoid populateData(const {sectionName}Message);\n\n")
            file.write(f"private:\n\tI_PacketDecoder& packetDecoder_;\n\tI_{sectionName}Data& {sectionLowercase}Data_;\n")
            file.write("};\n")
            file.close()

    def generateFiles(self):
        for className in self.parsedData:
            self.generateHeader(className)