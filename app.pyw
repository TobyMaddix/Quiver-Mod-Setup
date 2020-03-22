import setup
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class app_gui():
    def __init__(self):
        self.editFirst = False
        app = QApplication([]) #init app
        app.setStyle("fusion")

        self.create_layout_base()
        self.create_window()

        app.exec_()
    def create_layout_base(self):
        self.main_layout = QGridLayout()

        self.logo = QLabel()
        self.logo.setPixmap(QPixmap("resource/gui/logo.png"))
        self.main_layout.addWidget(self.logo,0,0)

        self.browsePath = QLineEdit()
        self.browsePath.setPlaceholderText("Path to create mod")
        self.browsePath.textChanged.connect(self.function_browse_edit)
        self.main_layout.addWidget(self.browsePath,0,1)

        self.browseButton = QPushButton("Browse")
        self.browseButton.clicked.connect(self.function_getdir)
        self.main_layout.addWidget(self.browseButton,0,2)
    def create_window(self):
        #define the window
        self.main_window = QWidget()
        self.main_window.setLayout(self.main_layout)
        #sets the window size and global style ect
        self.main_window.setMinimumSize(400,60)
        self.main_window.setMaximumSize(400,60)
        self.main_window.setGeometry(500, 500, 400, 60)
        self.main_window.setWindowTitle("Quiver Mod Setup")
        self.main_window.setStyleSheet(open("resource/gui/style.css").read())
        #show the window
        self.main_window.show()
    
    def function_getdir(self):
        browseSelection = str(QFileDialog.getExistingDirectory())
        self.browsePath.setText(browseSelection)
    
    def function_browse_edit(self):
        if (self.editFirst == False):
            self.editFirst = True
            self.gui_browse_edit()
    def gui_browse_edit(self):
        #add create mod button
        self.createmodButton = QPushButton("Create Mod")
        self.createmodButton.clicked.connect(self.function_createmod)
        self.main_layout.addWidget(self.createmodButton,1,0,1,3)
        #set size of window for new button
        self.main_window.setMinimumSize(400,100)
        self.main_window.setMaximumSize(400,100)
        self.main_window.setGeometry(500, 500, 400, 100)

    def function_createmod(self):
        self.gui_createmod()
        setupmod = setup.mod(self.browsePath.text(),"resource\createmod.zip")
        setupmod.mod_extract()
        del setupmod
    def gui_createmod(self):
        self.browsePath.setDisabled(True)
        self.browseButton.setDisabled(True)
        self.createmodButton.setDisabled(True)


app=app_gui()