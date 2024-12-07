'''
Packet Parser. This file is responsible for generating all the appropiate files from CSV file.
    @Author:
        David Solano
'''

import os 
import sys
import logging

class PacketParser():

    def __init__(self, csv_filePath):
        '''
        Constructor method. Initiates and the csv filepath for the desired CSV file
            @params:
                self -> self build in action\n
                csv_filePath -> String
            @return:
                None 
        '''
        self.csv_filePath = csv_filePath
        self.tempFolder_path = ""

    
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
        Creates a hidden temp folder in the same location the "PacketParser is located. This is the location in which all the generated cpp files
        will be saved.
            @params:
                self -> build in action
            @return:
                tempFolder_path -> String
        '''
        self.tempFolder_path = ""
        try:
            return self.tempFolder_path
        except Exception as e:
            logging.error("Raise error while in tempFolder. Error -> %s",e)

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
            self.tempFolder()
        except Exception as e:
            logging.error("Raised error while in overall_parseExecution.")
            return "Failed: Hidden Temp Folder Creation"
