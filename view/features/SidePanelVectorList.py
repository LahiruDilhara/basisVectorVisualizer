from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..widgets import Row,  LabeledCheckBox


@dataclass
class VectorListItem():
    id: int
    name: str
    enabled: bool

    def getWidget() -> QFrame:

        pass


def SidePanelVectorList() -> QVBoxLayout:
    vectorList: list[VectorListItem] = [
        VectorListItem(0, "vector 1", True),
        VectorListItem(0, "vector 1", False),
        VectorListItem(0, "vector 1", True),
        VectorListItem(0, "vector 1", True),
        VectorListItem(0, "vector 1", False),
        VectorListItem(0, "vector 1", False),
        VectorListItem(0, "vector 1", False),
        VectorListItem(0, "vector 1", False),
        VectorListItem(0, "vector 1", False),
    ]

    return Row.Row(spacing=10, alignment=Qt.AlignmentFlag.AlignLeft, subWidgets=[Row.RowItem(item=LabeledCheckBox.LabeledCheckBox(text=vector.name, checked=vector.enabled), stretch=1) for vector in vectorList])
