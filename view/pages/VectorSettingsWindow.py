from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..components import NewVectorPanel


class VectorSettingsWindow(QWidget):

    vectorPanelSpec: NewVectorPanel.VectorPanelSpec = NewVectorPanel.VectorPanelSpec()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Settings")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(NewVectorPanel.NewVectorPanel(
            vectorPanelSpec=self.vectorPanelSpec))
