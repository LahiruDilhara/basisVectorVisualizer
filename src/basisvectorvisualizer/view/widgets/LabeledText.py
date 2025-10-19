from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable
import matplotlib.pyplot as plt


def LabledText(labelText: str, text: str, spacing: int, labelFontSize: int, textFontSize: int, maxWidth: int = None, strechableText: bool = False):
    frame = QFrame()
    frame.setStyleSheet(
        "background-color: #ffffff; border-radius: 8px;")
    frame.setContentsMargins(0, 0, 0, 0)

    # Create a layout for the input
    textLayout = QHBoxLayout()
    textLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    textLayout.setSpacing(spacing)  # 10
    frame.setLayout(textLayout)

    # Create a label
    textLabel = QLabel(labelText)
    textLabel.setFont(QFont("Arial", labelFontSize))  # 11
    textLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
    textLabel.setStyleSheet(
        "padding: 5px; background-color: white; border-radius: 8px;")

    # Create text field
    text = QLabel(text)
    text.setStyleSheet(
        "padding: 5px; background-color: #f4f4f4; border-radius: 8px;")
    text.setAlignment(Qt.AlignmentFlag.AlignLeft)
    text.setFont(QFont("Arial", textFontSize))

    textLayout.addWidget(textLabel)
    textLayout.addWidget(text, 1 if strechableText else 0)

    if (maxWidth):
        frame.setMaximumWidth(maxWidth)

    return frame
