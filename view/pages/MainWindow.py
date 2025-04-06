from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from ..features.BasisVectorInput import *
from ..features import SidePaneltButtonSet, SidePanelVectorList
from ..components import SidePanel, MainPanel
from ..widgets import ToolButton


class MainWindow(QWidget):
    sidePanelButtons: list[SidePaneltButtonSet.SidePanelButtonSpec] = [
        SidePaneltButtonSet.SidePanelButtonSpec(text="Plot Vectors"),
        SidePaneltButtonSet.SidePanelButtonSpec(text="Clear Plot"),
    ]
    basisVectorInputs: BasisVectorInputSpec = BasisVectorInputSpec(
        ixOnChange=lambda x: print(x),
        iyOnChange=lambda x: print(x),
        jxOnChange=lambda x: print(x),
        jyOnChange=lambda x: print(x)
    )

    vectorList: list[SidePanelVectorList.VectorListItem] = [
        SidePanelVectorList.VectorListItem(0, "vector 1", True),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", True),
        SidePanelVectorList.VectorListItem(0, "vector 1", True),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
        SidePanelVectorList.VectorListItem(0, "vector 1", False),
    ]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Base Vector Display")
        self.setGeometry(100, 100, 1500, 800)

        # Initialize UI components
        self.initUI()
        # Set the main layout
        self.setLayout(self.mainLayout)

    def initUI(self):
        # Main Layout
        self.mainLayout = QHBoxLayout()

        # Left Sidebar
        self.sidebar = SidePanel.SidePanel(
            self.basisVectorInputs, self.sidePanelButtons, vectorList=self.vectorList)

        # Main Plot Area
        toolBarButtons = [
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("copy")),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("paste")),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("delete")),
            ToolButton.ToolButton(
                toolButtonSpec=ToolButton.ToolButtonSpec("write")),
        ]
        self.mainPlotArea = MainPanel.MainPanel(toolBarButtons=toolBarButtons)

        # Add the main layout components
        self.mainLayout.addWidget(self.sidebar, 4)
        self.mainLayout.addWidget(self.mainPlotArea, 15)

    def render(self):
        # Render the plot using a plotting library
        pass
