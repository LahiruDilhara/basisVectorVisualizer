from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QGridLayout, QColorDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QCloseEvent
from dataclasses import dataclass
from typing import Callable

from ..widgets import LabeledInput, LabeledCheckBox, LabeledButton


@dataclass
class VectorPanelSpec():
    onVectorNameChange: Callable[[str], None] = None
    onIScallerChange: Callable[[str], None] = None
    onJScallerChange: Callable[[str], None] = None
    onVectorThiknesChange: Callable[[str], None] = None
    onVectorColorChange: Callable[[str], None] = None
    onEnableInputChange: Callable[[bool], None] = None


class NewVectorPanel(QFrame):

    def __init__(self, vectorPanelSpec: VectorPanelSpec):
        super().__init__()

        self.vectorPanelSpec = vectorPanelSpec

        self.vectorNameInput = LabeledInput.LabledInput(
            "vector name :", "0", 10, 12, 12, vectorPanelSpec.onVectorNameChange)
        self.iScalerInput = LabeledInput.LabledInput(
            "i scaler :", "0", 10, 12, 12, vectorPanelSpec.onIScallerChange)
        self.jScalerInput = LabeledInput.LabledInput(
            "j scaler :", "0", 10, 12, 12, vectorPanelSpec.onJScallerChange)
        self.vectorEnabledInput = LabeledCheckBox.LabeledCheckBox(
            "vector enabled : ", True, vectorPanelSpec.onEnableInputChange, setSpace=False)
        self.vectorThikness = LabeledInput.LabledInput(
            "thickness :", "0", 10, 12, 12, vectorPanelSpec.onVectorThiknesChange)
        self.colorPickerButton = LabeledButton.LabeledButton(
            "choose color :", "selected color", 10, 12, self.onPress, buttonColor="#4CAF50")

        self.layout: QGridLayout = QGridLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(self.iScalerInput, 0, 0)
        self.layout.addWidget(self.jScalerInput, 0, 1)
        self.layout.addWidget(self.vectorNameInput, 0, 2)
        self.layout.addWidget(self.vectorEnabledInput, 1, 0)
        self.layout.addWidget(self.vectorThikness, 1, 1)
        self.layout.addWidget(self.colorPickerButton, 1, 2,
                              Qt.AlignmentFlag.AlignCenter)

    def onPress(self):
        color = QColorDialog.getColor()
        selectedColor = color.name()
        self.colorPickerButton.setButtonColor(selectedColor)
        if self.vectorPanelSpec.onVectorColorChange:
            self.vectorPanelSpec.onVectorColorChange(selectedColor)
