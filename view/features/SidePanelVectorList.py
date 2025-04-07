from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..widgets import Row,  LabeledCheckBox
from ..core.DataTypes import Vector
from typing import Callable
from functools import partial


def SidePanelVectorList(vectorList: list[Vector], onToggle: Callable[[Vector, bool], None] = None) -> QVBoxLayout:
    return Row.Row(
        spacing=10,
        alignment=Qt.AlignmentFlag.AlignLeft,
        subWidgets=[Row.RowItem(
            item=LabeledCheckBox.LabeledCheckBox(
                text=vector.name,
                checked=vector.enabled,
                onEnable=partial(onToggle, vector) if onToggle else None
            ),
            stretch=1
        ) for vector in vectorList]
    )
