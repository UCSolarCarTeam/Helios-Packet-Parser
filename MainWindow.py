'''
Main Window
    @Author:
        David Solano
'''

# Imports:
import logging
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import os
import sys


# This is needed for the one executable file to work:
def resource_path(relative_path):
    '''
    Function to get the temp folder path when the executable file running
        @params:
            relative_path -> (String)
        @return:
            base_path + relative_path -> (String)
    '''
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    except Exception as e:
        logging.error('Raised error while in resource_path. Error -> %s.', e) 

class MainWindow(QMainWindow):


    def __init__(self):
        '''
        Initializes the Main window parameters
            @param:
                self -> build in action
            @retun:
                None
        '''
        try:
            super().__init__()
            width = 550
            height =700
            self.setFixedWidth(550)
            self.setFixedHeight(700)
            self.current_path = os.path.dirname(__file__) # Gets current path of this file
            self.setWindowIcon(QIcon(resource_path(self.current_path + "\\SolarCarTeam_LogoIcon.ico")))
            self.setWindowTitle("Packet Parser")    
            self.resize(width, height) # Login window width and height
            # Sets the window to be displayed in the center of the screenS
            qr = self.frameGeometry()
            qr.moveCenter(self.screen().availableGeometry().center())
            self.move(qr.topLeft())

            # Default font and color
            self.default_font = QFont('Arial', 11)
            self.setFont(self.default_font)  # Apply default font to the whole application      

        # Create the tab widget
            self.tabs = QTabWidget()
            self.setCentralWidget(self.tabs)  # Set tabs as the central widget of the main window

            self.tabs.tabBar().setStyleSheet("""
                QTabBar::tab {
                    width: 275px;
                    height: 35px;
                }
            """)

            # Create the first tab
            self.tab1 = QWidget()
            self.tabs.addTab(self.tab1, "Hermes")
            self.setup_tab1()

            # Create the second tab
            self.tab2 = QWidget()
            self.tabs.addTab(self.tab2, "Dashboard")
            self.setup_tab2()
        except Exception as e:
            logging.error("Raised error initializing the MainWindow. Error -> %s", e)

    def setup_tab1(self):
        '''
        Sets up the widgets for the Hermes tab
            @param:
                self -> build in action
            @retun:
                None
        '''
        try:
            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

            # Attach File Section
            csv_label = QLabel("Attach File")
            csv_label.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                font-weight: bold;     /* Font weight */
                color: black;          /* Font color */                       
            """)
            layout.addWidget(csv_label)

            csv_input_layout = QHBoxLayout()
            self.csv_lineEdit_Hermes = QLineEdit()
            self.csv_lineEdit_Hermes.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            csv_input_layout.addWidget(self.csv_lineEdit_Hermes)
            csv_button = QPushButton("Browse")
            csv_button.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)         
            csv_button.clicked.connect(self.browse_buttonFunction_Hermes)
            csv_input_layout.addWidget(csv_button)
            layout.addLayout(csv_input_layout)

            # Generate Section
            generate_button = QPushButton("Generate")
            generate_button.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            generate_button.setFixedSize(250, 60)
            generate_button.clicked.connect(lambda: self.generate_buttonFunction_Hermes(self.csv_lineEdit_Hermes.text()))
            center_layout = QHBoxLayout()
            center_layout.addStretch()
            center_layout.addWidget(generate_button)
            center_layout.addStretch()
            layout.addLayout(center_layout)

            # Label Section
            label_layout = QHBoxLayout()
            label_layout.addStretch()
            self.hidden_label_Hermes = QLabel("This is a hidden label")
            self.hidden_label_Hermes.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: red;            /* Font color */       
                font-weight: bold;     /* Font weight */                                                   
            """)
            self.hidden_label_Hermes.setVisible(False)
            label_layout.addWidget(self.hidden_label_Hermes)
            label_layout.addStretch()
            layout.addLayout(label_layout)

            # Generated Files Section
            generated_files_label_layout = QHBoxLayout()
            generated_files_label_layout.addStretch()
            generated_files_label = QLabel("Generated Files")
            generated_files_label.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                font-weight: bold;     /* Font weight */
                color: black;          /* Font color */                       
            """)
            generated_files_label_layout.addWidget(generated_files_label)
            generated_files_label_layout.addStretch()
            layout.addLayout(generated_files_label_layout)

            # Progress Bar
            progress_bar_layout = QHBoxLayout()
            progress_bar_layout.addStretch()
            self.progress_bar_Hermes = QProgressBar()
            self.progress_bar_Hermes.setStyleSheet("""
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    background: white;
                }
                QProgressBar::chunk {
                    background-color: #4CAF50; /* Green color for progress */
                    width: 20px;
                }
            """)
            self.progress_bar_Hermes.setFixedSize(400, 25)
            self.progress_bar_Hermes.setValue(0)
            self.progress_bar_Hermes.setTextVisible(False)
            progress_bar_layout.addWidget(self.progress_bar_Hermes)
            progress_bar_layout.addStretch()
            layout.addLayout(progress_bar_layout)

            # Tree Section
            self.tree_widget_Hermes = QTreeWidget()
            self.tree_widget_Hermes.setColumnCount(1)
            self.tree_widget_Hermes.setHeaderLabels(["File Name"])
            self.tree_widget_Hermes.headerItem().setTextAlignment(0, Qt.AlignmentFlag.AlignCenter)
            self.tree_widget_Hermes.setStyleSheet("""
                QTreeWidget {
                    background: rgba(255, 255, 255, 150);  /* Semi-transparent white background for tree */
                    border: 1px solid rgba(0, 0, 0, 50);   /* Optional: Semi-transparent border */
                }
                QHeaderView::section {
                    background: rgb(77, 77, 77);           /* Matching grayish color for the header */
                    color: white;                          /* White text for better readability */
                    font-weight: bold;                     /* Header font style */
                    border: 1px solid rgba(0, 0, 0, 50);   /* Optional: Subtle border for header sections */
                }
                QTreeWidget::item {
                    background: rgba(255, 255, 255, 100);  /* Semi-transparent item background */
                }
            """)
            layout.addWidget(self.tree_widget_Hermes)

            # Save Files Section
            save_button_layout = QHBoxLayout()

            # Add stretch to center buttons
            save_button_layout.addStretch()

            # Save Selected Button
            self.save_selected_button_Hermes = QPushButton("Save Selected")
            self.save_selected_button_Hermes.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            self.save_selected_button_Hermes.setFixedSize(250, 60)
            self.save_selected_button_Hermes.setDisabled(True)  # Initially disabled
            self.save_selected_button_Hermes.clicked.connect(self.saveSelected_buttonFunction_Hermes)
            save_button_layout.addWidget(self.save_selected_button_Hermes)

            # Space between buttons
            save_button_layout.addSpacing(20)

            # Save All Files Button
            self.save_files_button_Hermes = QPushButton("Save All Files")
            self.save_files_button_Hermes.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            self.save_files_button_Hermes.setFixedSize(250, 60)
            self.save_files_button_Hermes.setDisabled(True)  # Initially disabled
            self.save_files_button_Hermes.clicked.connect(self.saveAllFiles_buttonFunction_Hermes)
            save_button_layout.addWidget(self.save_files_button_Hermes)

            # Add stretch to center buttons
            save_button_layout.addStretch()

            # Add the layout to the main layout
            layout.addLayout(save_button_layout)


            # Version Section
            version_label = QLabel("01.00.00")
            version_label.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 12px;       /* Font size */
                color: gray;           /* Font color */
                font-weight: normal;   /* Font weight */
            """)
            version_layout = QHBoxLayout()
            version_layout.addStretch()
            version_layout.addWidget(version_label)
            layout.addLayout(version_layout)

            # Set the layout for the tab
            self.tab1.setLayout(layout)

            # Background image
            current_path = os.path.dirname(__file__).replace("\\", "/").replace('c', "C")
            background_path = resource_path(current_path + "/SolarCar_Hermesbackground.png")
            if not os.path.exists(background_path):
                raise FileNotFoundError(f"Background image not found: {background_path}")
            self.tab1.setObjectName("tab1")
            self.tab1.setStyleSheet(f"""
                QWidget#tab1 {{
                    background-image: url("{background_path}");
                    background-repeat: no-repeat;
                    background-position: center;
                }}
            """)
        except Exception as e:
            logging.error("Raised error at setup_tab1. Error -> %s", e)


    def setup_tab2(self):
        '''
        Sets up the widgets for the Dashboard tab
            @param:
                self -> build in action
            @retun:
                None
        '''         
        try:
            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

            # Attach File Section
            csv_label = QLabel("Attach File")
            csv_label.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                font-weight: bold;     /* Font weight */
                color: white;          /* Font color */                       
            """)
            layout.addWidget(csv_label)

            csv_input_layout = QHBoxLayout()
            self.csv_lineEdit_Dashboard = QLineEdit()
            self.csv_lineEdit_Dashboard.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            csv_input_layout.addWidget(self.csv_lineEdit_Dashboard)
            csv_button = QPushButton("Browse")
            csv_button.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)         
            csv_button.clicked.connect(self.browse_buttonFunction_Dashboard)
            csv_input_layout.addWidget(csv_button)
            layout.addLayout(csv_input_layout)

            # Generate Section
            generate_button = QPushButton("Generate")
            generate_button.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            generate_button.setFixedSize(250, 60)
            generate_button.clicked.connect(lambda: self.generate_buttonFunction_Dashboard(self.csv_lineEdit_Dashboard.text()))
            center_layout = QHBoxLayout()
            center_layout.addStretch()
            center_layout.addWidget(generate_button)
            center_layout.addStretch()
            layout.addLayout(center_layout)

            # Label Section
            label_layout = QHBoxLayout()
            label_layout.addStretch()
            self.hidden_label_Dashboard = QLabel("This is a hidden label")
            self.hidden_label_Dashboard.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: red;            /* Font color */       
                font-weight: bold;     /* Font weight */                                                   
            """)
            self.hidden_label_Dashboard.setVisible(False)
            label_layout.addWidget(self.hidden_label_Dashboard)
            label_layout.addStretch()
            layout.addLayout(label_layout)

            # Generated Files Section
            generated_files_label_layout = QHBoxLayout()
            generated_files_label_layout.addStretch()
            generated_files_label = QLabel("Generated Files")
            generated_files_label.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                font-weight: bold;     /* Font weight */
                color: white;          /* Font color */                       
            """)
            generated_files_label_layout.addWidget(generated_files_label)
            generated_files_label_layout.addStretch()
            layout.addLayout(generated_files_label_layout)

            # Progress Bar
            progress_bar_layout = QHBoxLayout()
            progress_bar_layout.addStretch()
            self.progress_bar_Dashboard = QProgressBar()
            self.progress_bar_Dashboard.setStyleSheet("""
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    background: white;
                }
                QProgressBar::chunk {
                    background-color: #4CAF50; /* Green color for progress */
                    width: 20px;
                }
            """)
            self.progress_bar_Dashboard.setFixedSize(400, 25)
            self.progress_bar_Dashboard.setValue(0)
            self.progress_bar_Dashboard.setTextVisible(False)
            progress_bar_layout.addWidget(self.progress_bar_Dashboard)
            progress_bar_layout.addStretch()
            layout.addLayout(progress_bar_layout)

            # Tree Section
            self.tree_widget_Dashboard = QTreeWidget()
            self.tree_widget_Dashboard.setColumnCount(1)
            self.tree_widget_Dashboard.setHeaderLabels(["File Name"])
            self.tree_widget_Dashboard.headerItem().setTextAlignment(0, Qt.AlignmentFlag.AlignCenter)
            self.tree_widget_Dashboard.setStyleSheet("""
                QTreeWidget {
                    background: rgba(255, 255, 255, 150);  /* Semi-transparent white background for tree */
                    border: 1px solid rgba(0, 0, 0, 50);   /* Optional: Semi-transparent border */
                }
                QHeaderView::section {
                    background: rgb(77, 77, 77);           /* Matching grayish color for the header */
                    color: white;                          /* White text for better readability */
                    font-weight: bold;                     /* Header font style */
                    border: 1px solid rgba(0, 0, 0, 50);   /* Optional: Subtle border for header sections */
                }
                QTreeWidget::item {
                    background: rgba(255, 255, 255, 100);  /* Semi-transparent item background */
                }
            """)
            layout.addWidget(self.tree_widget_Dashboard)


            # Save Files Section
            save_button_layout = QHBoxLayout()

            # Add stretch to center buttons
            save_button_layout.addStretch()

            # Save Selected Button
            self.save_selected_button_Dashboard = QPushButton("Save Selected")
            self.save_selected_button_Dashboard.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            self.save_selected_button_Dashboard.setFixedSize(250, 60)
            self.save_selected_button_Dashboard.setDisabled(True)  # Initially disabled
            self.save_selected_button_Dashboard.clicked.connect(self.saveSelected_buttonFunction_Dashboard)
            save_button_layout.addWidget(self.save_selected_button_Dashboard)

            # Space between buttons
            save_button_layout.addSpacing(20)

            # Save All Files Button
            self.save_files_button_Dashboard = QPushButton("Save All Files")
            self.save_files_button_Dashboard.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 18px;       /* Font size */
                color: white;          /* Font color */                       
            """)
            self.save_files_button_Dashboard.setFixedSize(250, 60)
            self.save_files_button_Dashboard.setDisabled(True)  # Initially disabled
            self.save_files_button_Dashboard.clicked.connect(self.saveAllFiles_buttonFunction_Dashboard)
            save_button_layout.addWidget(self.save_files_button_Dashboard)

            # Add stretch to center buttons
            save_button_layout.addStretch()

            # Add the layout to the main layout
            layout.addLayout(save_button_layout)

            #Version Section:
                #Label:
            version_label = QLabel("01.00.00")
            version_label.setStyleSheet("""
                font-family: 'Arial';  /* Font name */
                font-size: 12px;       /* Font size */
                color: gray;           /* Font color */
                font-weight: normal;   /* Font weight */
            """)
            # Create a horizontal layout to align it to the bottom-right corner
            version_layout = QHBoxLayout()
            version_layout.addStretch()  # Stretch to push label to the right
            version_layout.addWidget(version_label)  # Add the version label to layout
            layout.addLayout(version_layout)

            # Set the layout for the tab
            self.tab2.setLayout(layout)

            # Update current path
            current_path = os.path.dirname(__file__).replace("\\", "/").replace('c', "C")
            background_path = resource_path(current_path + "/SolarCar_Dashboardbackground.png")

            # Ensure the background file exists
            if not os.path.exists(background_path):
                raise FileNotFoundError(f"Background image not found: {background_path}")

            # Set the object name for tab2
            self.tab2.setObjectName("tab2")

            # Apply the background image to tab1 only
            self.tab2.setStyleSheet(f"""
                QWidget#tab2 {{
                    background-image: url("{background_path}");
                    background-repeat: no-repeat;
                    background-position: center;
                }}
            """)
        except Exception as e:
            logging.error("Raised error at setup_tab2. Error -> %s", e)            

    def browse_buttonFunction_Hermes(self):
        '''
        Hermes: Provides a UI for users to use to select an Excel file
            @param:
                self -> build in action
            @return:
                None
        '''         
        try:
            options = QFileDialog.Option.ReadOnly  # Use specific option directly
            file_name, _ = QFileDialog.getOpenFileName(
                self,  # parent window
                "Select Excel File",  # dialog title
                "",  # default directory
                "Excel Files (*.xlsx *.xls);;All Files (*)",  # file filter for Excel files
                options=options  # pass options here
            )
            if file_name:
                self.csv_lineEdit_Hermes.setText(file_name)
        except Exception as e:
            logging.error("Raised error at browse_buttonFunction_Hermes. Error -> %s", e)         

    def generate_buttonFunction_Hermes(self, csvFilePath):
        '''
        Hermes: Generates cpp files based on the CSV file indicated by the user
            @param:
                self -> build in action\n
                csvFilePath -> String
            @retun:
                None
        '''         
        try:
            self.hidden_label_Hermes.setVisible(False)
            if(csvFilePath == '' or '.xlsx' not in csvFilePath):
                self.hidden_label_Hermes.setVisible(True)
                self.hidden_label_Hermes.setText("Invalid Filepath")
            else:
                self.hidden_label_Hermes.setVisible(False)
                print(csvFilePath)
                # Packet parser thenn generates the files onto a hidden "temp" folder inside the application and then returns the names of all files
                # These files names is then use to add the rows to the table widget.
        except Exception as e:
            logging.error("Raised error at generate_buttonFunction_Hermes. Error -> %s", e)                  

    def saveAllFiles_buttonFunction_Hermes(self):
        '''
        Hermes: Saves all files in the Tree widget data
            @param:
                self -> build in action\n
                csvFilePath -> String
            @retun:
                None
        '''              
        try:
            # Inside the "temp folder created by the Packet Parser python file all the files are compressed as a zip file. 
            # This zip file path is used to as reference to save the zip file onto user local computer 
            pass
        except Exception as e:
            logging.error("Raised error at save_files_buttonFunction_Hermes. Error -> %s", e)  

    def saveSelected_buttonFunction_Hermes(self):
        '''
        Hermes: Saves selected files indicated by the user in the Tree widget data
            @param:
                self -> build in action\n
                csvFilePath -> String
            @retun:
                None
        '''              
        try:
            # Inside the "temp folder created by the Packet Parser python file all the files are compressed as a zip file. 
            # This zip file path is used to as reference to save the zip file onto user local computer 
            pass
        except Exception as e:
            logging.error("Raised error at save_files_buttonFunction_Hermes. Error -> %s", e)                        

    def browse_buttonFunction_Dashboard(self):
        '''
        Hermes: Provides a UI for users to use to select an Excel file
            @param:
                self -> build in action
            @return:
                None
        '''         
        try:
            options = QFileDialog.Option.ReadOnly  # Use specific option directly
            file_name, _ = QFileDialog.getOpenFileName(
                self,  # parent window
                "Select Excel File",  # dialog title
                "",  # default directory
                "Excel Files (*.xlsx *.xls);;All Files (*)",  # file filter for Excel files
                options=options  # pass options here
            )
            if file_name:
                self.csv_lineEdit_Dashboard.setText(file_name)
        except Exception as e:
            logging.error("Raised error at browse_buttonFunction_Dashboard. Error -> %s", e)                

    def generate_buttonFunction_Dashboard(self, csvFilePath):
        '''
        Dashboard: Generates cpp files based on the CSV file indicated by the user
            @param:
                self -> build in action\n
                csvFilePath -> String
            @retun:
                None
        '''        
        try:
            self.hidden_label_Dashboard.setVisible(False)
            if(csvFilePath == '' or '.xlsx' not in csvFilePath):
                self.hidden_label_Dashboard.setVisible(True)
                self.hidden_label_Dashboard.setText("Invalid Filepath")
            else:
                self.hidden_label_Dashboard.setVisible(False)
                print(csvFilePath)
                # Packet parser thenn generates the files onto a hidden "temp" folder inside the application and then returns the names of all files
                # These files names is then use to add the rows to the table widget.
        except Exception as e:
            logging.error("Raised error at generate_buttonFunction_Dashboard. Error -> %s", e)                  

    def saveAllFiles_buttonFunction_Dashboard(self):
        '''
        Hermes: Saves all files in the Tree widget data
            @param:
                self -> build in action\n
                csvFilePath -> String
            @retun:
                None
        '''              
        try:
            # Inside the "temp folder created by the Packet Parser python file all the files are compressed as a zip file. 
            # This zip file path is used to as reference to save the zip file onto user local computer 
            pass
        except Exception as e:
            logging.error("Raised error at save_files_buttonFunction_Hermes. Error -> %s", e)  

    def saveSelected_buttonFunction_Dashboard(self):
        '''
        Hermes: Saves selected files indicated by the user in the Tree widget data
            @param:
                self -> build in action\n
                csvFilePath -> String
            @retun:
                None
        '''              
        try:
            # Inside the "temp folder created by the Packet Parser python file all the files are compressed as a zip file. 
            # This zip file path is used to as reference to save the zip file onto user local computer 
            pass
        except Exception as e:
            logging.error("Raised error at save_files_buttonFunction_Hermes. Error -> %s", e)          