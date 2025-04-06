from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


class VectorSettingsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Base Vector Display")
        self.setGeometry(100, 100, 1500, 800)
        self.setLayout(QHBoxLayout())
