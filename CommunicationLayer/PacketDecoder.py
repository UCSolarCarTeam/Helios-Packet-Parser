import os
import re
import json

class PacketDecoder:
    def __init__ (self, parsedData):
        self.basicHeader = "#pragma once\n\n#include <QObject>\n"
        self.parsedData = parsedData
        self.type = ""
        self.directory_name = "CommunicationLayer/PacketDecoder"
        self.current_directory = os.getcwd()
        # Generate Folder path
        self.directory_path = os.path.join(self.current_directory, self.directory_name)
        # Make folder if not exist
        os.makedirs(self.directory_path, exist_ok=True)

    def generateInterface(self):
        fileName = "I_PacketDecoder.h"
        className = fileName[:-2]
        # Make new folder
        filePath = os.path.join(self.directory_path, fileName)

        # Create the header file
        with open(filePath,"w") as file:
            file.write(self.basicHeader)
            for sectionName in self.parsedData:
                file.write('#include "../MessagingFramework/{section}Message.h"\n'.format(section=sectionName))
            file.write("\n")
            file.write("class {name} : public QObject \n{{\n\tQOBJECT\npublic:\n".format(name=className))
            file.write("\tvirtual ~{name}() {{}}\n\n".format(name=className))
            file.write("signals:\n")
            for sectionName in self.parsedData:
                file.write("\tvoid packetDecoded(const {section}Message);\n".format(section=sectionName))
            file.write("};\n")
            file.close()

    def generateHeader(self):
        fileName = "PacketDecoder.h"
        className = fileName[:-2]
        filePath = os.path.join(self.directory_path, fileName)
        with open(filePath,"w") as file:
            file.write(self.basicHeader)
            file.write("#include<QElapsedTimer>\n")
            file.write('#include "I_PacketDecoder.h"\n')
            file.write("class I_PacketChecksumChecker;\n\n")
            file.write("class {name} : public I_{name}\n{{\n\tQOBJECT\npublic:\n".format(name=className))
            file.write("\texplicit {name}(const I_PacketChecksumChecker& checksumChecker);\n".format(name=className))
            file.write("\tvirtual ~{name}();\n\n".format(name=className))
            file.write("private slots:\n\tvoid handleValidData(QByteArray messageData);\n\n};")
            file.close()

    def generateSource(self):
        fileName = "PacketDecoder.cpp"
        className = fileName[:-4]
        filePath = os.path.join(self.directory_path, fileName)
        with open(filePath,"w") as file:
            file.write("#include<QDebug>\n#include<QElapsedTimer>\n\n")
            file.write('#include "{name}.h"\n'.format(name=className))
            file.write('#include "../PacketChecksumChecker/I_PacketChecksumChecker.h"\n')
            file.write('#include "../MessagingFramework/MessageDefines.h"\n\n')
            file.write("namespace\n{\n\tconst int INDEX_OF_PACKET_TYPE = 0;\n}\n\n")
            file.write("{name}::{name}(const I_PacketChecksumChecker& checksumChecker)\n".format(name=className))
            file.write("{\n\tconnect(&checksumChecker, SIGNAL(validDataReceived(QByteArray)),\n")
            file.write("\t\t\tthis, SLOT(handleValidData(QByteArray)));\n}\n\n")
            file.write("{name}::~{name}()\n{{\n}}\n\n".format(name=className))
            file.write("void {name}::handleValidData(QByteArray messageData)\n{{\n".format(name=className))
            file.write("\tMessageDefines::Type messageType =\n")
            file.write("\t\tstatic_cast<MessageDefines::Type>(messageData.at(INDEX_OF_PACKET_TYPE));\n\n")
            file.write("\tif (MessageDefines::getLengthForMessage(messageType) == messageData.size())\n")
            file.write("\t{\n\t\tswitch (messageType)\n\t\t{")

            for sectionName in self.parsedData:
                snakeCaseName = re.sub(r'(?<!^)(?=[A-Z0-9])', '_', sectionName).upper()

                file.write("\n\t\t\tcase MessageDefines::{section}:\n".format(section=snakeCaseName))
                file.write("\t\t\t\temit packetDecoded({section}Message(messageData));\n\t\t\t\treturn;\n".format(section=sectionName))

            file.write("\t\t}\n\t}\n")
            file.write('\telse\n\t{\n\t\tqWarning() << "Message length is not correct for type" << static_cast<quint8>(messageType);')
            file.write('\n\t\tqWarning() << "Actual" << messageData.size() << "Expected" << MessageDefines::getLengthForMessage(messageType);')
            file.write('\n\t}\n}')
            file.close()
