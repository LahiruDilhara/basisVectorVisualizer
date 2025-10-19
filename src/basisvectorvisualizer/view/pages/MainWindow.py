from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QCloseEvent, QIcon
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from ..features.BasisVectorInput import *
from ..features import SidePaneltButtonSet, SidePanelVectorList
from ..components import SidePanel, MainPanel
from ..widgets import ToolButton, ToolColorButton
from .VectorSettingsWindow import VectorSettingsWindow

from ..viewModel.MainWindowViewModel import MainWindowViewModel
from ..viewModel.VectorSettingsViewModel import VectorSettingsViewModel
from ..viewModel.PlotAreaViewModel import PlotAreaViewModel

from ...domain.VectorService import VectorService
from importlib import resources


class MainWindow(QWidget):

    def __init__(self, viewModel: MainWindowViewModel):
        super().__init__()
        self.viewModel = viewModel
        self.plotViewModel = PlotAreaViewModel(VectorService(
        ), basisVector=viewModel.basisVector, vectorList=viewModel.vectorList, toolBoxState=viewModel.toolBoxState)

        iconfile = resources.files("basisvectorvisualizer.assets.icons").joinpath("icons8-vector-96.png")
        self.setWindowIcon(QIcon(str(iconfile)))

        self.basisVectorInputs: BasisVectorInputSpec = BasisVectorInputSpec(
            ixOnChange=viewModel.onBasisVectorIxChange,
            iyOnChange=viewModel.onBasisVectorIyChange,
            jxOnChange=viewModel.onBasisVectorJxChange,
            jyOnChange=viewModel.onBasisVectorJyChange,
            defaultIx=viewModel.basisVector.ix,
            defaultIy=viewModel.basisVector.iy,
            defaultJx=viewModel.basisVector.jx,
            defaultJy=viewModel.basisVector.jy
        )

        self.vectorSettingsWindow = None

        # Initialize UI components
        self.initUI()
        self.connectSignals()

    def initUI(self):
        self.setWindowTitle("Base Vector")
        self.setWindowFlags(
            Qt.Window |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowMaximizeButtonHint |
            Qt.WindowCloseButtonHint
        )


        # Main Layout
        self.mainLayout = QHBoxLayout()
        # Set the main layout
        self.setLayout(self.mainLayout)

        sidePanelButtons: list[SidePaneltButtonSet.SidePanelButtonSpec] = [
            SidePaneltButtonSet.SidePanelButtonSpec(
                text="Vector Settings", onPressed=self.openVectorSettingsWindow),
            SidePaneltButtonSet.SidePanelButtonSpec(
                text="Save", onPressed=self.viewModel.onSave),
        ]
        # Main Plot Area
        toolBarButtons = [
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("Plot vectors", enabled=self.viewModel.toolBoxState.plotVectors, onPressed=self.viewModel.onPlotVectorToolToggle)),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("Plot standard basis vectors", enabled=self.viewModel.toolBoxState.plotStandardBasisVectors, onPressed=self.viewModel.onPlotStandardBasisVectorsToolToggle)),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("Plot current basis vectors", enabled=self.viewModel.toolBoxState.plotCurrentBasisVectors, onPressed=self.viewModel.onPlotCurrentBasisVectorsToolToggle)),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("Draw the shape", enabled=self.viewModel.toolBoxState.drawShape, onPressed=self.viewModel.onDrawShapeToolToggle)),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("Fill the shape", enabled=self.viewModel.toolBoxState.fillShape, onPressed=self.viewModel.onFillShapeToolToggle)),
            ToolColorButton.ToolColorButton(
                self.viewModel.toolBoxState.fillColor, onPressed=self.viewModel.onFillColorToolToggle)
        ]

        # Left Sidebar
        self.sidebar = SidePanel.SidePanel(
            self.basisVectorInputs, sidePanelButtons, vectorList=self.viewModel.vectorList, onVectorToggle=self.viewModel.onVectorToggle)

        self.mainPlotArea = MainPanel.MainPanel(
            toolBarButtons=toolBarButtons, plotViewModel=self.plotViewModel)

        # Add the main layout components
        self.mainLayout.addWidget(self.sidebar, 4)
        self.mainLayout.addWidget(self.mainPlotArea, 15)

    def connectSignals(self):
        self.viewModel.vectorListChanged.connect(self.sidebar.updateVectorList)
        self.viewModel.vectorListChanged.connect(
            self.plotViewModel.setVectorList)
        self.viewModel.basisVectorChanged.connect(
            self.plotViewModel.setBasisVector)
        self.viewModel.toolBoxStateChanged.connect(
            self.plotViewModel.setToolBoxState)

    def openVectorSettingsWindow(self):
        viewModel = VectorSettingsViewModel()
        self.vectorSettingsWindow = VectorSettingsWindow(
            mainViewModel=self.viewModel, viewModel=viewModel)
        self.vectorSettingsWindow.show()

    def closeEvent(self, event: QCloseEvent):
        # Ensure the VectorSettingsWindow is closed when the main window closes
        if self.vectorSettingsWindow:
            self.vectorSettingsWindow.close()

        event.accept()  # Continue with the close event
