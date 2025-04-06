from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable


class LabeledButton(QFrame):
    def __init__(self, labelText: str, buttonText: str, spacing: int, labelFontSize: int, onPress: Callable[[], None], buttonColor: str = "#4CAF50"):
        super().__init__()
        self.lableText = labelText
        self.spacing = spacing
        self.labelFontSize = labelFontSize
        self.onPress = onPress
        self.buttonText = buttonText
        self.buttonColor = buttonColor

        self.setStyleSheet("background-color: #ffffff; border-radius: 8px;")
        self.setContentsMargins(0, 0, 0, 0)
        self.init_ui()

    def init_ui(self):
        # Create a layout for the button
        buttonCtonainerLayout = QHBoxLayout()
        buttonCtonainerLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttonCtonainerLayout.setSpacing(self.spacing)  # 10
        self.setLayout(buttonCtonainerLayout)

        # Create a label
        buttonLabel = QLabel(self.lableText)
        buttonLabel.setFont(QFont("Arial", self.labelFontSize))  # 11
        buttonLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttonLabel.setStyleSheet(
            "padding: 5px; background-color: white; border-radius: 8px;")

        # Create button
        self.button = QPushButton(self.buttonText)
        self.setButtonColor(self.buttonColor)

        # Connect the signals
        if self.onPress:
            self.button.pressed.connect(self.onPress)

        buttonCtonainerLayout.addWidget(buttonLabel)
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

# def LabeledButton(labelText: str, spacing: int, labelFontSize: int,  onPress: Callable[[], None], buttonColor: str = "#4CAF50"):
#     frame = QFrame()
#     frame.setStyleSheet(
#         "background-color: #ffffff; border-radius: 8px;")
#     frame.setContentsMargins(0, 0, 0, 0)

#     # Create a layout for the button
#     buttonCtonainerLayout = QHBoxLayout()
#     buttonCtonainerLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
#     buttonCtonainerLayout.setSpacing(spacing)  # 10
#     frame.setLayout(buttonCtonainerLayout)

#     # Create a label
#     buttonLabel = QLabel(labelText)
#     buttonLabel.setFont(QFont("Arial", labelFontSize))  # 11
#     buttonLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
#     buttonLabel.setStyleSheet(
#         "padding: 5px; background-color: white; border-radius: 8px;")

#     # Create button
#     button = QPushButton("select color")
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
#                 background-color: #45a049;
#             }}
#             QPushButton:pressed {{
#                 background-color: #3e8e41;
#             }}
#         """.format(buttonColor))

#     # Connect the signals
#     if (onPress):
#         button.pressed.connect(onPress)

#     buttonCtonainerLayout.addWidget(buttonLabel)
#     buttonCtonainerLayout.addWidget(button)

#     return frame
