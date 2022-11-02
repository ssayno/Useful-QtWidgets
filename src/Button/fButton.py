#!/usr/bin/env python3
from PyQt5.QtCore import QAbstractAnimation, QEvent, QPoint, QPointF, QPropertyAnimation, QVariantAnimation, Qt
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QIcon, QLinearGradient, QPaintEvent, QPainter, QPalette, QPen, QRadialGradient
from PyQt5.QtWidgets import QLabel, QPushButton, QToolButton

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
        radial_bg = QRadialGradient(QPointF(current_half_width, current_half_height), 100)
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


class AnimationQPushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumWidth(100)
        self.setMinimumHeight(100)
        self.setStyleSheet(basic_style)
        self.setAutoFillBackground(True)
        self._click_animation = QPropertyAnimation(self, b'pos', self)
        self._click_animation.setStartValue(QPoint(self.x(), self.y()))
        self._click_animation.setEndValue(QPoint(self.x(), self.y()))
        self._click_animation.setDuration(100)
        self._click_animation.finished.connect(self._click_animation_finished)

    def clicked_slot_func(self):
        self._click_animation.start()
        print("Start !!")

    def _click_animation_finished(self):
        print('Finished')


class ELAnimationQPushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumWidth(100)
        self.setMinimumHeight(100)
        self.setStyleSheet(basic_style)
        self.setAutoFillBackground(True)
        self.create_animation()

    def create_animation(self):
        self._animation = QVariantAnimation(
            parent=self
        )
        # 在设定值之前连接信号槽函数，那么在设定值的时候会运行一次
        self._animation.valueChanged.connect(self.print_animation_current_value)
        start_variant = QColor(173, 213, 0)
        end_variant = QColor(50, 230, 92)
        self._animation.setStartValue(start_variant)
        self._animation.setEndValue(end_variant)
        self._animation.setDuration(250)

    def print_animation_current_value(self, value):
        color = QColor(value).name()
        qss = """
            font-weight: bold;
            color: black;
        """
        background_color = f'''\
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop: 0 grey, stop: 0.4 {color}, stop: 1 white);
        '''
        qss += background_color
        self.setStyleSheet(qss)

    def enterEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        return super().enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        return super().leaveEvent(a0)


class PaletteButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumWidth(100)
        self.setMinimumHeight(100)
        # self.setDisabled(True)
        self.changePalette()
        self.setAutoFillBackground(True)

    def changePalette(self):
        palette = self.palette()
        palette.setColor(QPalette.ButtonText, QColor('red'))
        palette.setColor(QPalette.Button, QColor('green'))
        palette.setCurrentColorGroup(QPalette.Inactive)
        palette.setColor(QPalette.Inactive, QPalette.ButtonText, QColor('red'))
        palette.setColor(QPalette.Inactive, QPalette.Button, QColor('white'))
        self.setPalette(palette)

    def change_status(self):
        if self.isEnabled():
            self.setEnabled(False)
        else:
            self.setEnabled(True)
            palette = self.palette()
            linear = QLinearGradient(0, 0, self.width(), self.height())
            linear.setColorAt(0, QColor('Red'))
            linear.setColorAt(0.4, QColor('grey'))
            linear.setColorAt(1, QColor('white'))
            palette.setBrush(QPalette.Active, QPalette.Button, QBrush(linear))
            self.setPalette(palette)
