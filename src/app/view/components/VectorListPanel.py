from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from typing import Callable

from ..features import VectorListItem
from ...core.DataTypes import Vector


class VectorListPanel(QFrame):

    def __init__(self, vectors: list[Vector], onUp: Callable[[str], None], onDown: Callable[[str], None], onDelete: Callable[[str], None]):
        super().__init__()

        self.onUp = onUp
        self.onDown = onDown
        self.onDelete = onDelete

        self.layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(20)
        self.setListItems(vectorList=vectors)

        self.setStyleSheet(
            "background-color:#efefef; border:none; border-radius:15px;")

    def setListItems(self, vectorList: list[Vector]):
        self.remove_all_widgets()
        for vector in vectorList:
            self.layout.addWidget(VectorListItem.VectorListItem(
                vector=vector, onUp=self.onUp, onDown=self.onDown, onDelete=self.onDelete))
        self.layout.addStretch(1)

    def remove_all_widgets(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.update()
        self.updateGeometry()
