from typing import Callable
from PySide6.QtWidgets import QPushButton, QColorDialog
from PySide6.QtGui import QFont, QColor, QCloseEvent


class ToolColorButton(QPushButton):
    def __init__(self, defaultColor: str = "#4CAF50", onPressed: Callable[[str], None] = None):
        super().__init__()
        self.defaultColor = defaultColor
        self.onPressed = onPressed

        self.initUI()

    def initUI(self):
        self.setText(self.defaultColor)
        self.setButtonColor(QColor(self.defaultColor))

        self.clicked.connect(self.onButtonPress)

    def onButtonPress(self):
        color = QColorDialog.getColor()
        self.setButtonColor(color)
        self.setText(color.name())
        if (self.onPressed):
            self.onPressed(color.name())

    def setButtonColor(self, baseColor: QColor):
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
        """.format(baseColor.name(), hoverColor, pressedColor))
