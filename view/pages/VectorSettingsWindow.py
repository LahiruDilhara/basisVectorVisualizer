from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QColor

from ..components import NewVectorPanel, VectorListPanel
from ..widgets import sidePanelButton
from ..core.DataTypes import Vector

from ..viewModel import MainWindowViewModel, VectorSettingsViewModel


class VectorSettingsWindow(QWidget):

    vectorList = [
        Vector(1, "v1", 2, 4, True, 5, "red"),
        Vector(2, "v2", 4, 8, True, 50, "green"),
        Vector(4, "v4", 9, 10, False, 10, "yellow"),
        Vector(5, "v5", 14, 25, False, 20, "purple"),
    ]

    def __init__(self, mainViewModel: MainWindowViewModel.MainWindowViewModel, viewModel: VectorSettingsViewModel.VectorSettingsViewModel):
        super().__init__()
        self.setWindowTitle("Vector Settings")
        self.mainViewModel = mainViewModel
        self.viewModel = viewModel

        self.initUI()

    def initUI(self):

        self.vectorPanelSpec: NewVectorPanel.VectorPanelSpec = NewVectorPanel.VectorPanelSpec(
            onEnableInputChange=self.viewModel.setEnabled,
            onIScallerChange=self.viewModel.setIScaler,
            onJScallerChange=self.viewModel.setJScaler,
            onVectorColorChange=self.viewModel.setColor,
            onVectorNameChange=self.viewModel.setName,
            onVectorThiknesChange=self.viewModel.setThickness,
            defaultName=self.viewModel.name,
            defaultIScaler=self.viewModel.iScaler,
            defaultJScaler=self.viewModel.jScaler,
            defaultColor=self.viewModel.color,
            defaultEnabled=self.viewModel.enabled,
            defaultThickness=self.viewModel.thickness
        )

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create new vector panel
        vectorPanel = NewVectorPanel.NewVectorPanel(
            vectorPanelSpec=self.vectorPanelSpec)

        # Create button
        addButton = sidePanelButton.SidePanelButton(
            "Add Vector", buttonColor="#4CAF50", buttonHoverColor="#45a049", buttonPressedColor="#3e8e41", onPressed=lambda: self.viewModel.addVector(self.mainViewModel.onVectorAdd))

        # Create Vector List Panel
        self.vectorListPanel = VectorListPanel.VectorListPanel(
            vectors=self.vectorList, onUp=self.mainViewModel.onVectorMoveUp, onDown=self.mainViewModel.onVectorMoveDown, onDelete=self.mainViewModel.onVectorDelete)

        layout.addWidget(vectorPanel)
        layout.addWidget(addButton)
        layout.addWidget(self.vectorListPanel)

    def onDelete(self, id: str):
        for index, vector in enumerate(self.vectorList):
            if (vector.id == id):
                self.vectorList.pop(index)
                break

        self.vectorListPanel.setListItems(self.vectorList)
        self.refresh()

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

    def refresh(self):
        self.setUpdatesEnabled(False)
        # remove the flickering and adjust the window size
        QTimer.singleShot(0, self.adjustSize)
        self.setUpdatesEnabled(True)

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
        if not self.validateVector(vector):
            return

        self.vectorList.append(vector)
        self.vectorListPanel.setListItems(self.vectorList)
        self.refresh()
