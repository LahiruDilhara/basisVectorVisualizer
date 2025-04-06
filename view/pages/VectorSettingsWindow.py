from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..components import NewVectorPanel
from ..widgets import sidePanelButton


class VectorSettingsWindow(QWidget):

    vectorPanelSpec: NewVectorPanel.VectorPanelSpec = NewVectorPanel.VectorPanelSpec()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Settings")

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create button
        addButton = sidePanelButton.SidePanelButton(
            "Add Vector", buttonColor="#4CAF50", buttonHoverColor="#45a049", buttonPressedColor="#3e8e41", onPressed=None)

        layout.addWidget(NewVectorPanel.NewVectorPanel(
            vectorPanelSpec=self.vectorPanelSpec))
        layout.addWidget(addButton)
