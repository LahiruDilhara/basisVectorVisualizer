from typing import Callable
from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from .HorizontalStretchBox import HorizontalStretchBox


def LabeledCheckBox(text: str, checked: bool, onEnable: Callable[[bool], None] = None, fontSize: int = 11, setSpace: bool = True):
    def innerCheckHandler(state: Qt.CheckState):
        if (state == Qt.CheckState.Checked.value):
            onEnable(True)
        elif (state == Qt.CheckState.Unchecked.value):
            onEnable(False)
    inputLabel = QLabel(text)
    inputLabel.setFont(QFont("Arial", fontSize))  # 11
    inputLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    inputLabel.setStyleSheet(
        "padding: 5px; background-color: white; border-radius: 8px;")

    checkBox = QCheckBox()

    checkBox.setChecked(checked)

    if (onEnable):
        checkBox.stateChanged.connect(innerCheckHandler)

    return HorizontalStretchBox(setSpace=setSpace, subWidgets=[
        inputLabel,
        checkBox
    ])
