from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def HorizontalLabeledCard(labelText: str, alignment: Qt.AlignmentFlag, backgroundColor: str, space: int, fontSize: int, subWidget: QWidget):

    # Create a frame for the vector input
    cardFrame = QFrame()
    cardFrame.setStyleSheet(
        f"background-color: {backgroundColor};border-radius: 8px;")
    cardFrame.setContentsMargins(0, 0, 0, 0)

    # Create a layout for the vector input
    cardLayout = QHBoxLayout()
    cardLayout.setAlignment(alignment)
    cardLayout.setSpacing(space)  # 10
    cardFrame.setLayout(cardLayout)

    # Create a label for the vector name
    vector_label = QLabel(labelText)
    vector_label.setFont(QFont("Arial", fontSize, weight=QFont.Bold))
    vector_label.setAlignment(alignment)
    vector_label.setStyleSheet(
        " border-radius: 8px;")

    cardLayout.addWidget(vector_label)
    cardLayout.addWidget(subWidget)

    return cardFrame
