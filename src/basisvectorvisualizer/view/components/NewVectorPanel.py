from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QGridLayout, QColorDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QCloseEvent
from dataclasses import dataclass
from typing import Callable

from ..widgets import LabeledInput, LabeledCheckBox, LabeledButton


@dataclass
class VectorPanelSpec():
    onVectorNameChange: Callable[[str], None] = None
    onIScallerChange: Callable[[float], None] = None
    onJScallerChange: Callable[[float], None] = None
    onVectorThiknesChange: Callable[[int], None] = None
    onVectorColorChange: Callable[[str], None] = None
    onEnableInputChange: Callable[[bool], None] = None
    defaultName: str = ""
    defaultIScaler: int = 0
    defaultJScaler: int = 0
    defaultEnabled: bool = True
    defaultThickness: int = 1
    defaultColor: str = "#4CAF50"


class NewVectorPanel(QFrame):

    def __init__(self, vectorPanelSpec: VectorPanelSpec):
        super().__init__()

        self.vectorPanelSpec = vectorPanelSpec

        self.vectorNameInput = LabeledInput.LabledInput(
            "vector name :", vectorPanelSpec.defaultName, 10, 10, 10, vectorPanelSpec.onVectorNameChange)
        self.iScalerInput = LabeledInput.LabledInput(
            "i scaler :", str(vectorPanelSpec.defaultIScaler), 10, 10, 10, lambda text: (vectorPanelSpec.onIScallerChange(float(text)) if (self.isFloat(text)) else None))
        self.jScalerInput = LabeledInput.LabledInput(
            "j scaler :", str(vectorPanelSpec.defaultJScaler), 10, 10, 10, lambda text: (vectorPanelSpec.onJScallerChange(float(text)) if (self.isFloat(text)) else None))
        self.vectorEnabledInput = LabeledCheckBox.LabeledCheckBox(
            "vector enabled : ", vectorPanelSpec.defaultEnabled, vectorPanelSpec.onEnableInputChange, setSpace=True)
        self.vectorThikness = LabeledInput.LabledInput(
            "thickness :", str(vectorPanelSpec.defaultThickness), 10, 10, 10, lambda text: (vectorPanelSpec.onVectorThiknesChange(int(text)) if (str.isdigit(text)) else None))
        self.colorPickerButton = LabeledButton.LabeledButton(
            "choose color :", self.vectorPanelSpec.defaultColor, 10, 10, self.onPress, buttonColor=vectorPanelSpec.defaultColor, buttonStrech=True)

        self.layout: QGridLayout = QGridLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(self.iScalerInput, 0, 0)
        self.layout.addWidget(self.jScalerInput, 0, 1)
        self.layout.addWidget(self.vectorNameInput, 0, 2)
        self.layout.addWidget(self.vectorEnabledInput, 1, 0)
        self.layout.addWidget(self.vectorThikness, 1, 1)
        self.layout.addWidget(self.colorPickerButton, 1, 2)

    def onPress(self):
        color = QColorDialog.getColor()
        selectedColor = color.name()
        self.colorPickerButton.setButtonColor(selectedColor)
        self.colorPickerButton.setButtonName(selectedColor)
        if self.vectorPanelSpec.onVectorColorChange:
            self.vectorPanelSpec.onVectorColorChange(selectedColor)

    def reset(self):
        self.vectorNameInput.resetInput()
        self.iScalerInput.resetInput()
        self.jScalerInput.resetInput()
        self.vectorThikness.resetInput()

    def isFloat(self,value: str) -> bool:
        try:
            float(value)
            return True
        except:
            return False
