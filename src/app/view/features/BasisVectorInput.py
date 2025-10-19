from ..widgets import HorizontalLabeledCard, LabeledInput, sidePanelButton, VerticalLabeledCard, Column, Row
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from dataclasses import dataclass
from PySide6.QtCore import Qt
from typing import Callable


@dataclass
class BasisVectorInputSpec():
    ixOnChange: Callable[[str], None] = None
    iyOnChange: Callable[[str], None] = None
    jxOnChange: Callable[[str], None] = None
    jyOnChange: Callable[[str], None] = None
    defaultIx: float = 0.0
    defaultIy: float = 0.0
    defaultJx: float = 0.0
    defaultJy: float = 0.0

    pass


def BasisVectorInput(basisVectorInputSpec: BasisVectorInputSpec) -> QFrame:
    # Create the Inputs
    ixInput = LabeledInput.LabledInput(
        labelText="x :", defaultValue=str(basisVectorInputSpec.defaultIx), labelFontSize=9, spacing=6, inputFontSize=9, onChange=basisVectorInputSpec.ixOnChange)
    iyInput = LabeledInput.LabledInput(
        labelText="y :", defaultValue=str(basisVectorInputSpec.defaultIy), labelFontSize=9, spacing=6, inputFontSize=9, onChange=basisVectorInputSpec.iyOnChange)
    jxInput = LabeledInput.LabledInput(
        labelText="x :", defaultValue=str(basisVectorInputSpec.defaultJx), labelFontSize=9, spacing=6, inputFontSize=9, onChange=basisVectorInputSpec.jxOnChange)
    jyInput = LabeledInput.LabledInput(
        labelText="y :", defaultValue=str(basisVectorInputSpec.defaultJy), labelFontSize=9, spacing=6, inputFontSize=9, onChange=basisVectorInputSpec.jyOnChange)

    # Create Input Container

    inputContainer1 = HorizontalLabeledCard.HorizontalLabeledCard(
        "i", Qt.AlignmentFlag.AlignCenter, backgroundColor="#f4f4f4", space=2, fontSize=12, subWidget=Column.Column(spacing=6, subWidgets=[ixInput, iyInput]))

    inputContainer2 = HorizontalLabeledCard.HorizontalLabeledCard(
        "j", Qt.AlignmentFlag.AlignCenter, backgroundColor="#f4f4f4", space=2, fontSize=12, subWidget=Column.Column(spacing=6, subWidgets=[jxInput, jyInput]))

    return VerticalLabeledCard.VerticalLabeledCard(
        labelText="Basis Vector", alignment=Qt.AlignmentFlag.AlignLeft, backgroundColor="#f4f4f4", fontSize=10, space=6, subWidget=Row.Row(spacing=6, alignment=Qt.AlignmentFlag.AlignTop, subWidgets=[Row.RowItem(inputContainer1), Row.RowItem(inputContainer2)]))
