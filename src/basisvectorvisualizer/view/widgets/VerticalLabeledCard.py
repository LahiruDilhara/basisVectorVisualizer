from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def VerticalLabeledCard(labelText: str, alignment: Qt.AlignmentFlag, backgroundColor: str, space: int, fontSize: int, subWidget: QWidget):

    # Create card
    card = QFrame()
    card.setStyleSheet(
        f"background-color: {backgroundColor};border-radius: 8px;")  # f4f4f4
    card.setContentsMargins(0, 0, 0, 0)

    # Create card layout
    card_layout = QVBoxLayout()
    card_layout.setSpacing(space)
    card_layout.setAlignment(alignment)
    card.setLayout(card_layout)

    # Create title label
    title_label = QLabel(labelText)
    title_label.setFont(QFont("Arial", fontSize, weight=QFont.Bold))
    title_label.setAlignment(alignment)
    title_label.setWordWrap(True)

    # Add The widgets to the card
    card_layout.addWidget(title_label)
    card_layout.addWidget(subWidget)

    card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    return card
