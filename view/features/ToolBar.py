from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..widgets import ToolButton, Column, SpaceCard


def ToolBar(spacing: int, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter, toolButtons: list[QPushButton] = []):
    subWidgets = []

    for i in toolButtons:
        subWidgets.append(i)

    card = SpaceCard.SpaceCard(subWidget=Column.Column(
        spacing=spacing, alignment=alignment, subWidgets=subWidgets))
    return card
