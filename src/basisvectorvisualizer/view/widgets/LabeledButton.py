from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable


class LabeledButton(QFrame):
    def __init__(self, labelText: str, buttonText: str, spacing: int, labelFontSize: int, onPress: Callable[[], None], buttonColor: str = "#4CAF50", infiniteSpace: bool = False, buttonStrech: bool = False):
        super().__init__()
        self.lableText = labelText
        self.spacing = spacing
        self.labelFontSize = labelFontSize
        self.onPress = onPress
        self.buttonText = buttonText
        self.buttonColor = buttonColor
        self.infiniteSpace = infiniteSpace
        self.buttonStretch = buttonStrech

        self.setStyleSheet("background-color: #fff; border-radius: 8px;")
        self.setContentsMargins(0, 0, 0, 0)
        self.init_ui()

    def init_ui(self):
        # Create a layout for the button
        buttonCtonainerLayout = QHBoxLayout()
        buttonCtonainerLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if not self.infiniteSpace:
            buttonCtonainerLayout.setSpacing(self.spacing)  # 10
        self.setLayout(buttonCtonainerLayout)

        # Create a label
        buttonLabel = QLabel(self.lableText)
        buttonLabel.setFont(QFont("Arial", self.labelFontSize))  # 11
        # buttonLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttonLabel.setStyleSheet(
            "padding: 5px; background-color: white; border-radius: 8px;")

        # Create button
        self.button = QPushButton(self.buttonText)
        self.setButtonColor(self.buttonColor)

        # Connect the signals
        if self.onPress:
            self.button.pressed.connect(self.onPress)

        buttonCtonainerLayout.addWidget(buttonLabel)
        if (self.infiniteSpace and not self.buttonStretch):
            buttonCtonainerLayout.addStretch(1)
        if self.buttonStretch:
            buttonCtonainerLayout.addWidget(self.button, 1)
        else:
            buttonCtonainerLayout.addWidget(self.button)

    def setButtonColor(self, color: str):
        baseColor = QColor(color)

        hover_color = baseColor.lighter(120)
        pressed_color = baseColor.darker(120)
        button_styles = f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                }}
                QPushButton:hover {{
                    background-color: {hover_color.name()};
                }}
                QPushButton:pressed {{
                    background-color: {pressed_color.name()};
                }}
            """
        self.button.setStyleSheet(button_styles)

    def setButtonName(self, name: str):
        self.button.setText(name)
