from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QCloseEvent
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from ..features.BasisVectorInput import *
from ..features import SidePaneltButtonSet, SidePanelVectorList
from ..components import SidePanel, MainPanel
from ..widgets import ToolButton, ToolColorButton
from .VectorSettingsWindow import VectorSettingsWindow
from ..core.DataTypes import Vector

from ..viewModel.MainWindowViewModel import MainWindowViewModel
from ..viewModel.VectorSettingsViewModel import VectorSettingsViewModel


class MainWindow(QWidget):

    def __init__(self, viewModel: MainWindowViewModel):
        super().__init__()
        self.viewModel = viewModel

        self.basisVectorInputs: BasisVectorInputSpec = BasisVectorInputSpec(
            ixOnChange=viewModel.onBasisVectorIxChange,
            iyOnChange=viewModel.onBasisVectorIyChange,
            jxOnChange=viewModel.onBasisVectorJxChange,
            jyOnChange=viewModel.onBasisVectorJyChange
        )

        self.vectorSettingsWindow = None

        # Initialize UI components
        self.initUI()
        self.connectSignals()

    def initUI(self):
        self.setWindowTitle("Base Vector Display")
        self.setGeometry(100, 100, 1500, 800)

        # Main Layout
        self.mainLayout = QHBoxLayout()
        # Set the main layout
        self.setLayout(self.mainLayout)

        sidePanelButtons: list[SidePaneltButtonSet.SidePanelButtonSpec] = [
            SidePaneltButtonSet.SidePanelButtonSpec(
                text="Vector Settings", onPressed=self.openVectorSettingsWindow),
            SidePaneltButtonSet.SidePanelButtonSpec(
                text="Save"),  # Save Function
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

        self.mainPlotArea = MainPanel.MainPanel(toolBarButtons=toolBarButtons)

        # Add the main layout components
        self.mainLayout.addWidget(self.sidebar, 4)
        self.mainLayout.addWidget(self.mainPlotArea, 15)

    def connectSignals(self):
        self.viewModel.vectorListChanged.connect(self.sidebar.updateVectorList)

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
