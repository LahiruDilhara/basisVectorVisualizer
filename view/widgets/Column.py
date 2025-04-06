from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt


def Column(spacing: int, subWidgets: list[QWidget], alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter) -> QFrame:
    # Container
    container = QFrame()
    containerLayout = QHBoxLayout()
    container.setLayout(containerLayout)
    containerLayout.setSpacing(spacing)
    containerLayout.setAlignment(alignment)

    for i in subWidgets:
        containerLayout.addWidget(i)

    return container

    pass
