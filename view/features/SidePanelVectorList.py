from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..widgets import Row,  LabeledCheckBox
from ..core.DataTypes import Vector
from typing import Callable
from functools import partial


class SidePanelVectorList(QWidget):
    def __init__(self, vectorList: list[Vector], onToggle: Callable[[Vector, bool], None] = None):
        super().__init__()
        self.vectorList = vectorList
        self.onToggle = onToggle
        self.layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)

        self.initUI()

    def initUI(self):
        self.setVectorList(self.vectorList)

    def setVectorList(self, vectorList: list[Vector]):
        self.removeListItems()
        subWidgets = [LabeledCheckBox.LabeledCheckBox(text=vector.name, checked=vector.enabled, onEnable=partial(
            self.onToggle, vector) if self.onToggle else None) for vector in vectorList]
        for widget in subWidgets:
            self.layout.addWidget(widget)
        self.layout.addStretch(1)

    def removeListItems(self):
        self.layout.count()
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.update()
        self.updateGeometry()
