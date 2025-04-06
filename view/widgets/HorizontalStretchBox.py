from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def HorizontalStretchBox(subWidgets: list[QWidget]):
    frame = QFrame()
    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    for index, widget in enumerate(subWidgets):
        frameLayout.addWidget(widget)
        if index < len(subWidgets) - 1:
            frameLayout.addStretch(1)
    return frame
