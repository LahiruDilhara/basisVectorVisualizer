from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable
import matplotlib.pyplot as plt


def LabledInput(labelText: str, defaultValue: str, spacing: int, labelFontSize: int, inputFontSize: int, onChange: Callable[[str], None]):
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
    inputLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
    inputLabel.setStyleSheet(
        "padding: 5px; background-color: white; border-radius: 8px;")
    # Create input fields
    input = QLineEdit()
    input.setStyleSheet(
        "padding: 5px; background-color: #f4f4f4; border-radius: 8px;")
    input.setAlignment(Qt.AlignmentFlag.AlignLeft)
    input.setFont(QFont("Arial", inputFontSize))
    input.setText(defaultValue)

    # Connect the signals
    if (onChange):
        input.textChanged.connect(onChange)

    inputLayout.addWidget(inputLabel)
    inputLayout.addWidget(input)

    return frame
