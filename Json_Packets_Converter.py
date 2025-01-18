'''
Class responsible for taking Json file and generating .cpp files based on the contents of Json sile
'''

import logging
import json

class Json_Packets_Converter():
     
    def __init__(self, json_filePath, saved_filePath):
        '''
        Constructor method that takes the location json file and the location in where the cpp files will be saved on
            @params:
                self -> build in action\n
                json_filePath -> String
                saved_filePath -> String
        '''
        self.json_filePath = json_filePath
        self.saved_filePath = saved_filePath
    
    def parse_headers(self):
        '''
        Function that takes the contents of the Json file and generates cpp header files accordingly
            @params:
                self -> build in action
            @return:
                cppFiles_filePath -> String
        '''
        try:
            # Read the JSON file
            with open(self.json_filePath, 'r') as file:
                json_data = json.load(file)

            # Process the data to create cpp headers
            cpp_file_path = self.generate_cpp_header(json_data)
            return cpp_file_path

        except Exception as e:
            logging.error("Raised error while parsing the JSON file. Error -> %s", e)
            return "Failed: System error was unable to convert JSON into cpp header files"

    def generate_cpp_header(self, json_data):
        '''
        Function that processes the JSON data and generates the corresponding C++ header file.

        @params:
            json_data -> dict: Parsed JSON data.

        @return:
            cpp_file_path -> String: Path to the saved header file.
        '''
        try:
            cpp_header_content = ""
            
            for class_data in json_data.get("classes", []):
                class_name = class_data.get("class_name", "UnknownClass")
                cpp_header_content += f"#ifndef {class_name.upper()}_H\n"
                cpp_header_content += f"#define {class_name.upper()}_H\n\n"
                
                cpp_header_content += f"class {class_name} {{\n"
                cpp_header_content += "public:\n"

                # Add member variables and methods
                for member in class_data.get("members", []):
                    cpp_header_content += f"    {member.get('type', 'void')} {member.get('name', 'undefined')};\n"
                for method in class_data.get("methods", []):
                    cpp_header_content += f"    {method.get('return_type', 'void')} {method.get('name', 'undefined')}();\n"

                cpp_header_content += "};\n\n"
                cpp_header_content += f"#endif // {class_name.upper()}_H\n"

            # Saving the generated C++ header content to file
            cpp_file_path = f"{self.saved_filePath}/generated_header.h"
            with open(cpp_file_path, 'w') as file:
                file.write(cpp_header_content)
            
            return cpp_file_path
        
        except Exception as e:
            logging.error("Error in generating cpp header file. Error -> %s", e)
            return "Failed to generate cpp header file."