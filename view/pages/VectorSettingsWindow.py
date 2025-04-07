from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..components import NewVectorPanel, VectorListPanel
from ..widgets import sidePanelButton
from ..core.DataTypes import Vector


class VectorSettingsWindow(QWidget):

    vectorList = [
        Vector(1, "v1", 2, 4, True, 5, "red"),
        Vector(2, "v2", 4, 8, True, 50, "green"),
        Vector(4, "v4", 9, 10, False, 10, "yellow"),
        Vector(5, "v5", 14, 25, False, 20, "purple"),
    ]

    def setName(self, value):
        self.name = value

    def setIScaler(self, value):
        self.iScaler = value

    def setJScaler(self, value):
        self.jScaler = value

    def setThickness(self, value):
        self.iScaler = value

    def setColor(self, value):
        self.color = value

    def setEnabled(self, value):
        self.enabled = value

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Settings")

        # Initialize the data holding part for vector panel section
        self.name = "name"
        self.iScaler = 0
        self.jScaler = 0
        self.thickness = 1
        self.color = "#4CAF50"
        self.enabled = True

        self.vectorPanelSpec: NewVectorPanel.VectorPanelSpec = NewVectorPanel.VectorPanelSpec(
            onEnableInputChange=self.setEnabled,
            onIScallerChange=self.setIScaler,
            onJScallerChange=self.setJScaler,
            onVectorColorChange=self.setColor,
            onVectorNameChange=self.setName,
            onVectorThiknesChange=self.setThickness,
            defaultName=self.name,
            defaultIScaler=self.iScaler,
            defaultJScaler=self.jScaler,
            defaultColor=self.color,
            defaultEnabled=self.enabled,
            defaultThickness=self.thickness
        )

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
        id = self.getId()
        vector = Vector(id, self.name, self.iScaler, self.jScaler,
                        self.enabled, self.thickness, self.color)
        print(vector)
        if not self.validateVector(vector):
            return

        self.vectorList.append(vector)
        self.vectorListPanel.setListItems(self.vectorList)

    def validateVector(self, vector: Vector) -> bool:
        if (vector.thickness <= 0):
            return False
        if (len(vector.name) <= 1):
            return False
        if (len(vector.color) <= 2):
            return False
        return True

    def getId(self):
        max = -1
        for i in self.vectorList:
            if (i.id > max):
                max = i.id
        return max + 1
