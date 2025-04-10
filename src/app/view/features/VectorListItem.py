from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QIcon
from typing import Callable

from ..widgets import LabeledText, LabeledColorBox, Column, Button
from ..Types import Padding
from ...core import DataTypes


def VectorListItem(vector: DataTypes.Vector, onUp: Callable[[str], None], onDown: Callable[[str], None], onDelete: Callable[[str], None]):
    # Create Widgets
    id = LabeledText.LabledText(
        "id", str(vector.id), 2, 12, 12, fixedWith=100, strechableText=True)
    iScaler = LabeledText.LabledText(
        "i scaler ", str(vector.iScaler), 2, 12, 12, fixedWith=150, strechableText=True)
    jScaler = LabeledText.LabledText(
        "j scaler ", str(vector.jScaler), 2, 12, 12, fixedWith=150, strechableText=True)
    name = LabeledText.LabledText(
        "name ", vector.name, 2, 12, 12, fixedWith=200, strechableText=True)
    enabled = LabeledText.LabledText(
        "enabled ", str(vector.enabled), 2, 12, 12, fixedWith=150, strechableText=True)
    thickness = LabeledText.LabledText(
        "thickness", str(vector.thickness), 2, 12, 12, fixedWith=150, strechableText=True)
    color = LabeledColorBox.LabledColorBox(
        "color", vector.color, 2, 12, boxSize=25, fixedWidth=100, strechable=True)
    up = Button.Button(icon=QIcon("assets/icons/icons8-expand-arrow_up-100.png"), buttonColor="#33ff33", padding=Padding(7
                                                                                                                         ), borderRadius="5px", buttonFontSize="15px", fontColor="white", fixedWidth=28, onPressed=(lambda: onUp(vector.id)) if (onUp) else None)
    down = Button.Button(icon=QIcon("assets/icons/icons8-expand-arrow-100.png", color="white"), buttonColor="#33ff33", padding=Padding(7
                                                                                                                                       ), borderRadius="5px", buttonFontSize="15px", fontColor="white", fixedWidth=28, onPressed=(lambda: onDown(vector.id)) if (onUp) else None)
    delete = Button.Button(icon=QIcon("assets/icons/icons8-delete-120.png"), buttonColor="#ff3333", padding=Padding(7
                                                                                                                    ), borderRadius="5px", buttonFontSize="15px", fontColor="white", fixedWidth=28, onPressed=(lambda: onDelete(vector.id)) if (onDelete) else None)

    listItem = Column.Column(spacing=0, addEndSpacer=True, addStartSpacer=True, setSpacers=True, alignment=Qt.AlignmentFlag.AlignCenter, subWidgets=[
                             id, name, iScaler, jScaler, enabled, thickness, color, up, down, delete])
    listItem.setStyleSheet(
        "background-color:#ffe;border-radius:15px;")
    return listItem
