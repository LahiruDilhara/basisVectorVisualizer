from typing import Callable
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont, QColor, QCloseEvent
from dataclasses import dataclass


@dataclass
class ToolButtonSpec():
    text: str
    buttonColor: str = "#4CAF50"
    onPressed: Callable = None
    enabled: bool = True


class ToolButton(QPushButton):
    def __init__(self, toolButtonSpec: ToolButtonSpec):
        super().__init__()
        self.toolButtonSpec = toolButtonSpec

        self.initUI()

    def initUI(self):
        self.setText(self.toolButtonSpec.text)
        self.setButtonColor()

        if (self.toolButtonSpec.onPressed):
            self.clicked.connect(self.toolButtonSpec.onPressed)

    def setButtonColor(self):
        baseColor = QColor(self.toolButtonSpec.buttonColor)
        hoverColor = baseColor.lighter(110).name()
        pressedColor = baseColor.darker(110).name()

        self.setStyleSheet("""
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
        """.format(self.toolButtonSpec.buttonColor, hoverColor, pressedColor))


# def ToolButton(toolButtonSpec: ToolButtonSpec):
#     # Create a button for the sidebar
#     button = QPushButton(toolButtonSpec.text)

#     button.setStyleSheet("""
#             QPushButton {{
#                 background-color: {0};
#                 color: white;
#                 border: none;
#                 padding: 10px 20px;
#                 font-size: 16px;
#                 border-radius: 5px;
#             }}
#             QPushButton:hover {{
#                 background-color: {1};
#             }}
#             QPushButton:pressed {{
#                 background-color: {2};
#             }}
#         """.format(toolButtonSpec.buttonColor, toolButtonSpec.buttonHoverColor, toolButtonSpec.buttonPressedColor))

#     if (toolButtonSpec.onPressed):
#         button.clicked.connect(toolButtonSpec.onPressed)
#     return button
