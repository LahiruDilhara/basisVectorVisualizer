from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from dataclasses import dataclass
from ..Types import Margin, Padding


def SpaceCard(subWidget: QWidget, margin: Margin = Margin(0), padding: Padding = Padding(0), height: int = None, width: int = None):
    frame = QFrame()
    frame.setContentsMargins(*margin.getMargin())
    frame.setStyleSheet(
        f"padding: {padding.getPadding()}; background-color: white; border-radius: 8px;")
    layout = QVBoxLayout()
    frame.setLayout(layout)

    layout.addWidget(subWidget)

    if height:
        frame.setFixedHeight(height)
    if width:
        frame.setFixedWidth(width)

    return frame
