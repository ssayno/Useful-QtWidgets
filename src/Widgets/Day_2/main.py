#!/usr/bin/env python3


from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton
from src.Button.fButton import (AnimationQPushButton, ConicalButton, ELAnimationQPushButton,
                                LinerButton, RadialButton)


class Day_Two(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.add_widget()

    def add_widget(self):
        self.second_layout = QVBoxLayout()
        self.second_layout.setStretchFactor(self, 1)
        self.second_layout.setContentsMargins(0, 0, 0, 0)
        self.second_layout.setSpacing(10)
        self.setLayout(self.second_layout)
        #
        self.colorful_button = QPushButton("Click Me!")
        # self.colorful_button.setMinimumHeight(400)
        self.second_layout.addWidget(self.colorful_button)
        #
        self.conical_button = ConicalButton(self)
        # self.conical_button.setMinimumHeight(400)
        self.conical_button.setText('Conical Bg Button')
        self.linear_button = LinerButton(self)
        # self.linear_button.setMinimumHeight(400)
        self.linear_button.setText("Linear Bg Button")
        #
        self.radial_button = RadialButton(self)
        self.radial_button.setText('Radial Button')
        # clicked Animation Button
        self.click_button = AnimationQPushButton(self)
        self.click_button.setText("click me to shake!")
        # enter or leave animation Button
        self.el_button = ELAnimationQPushButton(self)
        self.el_button.setText("enter or leave show aniamtion")
        # layout add button
        self.second_layout.addWidget(self.conical_button)
        self.second_layout.addWidget(self.linear_button)
        self.second_layout.addWidget(self.radial_button)
        self.second_layout.addWidget(self.click_button)
        self.second_layout.addWidget(self.el_button)
