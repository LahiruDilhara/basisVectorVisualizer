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
        self.layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(self.layout)
        self.setContentsMargins(0, 0, 0, 0)

        self.initUI()

    def initUI(self):
        widget = Row.Row(
            spacing=10,
            alignment=Qt.AlignmentFlag.AlignLeft,
            subWidgets=[Row.RowItem(
                item=LabeledCheckBox.LabeledCheckBox(
                    text=vector.name,
                    checked=vector.enabled,
                    onEnable=partial(
                        self.onToggle, vector) if self.onToggle else None
                ),
                stretch=1
            ) for vector in self.vectorList]
        )

        self.layout.addWidget(widget)
