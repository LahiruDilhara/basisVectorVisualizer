from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


class ScrollCard(QScrollArea):
    def __init__(self, subWidget: QWidget, resizable: bool = False, verticalScrolling: bool = True, horizontalScrolling: bool = True, minHeight: int = None, minWidth: int = None):
        super().__init__()
        self.subWidget = subWidget
        self.resizable = resizable
        self.verticalScrolling = verticalScrolling
        self.horizontalScrolling = horizontalScrolling

        if minHeight:
            self.setMinimumHeight(minHeight)

        if minWidth:
            self.setMinimumWidth(minWidth)

        self.initUI()

    def initUI(self):
        self.setWidgetResizable(self.resizable)
        self.setWidget(self.subWidget)

        if self.verticalScrolling:
            self.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        else:
            self.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        if self.horizontalScrolling:
            self.setHorizontalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        else:
            self.setHorizontalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setStyleSheet("""
        QScrollArea {
            border: none;
            background: #f4f4f4;
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

    # def setScrollAreaWidth(self):
    #     if not self.horizontalScrolling:
    #         self.setFixedWidth((self.subWidget.minimumSizeHint().width(
    #         ) + self.verticalScrollBar().sizeHint().width()))
