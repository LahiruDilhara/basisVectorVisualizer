from typing import Callable
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont, QColor, QCloseEvent
from dataclasses import dataclass


@dataclass
class ToolButtonSpec():
    text: str
    buttonEnableColor: str = "#4CAF50"
    buttonDisableColor: str = "#66ff66"
    onPressed: Callable[[bool], None] = None
    enabled: bool = True


class ToolButton(QPushButton):
    def __init__(self, toolButtonSpec: ToolButtonSpec):
        super().__init__()
        self.toolButtonSpec = toolButtonSpec

        self.initUI()

    def initUI(self):
        self.setText(self.toolButtonSpec.text)
        self.setButtonColor()

        self.clicked.connect(self.onButtonPress)

    def onButtonPress(self):
        self.toolButtonSpec.enabled = not self.toolButtonSpec.enabled
        if self.toolButtonSpec.onPressed:
            self.toolButtonSpec.onPressed(self.toolButtonSpec.enabled)
        self.setButtonColor()

    def setButtonColor(self):
        color = self.toolButtonSpec.buttonEnableColor if (
            self.toolButtonSpec.enabled) else self.toolButtonSpec.buttonDisableColor
        baseColor = QColor(color)
        hoverColor = baseColor.lighter(110).name()
        pressedColor = baseColor.darker(110).name()

        self.setStyleSheet("""
            QPushButton {{
                background-color: {0};
                color: white;
                border: none;
                padding: 6px 12px;
                font-size: 12px;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: {1};
            }}
            QPushButton:pressed {{
                background-color: {2};
            }}
        """.format(color, hoverColor, pressedColor))
