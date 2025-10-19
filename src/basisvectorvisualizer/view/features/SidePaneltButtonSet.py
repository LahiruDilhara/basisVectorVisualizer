from typing import Callable
from dataclasses import dataclass
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QFrame, QSizePolicy
from PySide6.QtCore import Qt
from ..widgets.sidePanelButton import SidePanelButton


@dataclass
class SidePanelButtonSpec():
    text: str
    buttonColor: str = "#4CAF50"
    buttonHoverColor: str = "#45a049"
    buttonPressedColor: str = "#3e8e41"
    onPressed: Callable = None

    def build(self) -> QPushButton:
        return SidePanelButton(text=self.text, buttonColor=self.buttonColor, buttonHoverColor=self.buttonHoverColor,
                               buttonPressedColor=self.buttonPressedColor, onPressed=self.onPressed)


def SidePanelButtonSet(buttonList: list[SidePanelButtonSpec], spacing: int = 10):

    # Create a frame for the buttons
    button_frame = QFrame()

    # Create a layout for the button frame
    button_layout = QVBoxLayout()
    button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    button_layout.setSpacing(spacing)
    button_frame.setLayout(button_layout)

    # Create buttons
    for button in buttonList:
        button_layout.addWidget(button.build())

    button_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    return button_frame
