from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtCore import Qt
from dataclasses import dataclass


@dataclass
class RowItem():
    item: QWidget
    stretch: int = 0


def Row(spacing: int, subWidgets: list[RowItem], alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter) -> QFrame:
    # Container
    container = QFrame()
    containerLayout = QVBoxLayout()
    container.setLayout(containerLayout)
    containerLayout.setAlignment(alignment)
    containerLayout.setSpacing(spacing)

    for item in subWidgets:
        containerLayout.addWidget(item.item, item.stretch)
    
    container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    return container
