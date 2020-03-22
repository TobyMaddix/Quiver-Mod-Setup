import setup
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class app_gui():
    def __init__(self):
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
        self.main_layout.addWidget(self.browsePath,0,1)

        self.browseButton = QPushButton("Browse")
        self.main_layout.addWidget(self.browseButton,0,2)
        self.browseButton.clicked.connect(self.function_getdir)
    def create_layout_created(self):
        self.createLoad = QProgressBar()
        self.main_layout.addWidget(self.createLoad,1,0)

    def create_window(self):
        self.main_window = QWidget()
        self.main_window.setLayout(self.main_layout)

        self.main_window.setGeometry(500, 500, 300, 60)
        self.main_window.setMinimumSize(300,60)
        self.main_window.setWindowTitle("Quiver Mod Setup")
        #self.main_window.setWindowFlags(Qt.FramelessWindowHint)
        
        self.main_window.setStyleSheet(open("resource/gui/style.css").read())

        self.main_window.show()
    
    def function_getdir(self):
        self.browse = QFileDialog()
        self.browse.setFileMode(QFileDialog.Directory)
        
        #filenames = browse.QStringList()

        #if browse.exec_():
            #filenames = browse.selectedFiles()

    def function_createmod(self):
        self.gui_createmod()
        #setupmod = setup.mod(self.createPath.text(),"resource\createmod.zip")
        #setupmod.mod_extract()
        #del setupmod

    def gui_createmod(self):
        self.createPath.setDisabled(True)
        self.createButton.setDisabled(True)

        self.createProgress = QProgressBar()
        self.main_layout.addWidget(self.createProgress,1,0)


app=app_gui()