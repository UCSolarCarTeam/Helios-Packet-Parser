'''
Packet Parser. This file is responsible for generating all the appropiate folder with its respectives files from Excel file.
    @Author:
        David Solano
'''

import os 
import logging
from pathlib import Path
import shutil
from Excel_Json_Converter import Excel_Json_Converter
from Json_Packets_Converter import Json_Packets_Converter

class PacketParser():

    def __init__(self, excel_filePath):
        '''
        Constructor method. Initiates and the csv filepath for the desired CSV file
            @params:
                self -> self build in action\n
                csv_filePath -> String
            @return:
                None 
        '''
        self.excel_filePath = excel_filePath
        self.folder_Files_list = []

    
    def parsingCSV(self):
        '''
        Creates .cpp files accordingly to the contents of the CSV file.
            @params:
                self -> build in action
            @return:
                fileList -> Array[String]
        '''
        fileList = []
        try:
            return fileList
        except Exception as e:
            logging.error("Raised error while in parsingCSV. Error -> %s", e)

    def tempFolder(self):
        '''
        Creates a hidden temp folder in the same location where the script is located. 
        This folder will be used to save all the generated cpp files.
            @params:
                self -> built-in action
            @return:
                tempFolder_path -> String
        '''
        try:
            # Get the directory where the script is located
            script_dir = Path(__file__).parent.resolve()

            # Define the folder name and path
            temp_folder_name = ".temp"  # Hidden in Unix-based systems
            temp_folder_path = script_dir / temp_folder_name

            # Create the folder if it doesn't exist
            if not temp_folder_path.exists():
                temp_folder_path.mkdir(parents=True)
                logging.info(f"Created temp folder at {temp_folder_path}")

                # Ensure the folder is hidden on Windows
                if os.name == 'nt':  # Check if the OS is Windows
                    os.system(f'attrib +h "{temp_folder_path}"')  # Use attrib to hide folder

            # Store the path in the class attribute
            tempFolder_path = str(temp_folder_path)

            return tempFolder_path

        except Exception as e:
            logging.error("Raised error while in tempFolder. Error -> %s", e)
            return "Failed: Sys error to create temp folder"
        
    def deleteFolder(self, folderPath):
        '''
        Deletes desired folder
            @params:
                self -> build in action\n
                folderPath -> String
            @return:
                deleteAction -> String 
        '''
        try:
            # Ensure the path exists
            if not os.path.exists(folderPath):
                logging.warning(f"Folder not found: {folderPath}")
                return f"Failed: Folder '{folderPath}' does not exist"

            # Delete the folder and its contents
            shutil.rmtree(folderPath)
            logging.info(f"Successfully deleted folder: {folderPath}")
            return f"Success: Folder '{folderPath}' deleted"
        except Exception as e:
            logging.error("Raised error while in deleteFolder")
            return "Failed: Sys error to delete folder"

    def overall_parseExecution(self):
        '''
        This function is solely responsible for overall executing the parsing process.
            @params:
                self -> build in action
            @return 
                NOTE: This is for now but will change
                None 
        '''
        try:
            tempFolder_path = self.tempFolder()
            if("Failed" in tempFolder_path):
                print("Failed to create tempfolder") # Inform user temp folder was unable to be created

            excelToJson_filePath = Excel_Json_Converter(self.excel_filePath, tempFolder_path).parse()
            if("Failed" in excelToJson_filePath):
                print("Failed convert Excel into Json") # Inform user that it was unable to convert Excel into Json

            # packets_header_filePath = Json_Packets_Converter(excelToJson_filePath, tempFolder_path).parse_headers()
            # if("Failed" in packets_header_filePath):
            #     print("Failed to generate Packets header files") #  Inform user that it was unable to generate Packets header files       
            # if("Failed" in self.deleteFolder(self.tempFolder())):
            #     print("Failed to delete tempfolder") # Inform user temp folder was unable to be deleted
        except Exception as e:
            logging.error("Raised error while in overall_parseExecution. Error -> %s", e)
            return "Failed: Hidden Temp Folder Creation"
        
# Testing purposes
if __name__ == "__main__":
    excelFilePath = "C:\\Users\\david\\OneDrive\\Desktop\\Personal\\SolarCar\\Helios-Packet-Parser\\Spreadsheets\\ElysiaDateSheet_4.xlsx"
    PacketParser(excelFilePath).overall_parseExecution()
