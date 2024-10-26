import re

class BusinessLayerGen:
    def __init__(self, data):
        self.data = data
        
    def genJsonMessageBuilder(self):
        print("Generating I_JsonMessageBuilder.h")

        interfaceNewLines = ""
        headerNewLines = ""

        for key, value in self.data.items():
            if(value[0]["Detail"]["Quantity"] > 1 or self.__compareStringIntDifference([item["Name"] for item in value])):
                classType = "QJsonArray"
            else:
                classType = "QJsonObject"

            className = "build" + key + "Message"
            classParams = "(const I_" + key + "Data& data)"

            interfaceNewLine = "virtual " + classType + " " + className + classParams + " = 0;\n\t"
            interfaceNewLines += interfaceNewLine

            headerNewLine = classType + " " + className + classParams + ";\n\t"
            headerNewLines += headerNewLine

        interfaceTemplatePath = "./BusinessLayer/Templates/I_JsonMessageBuilder.h"
        headerTemplatePath = "./BusinessLayer/Templates/JsonMessageBuilder.h"

        with open(interfaceTemplatePath, "r") as file:
            content = file.read()

        content = content.replace("$$PUBLIC_FUNCTIONS$$", interfaceNewLines)

        with open('Output/I_JsonMessageBuilder.h', 'w') as file:
            file.write(content)

        print("I_JsonMessageBuilder.h generated successfully")

        with open(headerTemplatePath, "r") as file:
            content = file.read()

        content = content.replace("$$PUBLIC_FUNCTIONS$$", headerNewLines)

        with open('Output/JsonMessageBuilder.h', 'w') as file:
            file.write(content)

        print("JsonMessageBuilder.h generated successfully")

    def __stringsDifferByNumber(self, str1, str2):
        int1 = re.findall(r'\d+', str1)
        int2 = re.findall(r'\d+', str2)

        mod1 = re.sub(r'\d+', '', str1)
        mod2 = re.sub(r'\d+', '', str2)

        if int1 and int2:
            int1 = int(int1[0])
            int2 = int(int2[0])
        else:
            return False

        if mod1 == mod2 and int1 == int2 + 1 or int2 == int1 + 1:
            return True
        return False

    def __compareStringIntDifference(self,strings):
        for i in range(len(strings)):
            for j in range(i + 1, len(strings)):
                if self.__stringsDifferByNumber(strings[i], strings[j]):
                    return True
        return False
            
