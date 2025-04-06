from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from typing import Callable

from ..widgets import LabeledText, LabeledColorBox, Column, Button
from ..Types import Padding
from ..core import DataTypes


def VectorListItem(vector: DataTypes.Vector, onUp: Callable[[str], None], onDown: Callable[[str], None], onDelete: Callable[[str], None]):
    # Create Widgets
    idText = LabeledText.LabledText("id", vector.id, 10, 12, 12)
    iScaler = LabeledText.LabledText(
        "i scaler ", str(vector.iScaler), 10, 12, 12)
    jScaler = LabeledText.LabledText(
        "j scaler ", str(vector.jScaler), 10, 12, 12)
    name = LabeledText.LabledText("name ", vector.name, 10, 12, 12)
    enabled = LabeledText.LabledText(
        "enabled ", str(vector.enabled), 10, 12, 12)
    thickness = LabeledText.LabledText(
        "thickness", str(vector.thickness), 10, 12, 12)
    color = LabeledColorBox.LabledColorBox(
        "color", vector.color, 10, 12, boxSize=25)
    up = Button.Button(text="up", buttonColor="green", padding=Padding(5
                                                                       ), borderRadius="5px", buttonFontSize="15px", fontColor="white", onPressed=(lambda: onUp(vector.id)) if (onUp) else None)
    down = Button.Button(text="down", buttonColor="green", padding=Padding(5
                                                                           ), borderRadius="5px", buttonFontSize="15px", fontColor="white", onPressed=(lambda: onDown(vector.id)) if (onUp) else None)
    delete = Button.Button(text="delete", buttonColor="red", padding=Padding(5
                                                                             ), borderRadius="5px", buttonFontSize="15px", fontColor="white", onPressed=(lambda: onDelete(vector.id)) if (onDelete) else None)

    listItem = Column.Column(spacing=15, alignment=Qt.AlignmentFlag.AlignCenter, subWidgets=[
                             idText, name, iScaler, jScaler, enabled, thickness, color, up, down, delete])
    listItem.setStyleSheet(
        "background-color:#ffe;border-radius:15px;")
    return listItem
