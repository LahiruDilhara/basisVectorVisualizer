from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QColor

from ..components import NewVectorPanel, VectorListPanel
from ..widgets import sidePanelButton
from ...core.DataTypes import Vector
from ..widgets import ScrollCard

from ..viewModel import MainWindowViewModel, VectorSettingsViewModel


class VectorSettingsWindow(QWidget):

    def __init__(self, mainViewModel: MainWindowViewModel.MainWindowViewModel, viewModel: VectorSettingsViewModel.VectorSettingsViewModel):
        super().__init__()
        self.setWindowTitle("Vector Settings")
        self.mainViewModel = mainViewModel
        self.viewModel = viewModel
        self.scrollableVectorListPanel = None
        self.vectorListPanel = None
        self.layout: QVBoxLayout = None

        self.initUI()

        self.connectSignals()

    def connectSignals(self):
        self.mainViewModel.vectorListChanged.connect(self.onVectorListChange)

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

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create new vector panel
        vectorPanel = NewVectorPanel.NewVectorPanel(
            vectorPanelSpec=self.vectorPanelSpec)

        # Create button
        addButton = sidePanelButton.SidePanelButton(
            "Add Vector", buttonColor="#4CAF50", buttonHoverColor="#45a049", buttonPressedColor="#3e8e41", onPressed=lambda: self.viewModel.addVector(self.mainViewModel.onVectorAdd))

        # Create Vector List Panel
        self.vectorListPanel = VectorListPanel.VectorListPanel(
            vectors=self.mainViewModel.vectorList, onUp=self.mainViewModel.onVectorMoveUp, onDown=self.mainViewModel.onVectorMoveDown, onDelete=self.mainViewModel.onVectorDelete)

        self.scrollableVectorListPanel = ScrollCard.ScrollCard(
            self.vectorListPanel, resizable=True, horizontalScrolling=False, minWidth=600)
        self.setFixedHeight(600)

        self.layout.addWidget(vectorPanel)
        self.layout.addWidget(addButton)
        self.layout.addWidget(self.scrollableVectorListPanel)

    def onVectorListChange(self, vectorList: list[Vector]):
        self.setUpdatesEnabled(False)
        # remove the flickering and adjust the window size
        QTimer.singleShot(0, self.adjustSize)
        self.setUpdatesEnabled(True)
        self.vectorListPanel.setListItems(vectorList=vectorList)
