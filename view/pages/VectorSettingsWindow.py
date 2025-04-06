from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..components import NewVectorPanel, VectorListPanel
from ..widgets import sidePanelButton
from ..core.DataTypes import Vector


class VectorSettingsWindow(QWidget):

    vectorPanelSpec: NewVectorPanel.VectorPanelSpec = NewVectorPanel.VectorPanelSpec(

    )

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

        # Create new vector panel
        vectorPanel = NewVectorPanel.NewVectorPanel(
            vectorPanelSpec=self.vectorPanelSpec)

        # Create button
        addButton = sidePanelButton.SidePanelButton(
            "Add Vector", buttonColor="#4CAF50", buttonHoverColor="#45a049", buttonPressedColor="#3e8e41", onPressed=self.onAdd)

        # Create Vector List Panel
        self.vectorListPanel = VectorListPanel.VectorListPanel(
            vectors=self.vectorList, onUp=self.onUp, onDown=self.onDown, onDelete=self.onDelete)

        layout.addWidget(vectorPanel)
        layout.addWidget(addButton)
        layout.addWidget(self.vectorListPanel)

    def onDelete(self, id: str):
        for index, vector in enumerate(self.vectorList):
            if (vector.id == id):
                self.vectorList.pop(index)
                break

        self.vectorListPanel.setListItems(self.vectorList)

    def onUp(self, id: str):
        index = -1

        for i, vector in enumerate(self.vectorList):
            if (vector.id == id):
                index = i
                break

        if (index == -1):
            return

        if (index > 0):
            item = self.vectorList.pop(index)
            self.vectorList.insert(index - 1, item)

        self.vectorListPanel.setListItems(self.vectorList)

    def onDown(self, id: str):
        index = -1

        for i, vector in enumerate(self.vectorList):
            if (vector.id == id):
                index = i
                break

        if (index == -1):
            return

        if (index < len(self.vectorList) - 1):
            item = self.vectorList.pop(index)
            self.vectorList.insert(index + 1, item)

        self.vectorListPanel.setListItems(self.vectorList)

    def onAdd(self):
        pass

    def validateVector(self, vector: Vector) -> bool:
        try:
            int(vector.id)
            int(vector.iScaler)
            int(vector.jScaler)
            int(vector.thickness)
            if (len(vector.name) <= 1):
                return False
            if (len(vector.color) <= 2):
                return False
        except:
            return False
        return True
