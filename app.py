import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Project')

        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.button = QPushButton("Click")

        self.button.clicked.connect(self.changeDisplay)

        self.layout.addWidget(self.display)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def changeDisplay(self):
        self.display.setText("1")


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
