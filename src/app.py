from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class App(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("MDAVT")

        label = QLabel("Test string")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


def window():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


window()