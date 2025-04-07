from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable

from ..widgets import LabeledText, LabeledColorBox, Column, Button
from ..Types import Padding
from ..core import DataTypes


def VectorListItem(vector: DataTypes.Vector, onUp: Callable[[str], None], onDown: Callable[[str], None], onDelete: Callable[[str], None]):
    # Create Widgets
    id = LabeledText.LabledText("id", str(vector.id), 2, 12, 12, fixedWith=100)
    iScaler = LabeledText.LabledText(
        "i scaler ", str(vector.iScaler), 2, 12, 12, fixedWith=150)
    jScaler = LabeledText.LabledText(
        "j scaler ", str(vector.jScaler), 2, 12, 12, fixedWith=150)
    name = LabeledText.LabledText(
        "name ", vector.name, 2, 12, 12, fixedWith=200)
    enabled = LabeledText.LabledText(
        "enabled ", str(vector.enabled), 2, 12, 12, fixedWith=150)
    thickness = LabeledText.LabledText(
        "thickness", str(vector.thickness), 2, 12, 12, fixedWith=150)
    color = LabeledColorBox.LabledColorBox(
        "color", vector.color, 2, 12, boxSize=25, fixedWidth=100)
    up = Button.Button(text="up", buttonColor="green", padding=Padding(5
                                                                       ), borderRadius="5px", buttonFontSize="15px", fontColor="white", fixedWidth=40, onPressed=(lambda: onUp(vector.id)) if (onUp) else None)
    down = Button.Button(text="down", buttonColor="green", padding=Padding(5
                                                                           ), borderRadius="5px", buttonFontSize="15px", fontColor="white", fixedWidth=60, onPressed=(lambda: onDown(vector.id)) if (onUp) else None)
    delete = Button.Button(text="delete", buttonColor="red", padding=Padding(5
                                                                             ), borderRadius="5px", buttonFontSize="15px", fontColor="white", fixedWidth=60, onPressed=(lambda: onDelete(vector.id)) if (onDelete) else None)

    listItem = Column.Column(spacing=0, alignment=Qt.AlignmentFlag.AlignCenter, setSpacers=True, subWidgets=[
                             id, name, iScaler, jScaler, enabled, thickness, color, up, down, delete])
    listItem.setStyleSheet(
        "background-color:#ffe;border-radius:15px;")
    return listItem
