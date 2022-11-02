#!/usr/bin/env python3
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QSlider, QStyleFactory, QVBoxLayout, QWidget

basic_sytle = '''\
QLabel{
qproperty-alignment: AlignCenter;
font: 20px;
}
'''
class Day_Four(QWidget):
    update_frame_bg_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet(basic_sytle)
        self._layout = QVBoxLayout(self)
        self.setLayout(self._layout)
        self.update_frame_bg_signal.connect(self.update_frame_background_color)
        self.add_widget()

    def add_widget(self):
        #
        self.color_show_Frame = QFrame()
        self.color_show_Frame.setMinimumHeight(300)
        self.color_show_Frame.setFrameShape(QFrame.Panel)
        self.color_show_Frame.setAutoFillBackground(True)
        start_color_code = self.color_show_Frame.palette().color(QPalette.Background)
        start_html_color_code = start_color_code.name()
        start_red_value = start_color_code.red()
        start_green_value = start_color_code.green()
        start_blue_value = start_color_code.blue()
        # self.color_button = QPushButton()
        # self.color_button.setAutoFillBackground(True)
        # self.color_button.setText('What Can I do')
        # self.color_button.setFixedWidth(180)
        # #
        self.hex_label = QLabel(f'HTML Color: {start_html_color_code}')
        self.red_label = QLabel(f'Red: {start_red_value}')
        self.red_slider = Color_Slider(self.red_label, self.update_frame_bg_signal, self)
        self.green_label = QLabel(f'Green: {start_green_value}')
        self.green_slider = Color_Slider(self.green_label, self.update_frame_bg_signal, self)
        self.blue_label = QLabel(f'Blue: {start_blue_value}')
        self.blue_slider = Color_Slider(self.blue_label, self.update_frame_bg_signal, self)
        self.red_slider.setValue(start_red_value)
        self.red_slider.setFocus()
        self.green_slider.setValue(start_green_value)
        self.blue_slider.setValue(start_blue_value)
        #
        self._layout.addWidget(self.hex_label)
        self._layout.addWidget(self.color_show_Frame)
        self._layout.addWidget(self.red_label)
        self._layout.addWidget(self.red_slider)
        self._layout.addWidget(self.green_label)
        self._layout.addWidget(self.green_slider)
        self._layout.addWidget(self.blue_label)
        self._layout.addWidget(self.blue_slider)

    def update_frame_background_color(self):
        palette = self.color_show_Frame.palette()
        red_value = int(self.red_slider.value())
        green_value = int(self.green_slider.value())
        blue_value = int(self.blue_slider.value())
        bg_color = QColor(red_value, green_value, blue_value)
        hex_value = bg_color.name()
        self.hex_label.setText(f'HTML Color: {hex_value}')
        palette.setColor(QPalette.Active, QPalette.Window, bg_color)
        palette.setColor(QPalette.Active, QPalette.ButtonText, QColor('black'))
        self.color_show_Frame.setPalette(palette)


class Color_Slider(QSlider):
    def __init__(self, connect_label:QLabel, update_signal, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setMinimum(0)
        self.cl = connect_label
        self.us = update_signal
        self.setMaximum(255)
        self.hasFocus()
        # self.setStyle(QStyleFactory.create('Fusion'))
        self.setOrientation(Qt.Horizontal)
        self.valueChanged.connect(self.update_connect_label_info)

    def update_connect_label_info(self, value):
        self.us.emit()
        origin_text = self.cl.text()
        prefix = origin_text.split(':')[0]
        self.cl.setText(f'{prefix}: {value}')
