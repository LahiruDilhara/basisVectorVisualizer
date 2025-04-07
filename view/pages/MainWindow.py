from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QCloseEvent
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from ..features.BasisVectorInput import *
from ..features import SidePaneltButtonSet, SidePanelVectorList
from ..components import SidePanel, MainPanel
from ..widgets import ToolButton
from .VectorSettingsWindow import VectorSettingsWindow
from ..core.DataTypes import Vector


class MainWindow(QWidget):

    basisVectorInputs: BasisVectorInputSpec = BasisVectorInputSpec(
        ixOnChange=lambda x: print(x),
        iyOnChange=lambda x: print(x),
        jxOnChange=lambda x: print(x),
        jyOnChange=lambda x: print(x)
    )

    vectorList: list[Vector] = [
        Vector(1, "v1", 2, 4, True, 5, "red"),
        Vector(2, "v2", 4, 8, True, 50, "green"),
        Vector(4, "v4", 9, 10, False, 10, "yellow"),
        Vector(5, "v5", 14, 25, False, 20, "purple"),
    ]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Base Vector Display")
        self.setGeometry(100, 100, 1500, 800)
        self.vectorSettingsWindow = VectorSettingsWindow()

        # Initialize UI components
        self.initUI()
        # Set the main layout
        self.setLayout(self.mainLayout)

    def initUI(self):
        sidePanelButtons: list[SidePaneltButtonSet.SidePanelButtonSpec] = [
            SidePaneltButtonSet.SidePanelButtonSpec(
                text="Vector Settings", onPressed=self.openVectorSettingsWindow),
            SidePaneltButtonSet.SidePanelButtonSpec(
                text="Save"),  # Save Function
        ]
        # Main Plot Area
        toolBarButtons = [
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("plot vectors")),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("plot standard basis vectors")),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("plot current basis vectors")),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("draw the shape")),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("fill the shape")),
        ]

        # Main Layout
        self.mainLayout = QHBoxLayout()

        # Left Sidebar
        self.sidebar = SidePanel.SidePanel(
            self.basisVectorInputs, sidePanelButtons, vectorList=self.vectorList)

        self.mainPlotArea = MainPanel.MainPanel(toolBarButtons=toolBarButtons)

        # Add the main layout components
        self.mainLayout.addWidget(self.sidebar, 4)
        self.mainLayout.addWidget(self.mainPlotArea, 15)

    def openVectorSettingsWindow(self):
        self.vectorSettingsWindow.show()

    def closeEvent(self, event: QCloseEvent):
        # Ensure the VectorSettingsWindow is closed when the main window closes
        if self.vectorSettingsWindow:
            self.vectorSettingsWindow.close()

        event.accept()  # Continue with the close event
