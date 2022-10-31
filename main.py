#!/usr/bin/env python3
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSplitter, QStackedWidget, QVBoxLayout, QWidget
from src.progressbar import OwnProgressbar

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.cw = QStackedWidget(self)
        self.setCentralWidget(self.cw)
        #
        self.first_day = QWidget(self)
        self.fd_layout = QVBoxLayout()
        self.first_day.setLayout(self.fd_layout)
        #
        self.cw.addWidget(self.first_day)
        #
        self.add_widget()

    def add_widget(self):
        spl = QSplitter()
        spl.setOrientation(Qt.Vertical)
        button = QPushButton("Start Animation")
        self.opb = OwnProgressbar(self)
        self.opb.hasFocus()
        spl.addWidget(button)
        spl.addWidget(self.opb)
        self.fd_layout.addWidget(spl)
        button.clicked.connect(self.show_progressbar)

    def show_progressbar(self):
        self.opb.set_value()

if __name__ == '__main__':
    print("用于记录一些常用的 Qt 控件")
    app = QApplication(sys.argv)
    mu = MainUI()
    mu.show()
    sys.exit(app.exec_())
