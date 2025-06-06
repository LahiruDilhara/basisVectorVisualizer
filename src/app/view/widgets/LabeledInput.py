from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable
import matplotlib.pyplot as plt


class LabledInput(QFrame):

    def __init__(self, labelText: str, defaultValue: str, spacing: int, labelFontSize: int, inputFontSize: int, onChange: Callable[[str], None]):
        super().__init__()
        self.labelText = labelText
        self.defaultValue = defaultValue
        self.spacing = spacing
        self.labelFontSize = labelFontSize
        self.inputFontSize = inputFontSize
        self.onChange = onChange

        self.initUi()

    def initUi(self):
        self.setStyleSheet(
            "background-color: #ffffff; border-radius: 8px;")
        self.setContentsMargins(0, 0, 0, 0)

        # Create a layout for the input
        inputLayout = QHBoxLayout()
        inputLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        inputLayout.setSpacing(self.spacing)  # 10
        self.setLayout(inputLayout)

        # Create a label
        inputLabel = QLabel(self.labelText)
        inputLabel.setFont(QFont("Arial", self.labelFontSize))  # 11
        inputLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        inputLabel.setStyleSheet(
            "padding: 5px; background-color: white; border-radius: 8px;")
        # Create input fields
        self.input = QLineEdit()
        self.input.setStyleSheet(
            "padding: 5px; background-color: #f4f4f4; border-radius: 8px;")
        self.input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.input.setFont(QFont("Arial", self.inputFontSize))
        self.input.setText(self.defaultValue)

        # Connect the signals
        if (self.onChange):
            self.input.textChanged.connect(self.onChange)

        inputLayout.addWidget(inputLabel)
        inputLayout.addWidget(self.input)

    def resetInput(self):
        self.input.setText(self.defaultValue)

        # def LabledInput(labelText: str, defaultValue: str, spacing: int, labelFontSize: int, inputFontSize: int, onChange: Callable[[str], None]):
        #     frame = QFrame()
        #     frame.setStyleSheet(
        #         "background-color: #ffffff; border-radius: 8px;")
        #     frame.setContentsMargins(0, 0, 0, 0)

        #     # Create a layout for the input
        #     inputLayout = QHBoxLayout()
        #     inputLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #     inputLayout.setSpacing(spacing)  # 10
        #     frame.setLayout(inputLayout)

        #     # Create a label
        #     inputLabel = QLabel(labelText)
        #     inputLabel.setFont(QFont("Arial", labelFontSize))  # 11
        #     inputLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #     inputLabel.setStyleSheet(
        #         "padding: 5px; background-color: white; border-radius: 8px;")
        #     # Create input fields
        #     input = QLineEdit()
        #     input.setStyleSheet(
        #         "padding: 5px; background-color: #f4f4f4; border-radius: 8px;")
        #     input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #     input.setFont(QFont("Arial", inputFontSize))
        #     input.setText(defaultValue)

        #     # Connect the signals
        #     if (onChange):
        #         input.textChanged.connect(onChange)

        #     inputLayout.addWidget(inputLabel)
        #     inputLayout.addWidget(input)

        #     return frame
