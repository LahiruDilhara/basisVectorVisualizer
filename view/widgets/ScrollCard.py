from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def ScrollCard(subWidget: QWidget, resizable: bool = False):

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(resizable)
    scroll_area.setWidget(subWidget)

    scroll_area.setStyleSheet("""
        QScrollArea {
            border: none;
            background: #ffffff;
            border-radius: 10px;
        }

        QScrollBar:vertical {
            background: #f4f4f4;
            width: 8px;
            border-radius: 4px;
        }

        QScrollBar::handle:vertical {
            background: #BBB;
            min-height: 20px;
            border-radius: 4px;
        }
        QScrollBar::handle:vertical:hover {
            background: #777;
        }
        QScrollBar::handle:vertical:pressed {
            background: #999;
        }
        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            background: none;
            border: none;
        }

    """)

    return scroll_area
