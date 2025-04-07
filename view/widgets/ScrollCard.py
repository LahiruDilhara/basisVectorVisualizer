from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def ScrollCard(subWidget: QWidget, resizable: bool = False, verticalScrolling: bool = True, horizontalScrolling: bool = True):

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(resizable)
    scroll_area.setWidget(subWidget)

    if verticalScrolling:
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    else:
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    if horizontalScrolling:
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    else:
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    scroll_area.setStyleSheet("""
    QScrollArea {
        border: none;
        background: #ffffff;
        border-radius: 10px;
    }

    /* Vertical ScrollBar */
    QScrollBar:vertical, QScrollBar:horizontal {
        background: #f4f4f4;
        width: 8px;
        height: 8px;
        border-radius: 4px;
    }

    /* Handle (Thumb) */
    QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
        background: #BBB;
        min-height: 20px;
        min-width: 20px;
        border-radius: 4px;
    }

    /* Hover State */
    QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
        background: #777;
    }

    /* Pressed State */
    QScrollBar::handle:vertical:pressed, QScrollBar::handle:horizontal:pressed {
        background: #999;
    }

    /* Remove the up/down and left/right buttons */
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        background: none;
        border: none;
    }
""")

    return scroll_area
