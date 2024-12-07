'''
This file is reposible for the execution of the PacketParse project.
    @Author: David Solano
    @Version: 01.00.01
'''

# Imports
from PyQt6.QtWidgets import *
import sys
from MainWindow import MainWindow
class Main:

    def __init__(self):
        pass

    def show_MainWindow(self):
        self.mainWindow =  MainWindow()
        self.mainWindow.show()

def main():
    app = QApplication(sys.argv)
    controller =  Main()
    controller.show_MainWindow()
    sys.exit(app.exec())     

if __name__ =="__main__":
    main()
4