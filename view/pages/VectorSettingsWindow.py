from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..components import NewVectorPanel, VectorListPanel
from ..widgets import sidePanelButton
from ..core.DataTypes import Vector


class VectorSettingsWindow(QWidget):

    vectorPanelSpec: NewVectorPanel.VectorPanelSpec = NewVectorPanel.VectorPanelSpec()

    vectorList = [
        Vector("1", "v1", 2, 4, True, 5, "red"),
        Vector("2", "v2", 4, 8, True, 50, "green"),
        Vector("4", "v4", 9, 10, False, 10, "yellow"),
        Vector("5", "v5", 14, 25, False, 20, "purple"),
    ]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Settings")

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create button
        addButton = sidePanelButton.SidePanelButton(
            "Add Vector", buttonColor="#4CAF50", buttonHoverColor="#45a049", buttonPressedColor="#3e8e41", onPressed=None)

        # Create Vector List Panel
        vectorListPanel = VectorListPanel.VectorListPanel(
            vectors=self.vectorList, onUp=self.onUp, onDown=self.onDown, onDelete=self.onDelete)

        layout.addWidget(NewVectorPanel.NewVectorPanel(
            vectorPanelSpec=self.vectorPanelSpec))
        layout.addWidget(addButton)
        layout.addWidget(vectorListPanel)

    def onDelete(self, id: str):
        print(id)

    def onUp(self, id: str):
        print(id)

    def onDown(self, id: str):
        print(id)
