from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt


def Column(spacing: int, subWidgets: list[QWidget], alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter, setSpacers: bool = False) -> QFrame:
    # Container
    container = QFrame()
    containerLayout = QHBoxLayout()
    container.setLayout(containerLayout)
    if not setSpacers:
        containerLayout.setSpacing(spacing)
    containerLayout.setAlignment(alignment)

    for index, widget in enumerate(subWidgets):
        containerLayout.addWidget(widget)
        if setSpacers and (index < len(subWidgets)-1):
            containerLayout.addStretch(1)

    return container
