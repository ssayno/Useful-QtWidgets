#!/usr/bin/env python3
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QMainWindow, QApplication, QPushButton, QSplitter, QStackedWidget, QToolTip, QVBoxLayout, QWidget
from src.Widgets.Day_4.main import Day_Four
from src.Widgets.Day_2.main import Day_Two
from src.progressbar import OwnProgressbar
from src.Button.fButton import PaletteButton

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(600)
        self.setMinimumWidth(600)
        self.cw = QWidget(self)
        self.setCentralWidget(self.cw)
        self.cw_layout = QHBoxLayout()
        self.cw.setLayout(self.cw_layout)
        # sub stacked layout
        """
        sub stakced layout
        """
        self.spl = QSplitter(self)
        self.cw_layout.addWidget(self.spl)
        #
        self.set_day_button()
        self.sub_stack_widget = QStackedWidget()
        # create day button frame
        self.spl.addWidget(self.sub_stack_widget)
        # first day
        self.add_first_day_widget()
        # second day
        self.add_second_day_widget()
        #
        self.add_third_day_widget()
        #
        self.add_fourth_day_widget()
        # connect button with slot func
        self.connect_day_button_with_slot_func()
        # time
        self.sub_stack_widget.setCurrentWidget(self.four_day)

    def set_day_button(self):
        self.day_frame = QFrame(self)
        self.day_frame.setFrameShape(QFrame.StyledPanel)
        self.day_frame.setStyleSheet('QFrame{border-radius: 8px; border: 2px solid grey;}')
        self.spl.addWidget(self.day_frame)
        self.day_layout = QGridLayout()
        self.day_frame.setLayout(self.day_layout)
        # first button
        self.first_day_button = QPushButton("First Day")
        self.day_layout.addWidget(self.first_day_button)
        # second button
        self.second_day_button = QPushButton("Second Day")
        self.day_layout.addWidget(self.second_day_button)
        # third button
        self.third_day_button = QPushButton("Third Day")
        self.day_layout.addWidget(self.third_day_button)
        # fourth button
        self.fourth_day_button = QPushButton("Fourth Day")
        self.day_layout.addWidget(self.fourth_day_button)

    def connect_day_button_with_slot_func(self):
        self.first_day_button.clicked.connect(
            lambda: self.sub_stack_widget.setCurrentWidget(self.first_day)
        )
        self.second_day_button.clicked.connect(
            lambda: self.sub_stack_widget.setCurrentWidget(self.second_day)
        )
        self.third_day_button.clicked.connect(
            lambda: self.sub_stack_widget.setCurrentWidget(self.third_day)
        )
        self.fourth_day_button.clicked.connect(
            lambda: self.sub_stack_widget.setCurrentWidget(self.four_day)
        )

    def add_first_day_widget(self):
        self.first_day = QWidget(self)
        self.first_day.setStyleSheet('QLabel{border: 5px solid black;}')
        self.fd_layout = QVBoxLayout()
        self.fd_layout.addStretch()
        self.first_day.setLayout(self.fd_layout)
        #
        self.sub_stack_widget.addWidget(self.first_day)
        # day button
        label = QLabel("Just For Test")
        label.setToolTip("Click me to jump to <a href='https://www.github.com/'>github</a>github.")
        label.setAlignment(Qt.AlignCenter)
        button = QPushButton("Start Animation")
        button.setToolTip("hello <a href='https://www.github.com/'>ssayno</a>")
        self.opb = OwnProgressbar(self)
        self.fd_layout.addWidget(label, stretch=2)
        self.fd_layout.addWidget(button, stretch=5)
        self.fd_layout.addWidget(self.opb, stretch=3)
        button.clicked.connect(self.show_progressbar)

    # Mon Oct 31 22:20:56 2022
    def add_second_day_widget(self):
        self.second_day = Day_Two(self)
        self.sub_stack_widget.addWidget(self.second_day)

    def add_third_day_widget(self):
        self.third_day = QWidget(self)
        self.third_day_layout = QVBoxLayout(self.third_day)
        self.third_day.setLayout(self.third_day_layout)
        self.third_day_layout.setContentsMargins(0, 0, 0, 0)
        #
        self.sub_stack_widget.addWidget(self.third_day)
        #
        change_status_button = QPushButton("change status")
        self.paletteButton = PaletteButton(self.third_day)
        self.paletteButton.setText('Palette Button')
        change_status_button.clicked.connect(self.paletteButton.change_status)
        #
        self.third_day_layout.addWidget(change_status_button)
        self.third_day_layout.addWidget(self.paletteButton)

    def add_fourth_day_widget(self):
        self.four_day = Day_Four(self)
        self.sub_stack_widget.addWidget(self.four_day)

    def show_progressbar(self):
        self.opb.set_value()

if __name__ == '__main__':
    print("用于记录一些常用的 Qt 控件")
    app = QApplication(sys.argv)
    mu = MainUI()
    mu.show()
    sys.exit(app.exec_())
