from PySide6.QtWidgets import QPushButton
from typing import Callable


def SidePanelButton(text: str, buttonColor: str, buttonHoverColor: str, buttonPressedColor: str, onPressed: Callable) -> QPushButton:
    # Create a button for the sidebar
    button = QPushButton(text)

    button.setStyleSheet("""
            QPushButton {{
                background-color: {0};
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: {1};
            }}
            QPushButton:pressed {{
                background-color: {2};
            }}
        """.format(buttonColor, buttonHoverColor, buttonPressedColor))

    if (onPressed):
        button.clicked.connect(onPressed)
    return button
