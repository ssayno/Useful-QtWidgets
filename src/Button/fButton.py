#!/usr/bin/env python3
from PyQt5.QtCore import QPoint, QPointF, Qt
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QLinearGradient, QPaintEvent, QPainter, QPen, QRadialGradient
from PyQt5.QtWidgets import QPushButton

basic_style = '''\
QPushButton:hover{
background-color: white;
color: black;
}
'''
class ConicalButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumWidth(100)
        self.setMinimumHeight(100)
        self.setStyleSheet(basic_style)
        self.setAutoFillBackground(True)

    def paintEvent(self, a0: QPaintEvent) -> None:
        current_half_width = int(self.width() / 2)
        current_half_height = int(self.height() / 2)
        painter = QPainter(self)
        conical_bg = QConicalGradient(QPointF(current_half_width, current_half_height), 120)
        # conical_bg.setAngle(120)
        # conical_bg.setCenter(current_half_width, current_half_height)
        conical_bg.setColorAt(0, QColor('green'))
        conical_bg.setColorAt(0.33, QColor('red'))
        conical_bg.setColorAt(0.66, QColor('blue'))
        conical_bg.setColorAt(1, QColor('green'))
        pen = QPen(QColor('yellow'), 0, Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.setBrush(QBrush(conical_bg))
        # print(self.x(), self.y(), self.width(), self.height())
        # drawRect and fillRect is very different
        painter.fillRect(self.rect(), conical_bg)
        painter.drawText(QPoint(current_half_width, current_half_height), 'Conical')
        return super().paintEvent(a0)


class LinerButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumWidth(100)
        self.setMinimumHeight(100)
        self.setStyleSheet(basic_style)
        self.setAutoFillBackground(True)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        linear_bg = QLinearGradient(0, 0, self.width(), self.height())
        """
        stop:0 #1BDAF9,
        stop: 0.5 #5FEEB8,
        stop:1 #1BDAF9);
        """
        linear_bg.setColorAt(0, QColor('red'))
        linear_bg.setColorAt(0.3, QColor('yellow'))
        linear_bg.setColorAt(1, QColor('blue'))
        painter.setBrush(QBrush(linear_bg))
        # painter.drawRect(self.rect())
        painter.fillRect(self.rect(), linear_bg)
        return super().paintEvent(a0)


class RadialButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumWidth(100)
        self.setMinimumHeight(100)
        self.setStyleSheet(basic_style)
        self.setAutoFillBackground(True)

    def paintEvent(self, a0: QPaintEvent) -> None:
        current_half_width = int(self.width() / 2)
        current_half_height = int(self.height() / 2)
        painter = QPainter(self)
        """
        stop:0 #1BDAF9,
        stop: 0.5 #5FEEB8,
        stop:1 #1BDAF9);
        """
        radial_bg = QRadialGradient(QPointF(current_half_width + self.x(), current_half_height+self.y()), 100)
        # radial_bg = QRadialGradient(QPointF(current_half_width, current_half_height), 100)
        # radial_bg = QRadialGradient()
        #radial_bg.setCenter(QPointF(current_half_width, current_half_height))
        #radial_bg.setRadius(100)
        radial_bg.setColorAt(0, QColor('red'))
        radial_bg.setColorAt(0.3, QColor('yellow'))
        radial_bg.setColorAt(1, QColor('blue'))
        painter.setBrush(QBrush(radial_bg))
        painter.fillRect(self.rect(), radial_bg)
        return super().paintEvent(a0)
