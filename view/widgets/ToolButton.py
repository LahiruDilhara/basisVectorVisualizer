from typing import Callable
from PySide6.QtWidgets import QPushButton
from dataclasses import dataclass


@dataclass
class ToolButtonSpec():
    text: str
    buttonColor: str = "#4CAF50"
    buttonHoverColor: str = "#45a049"
    buttonPressedColor: str = "#3e8e41"
    onPressed: Callable = None


def ToolButton(toolButtonSpec: ToolButtonSpec):
    # Create a button for the sidebar
    button = QPushButton(toolButtonSpec.text)

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
        """.format(toolButtonSpec.buttonColor, toolButtonSpec.buttonHoverColor, toolButtonSpec.buttonPressedColor))

    if (toolButtonSpec.onPressed):
        button.clicked.connect(toolButtonSpec.onPressed)
    return button
