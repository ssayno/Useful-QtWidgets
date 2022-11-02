#!/usr/bin/env python3

from PyQt5.QtWidgets import QLabel


class BasicLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
