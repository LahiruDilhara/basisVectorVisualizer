from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def HorizontalStretchBox(subWidgets: list[QWidget], setSpace: bool = True):
    frame = QFrame()
    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    frame.setStyleSheet(
        "background-color: #ffffff; border-radius: 8px;")
    for index, widget in enumerate(subWidgets):
        frameLayout.addWidget(widget)
        if (index < len(subWidgets) - 1) and setSpace:
            frameLayout.addStretch(1)
    return frame
