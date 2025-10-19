from typing import Callable
from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


class LabeledCheckBox(QFrame):
    def __init__(self, text: str, checked: bool, onEnable: Callable[[bool], None] = None, fontSize: int = 11, setSpace: bool = True, subWidgets: list[QWidget] = []):
        super().__init__()
        self.text = text
        self.checked = checked
        self.onEnabled = onEnable
        self.fontSize = fontSize
        self.setSpace = setSpace
        self.layout: QHBoxLayout = QHBoxLayout()
        self.subWidgets = subWidgets

        self.setLayout(self.layout)

        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            "background-color: #ffffff; border-radius: 8px;")
        inputLabel = QLabel(self.text)
        inputLabel.setFont(QFont("Arial", self.fontSize))  # 11
        inputLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        inputLabel.setStyleSheet(
            "padding: 5px; background-color: white; border-radius: 8px;")

        checkBox = QCheckBox()

        checkBox.setChecked(self.checked)

        if (self.onEnabled):
            checkBox.stateChanged.connect(self.CheckHandler)

        self.layout.addWidget(inputLabel)
        self.layout.addStretch(1)
        for widget in self.subWidgets:
            self.layout.addWidget(widget)
            self.layout.addStretch(1)
        self.layout.addWidget(checkBox)

    def CheckHandler(self, state: Qt.CheckState):
        if (state == Qt.CheckState.Checked.value):
            self.onEnabled(True)
        elif (state == Qt.CheckState.Unchecked.value):
            self.onEnabled(False)
