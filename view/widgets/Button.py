from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont, QColor
from typing import Callable

from ..Types import Padding


def Button(text: str, buttonColor: str, onPressed: Callable, padding: Padding, buttonFontSize: str = "10px", borderRadius: str = "5px", fontColor: str = "white", fixedWidth: int = None) -> QPushButton:
    # Create a button for the sidebar
    button = QPushButton(text)
    baseColor = QColor(buttonColor)
    hoverColor = baseColor.lighter(120).name()
    pressedColor = baseColor.darker(120).name()

    button.setStyleSheet("""
            QPushButton {{
                background-color: {0};
                color: {1};
                border: none;
                padding: {2};
                font-size: {3};
                border-radius: {4};
            }}
            QPushButton:hover {{
                background-color: {5};
            }}
            QPushButton:pressed {{
                background-color: {6};
            }}
        """.format(buttonColor, fontColor, padding.getPadding(), buttonFontSize, borderRadius, hoverColor, pressedColor))

    if (onPressed):
        button.clicked.connect(onPressed)

    if (fixedWidth):
        button.setFixedWidth(fixedWidth)
    return button
