from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import PlaneChosenCords2D

from src.dataSource import DataSource
from src.parameters import Parameters, ExportMethod, GraphType


class App(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        main_layout = QGridLayout()
        border = QGridLayout()
        input_layout = QGridLayout()

        main_layout.addWidget(Color('black'), 0, 0, 4, 2)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        main_layout.addLayout(border, 4, 0, 2, 2)

        border.addWidget(Color(qRgb(0, 184, 230)), 4, 0, 2, 2)

        main_layout.addLayout(input_layout, 4, 0, 2, 2)

        input_layout.addWidget(Color(qRgb(0, 0, 102)), 4, 0, 2, 2)
        input_layout.setContentsMargins(5, 5, 5, 5)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 1000, 600)
        self.setFixedSize(1000, 600)
        self.setWindowTitle("MDAVT")
        grid = QGridLayout()
        self.setLayout(grid)

        strategy_type_label = QLabel(self)
        strategy_type_label.setText("Strategy Type")
        strategy_type_label.setFixedWidth(165)
        strategy_type_label.setFixedHeight(30)
        strategy_type_label.setGeometry(90, 425, 200, 200)
        strategy_type_label.setStyleSheet("QLabel { background-color : qRgb(0, 0, 102);"
                                          "color : white;"
                                          "font-size: 10pt;"
                                          "font-weight:600;}")

        strategy_type_combobox = QComboBox(self)
        strategy_type_combobox.addItems(["2D Plane with chosen cords",
                                         "2D Plane Linear Combination",
                                         "Parallel Coordinates"])
        strategy_type_combobox.setFixedWidth(165)
        strategy_type_combobox.setFixedHeight(30)
        strategy_type_combobox.setGeometry(200, 425, 200, 200)

        display_type_label = QLabel(self)
        display_type_label.setText("Display Type")
        display_type_label.setFixedWidth(165)
        display_type_label.setFixedHeight(30)
        display_type_label.setGeometry(90, 465, 200, 200)
        display_type_label.setStyleSheet("QLabel { background-color : qRgb(0, 0, 102);"
                                         "color : white;"
                                         "font-size: 10pt;"
                                         "font-weight:600;}")

        display_type_combobox = QComboBox(self)
        display_type_combobox.addItems(["Graph", "Data Series"])
        display_type_combobox.setFixedWidth(165)
        display_type_combobox.setFixedHeight(30)
        display_type_combobox.setGeometry(200, 465, 200, 200)

        text_edit_label = QLabel(self)
        text_edit_label.setText("Open File")
        text_edit_label.setFixedWidth(165)
        text_edit_label.setFixedHeight(30)
        text_edit_label.setGeometry(90, 505, 200, 200)
        text_edit_label.setStyleSheet("QLabel { background-color : qRgb(0, 0, 102);"
                                      "color : white;"
                                      "font-size: 10pt;"
                                      "font-weight:600;}")

        text_edit_field = QPlainTextEdit(self)
        text = "File path"
        text_edit_field.setPlainText(text)
        text_edit_field.setFixedWidth(165)
        text_edit_field.setFixedHeight(30)
        text_edit_field.setGeometry(200, 505, 200, 200)

        input_parameter_label = QLabel(self)
        input_parameter_label.setText("Parameter")
        input_parameter_label.setFixedWidth(165)
        input_parameter_label.setFixedHeight(30)
        input_parameter_label.setGeometry(90, 545, 200, 200)
        input_parameter_label.setStyleSheet("QLabel { background-color : qRgb(51, 0, 102);"
                                            "color : white;"
                                            "font-size: 10pt;"
                                            "font-weight:600;}")

        input_parameter_field = QPlainTextEdit(self)
        input_parameter_field.setFixedWidth(165)
        input_parameter_field.setFixedHeight(30)
        input_parameter_field.setGeometry(200, 545, 200, 200)

        execution_button = QPushButton('Display', self)
        execution_button.setStyleSheet("QPushButton { color : black;font-size: 16pt; }")
        execution_button.setFixedWidth(300)
        execution_button.setFixedHeight(100)
        execution_button.setGeometry(550, 448, 200, 200)
        #execution_button.clicked.connect(self.render())


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


def window():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


#window()

data_source = DataSource(r"C:\Users\Daniel\Desktop\wine.csv")
data = data_source.parse_data()
cords = PlaneChosenCords2D.ChosenCords()
params = Parameters(GraphType.chosen_coords, ExportMethod.bitmap, [1, 3])
cords.execute(params, data)
#print()