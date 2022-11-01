#!/usr/bin/env python3
from PyQt5.QtCore import QPropertyAnimation, QTimer, Qt
from PyQt5.QtWidgets import QProgressBar, QStyleFactory


class OwnProgressbar(QProgressBar):
    def __init__(self, parent) -> None:
        super(OwnProgressbar, self).__init__(parent=parent)
        # for Mac, you should add this to show percentage
        self.setStyle(QStyleFactory.create('Fusion'))
        self.setAlignment(Qt.AlignCenter)
        self.setFormat('Loading... %p%')
        self.setMinimum(0)
        self.setMaximum(100)
        # create animation
        self.create_panimation()
        # set a status
        self.allow_next = True
        self.setOrientation(Qt.Horizontal)
        # self.setOrientation(Qt.Vertical)
        self.valueChanged.connect(self.value_change)

    def setValue(self, value: int) -> None:
        self.old_value = self.value()
        return super().setValue(value)

    def set_value(self):
        if self.allow_next:
            self.old_value = -1
            self.allow_next = False
            for i in range(101):
                QTimer.singleShot(20 * i, lambda x=i: self.test(x))

    def test(self, x):
        self.setValue(x)

    def value_change(self, _value):
        #if self.isMaximized(): isMaximized not useful
        if _value == self.maximum():
            self.allow_next = True
        else:
            self._animation.start()

    def create_panimation(self):
        if not hasattr(self, "old_value"):
            self.old_value = self.value()
        self._animation = QPropertyAnimation(self, b'value', self.parent())
        self._animation.setStartValue(self.value())
        self._animation.setEndValue(self.old_value)
