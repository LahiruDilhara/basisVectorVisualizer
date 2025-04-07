from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable
import matplotlib.pyplot as plt


def LabledColorBox(labelText: str, color: str, spacing: int, labelFontSize: int, boxSize: int, fixedWidth: int = None, strechable: bool = False):
    frame = QFrame()
    frame.setStyleSheet(
        "background-color: #ffffff; border-radius: 8px;")
    frame.setContentsMargins(0, 0, 0, 0)

    # Create a layout for the input
    inputLayout = QHBoxLayout()
    inputLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    inputLayout.setSpacing(spacing)  # 10
    frame.setLayout(inputLayout)

    # Create a label
    inputLabel = QLabel(labelText)
    inputLabel.setFont(QFont("Arial", labelFontSize))  # 11
    inputLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    inputLabel.setStyleSheet(
        "padding: 5px; background-color: white; border-radius: 8px;")

    # Create text field
    box = QWidget()
    box.setFixedSize(boxSize, boxSize)
    box.setStyleSheet(
        f"padding: 5px; background-color: {color}; border-radius: 8px;")

    inputLayout.addWidget(inputLabel)
    inputLayout.addWidget(box, 1 if (strechable) else 0)

    if fixedWidth:
        frame.setFixedWidth(fixedWidth)

    return frame
