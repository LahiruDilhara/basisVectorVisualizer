from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def ScrollCard(subWidget: QWidget, resizable: bool = False):
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(resizable)
    scroll_area.setWidget(subWidget)
    # scroll_area.setStyleSheet("""
    #     QScrollArea {
    #         border: none;
    #         background: #fffff; /* Dark mode background */
    #         border-radius: 10px;
    #     }

    #     /* Hide scrollbar background */
    #     QScrollBar:vertical {
    #         background: #1E1E1E;
    #         width: 8px;
    #         border-radius: 4px;
    #     }

    #     QScrollBar::handle:vertical {
    #         background: #555;
    #         min-height: 20px;
    #         border-radius: 4px;
    #     }

    #     QScrollBar::handle:vertical:hover {
    #         background: #777;
    #     }

    #     QScrollBar::handle:vertical:pressed {
    #         background: #999;
    #     }

    #     QScrollBar::add-line:vertical,
    #     QScrollBar::sub-line:vertical {
    #         background: none;
    #         border: none;
    #     }

    #     QLabel {
    #         color: white;
    #         font-size: 14px;
    #         padding: 5px;
    #     }
    # """)

    return scroll_area
