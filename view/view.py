from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from .features.BasisVectorInput import *
from .features import SidePaneltButtonSet
from .components import SidePanel, MainPanel
from .widgets import ToolButton


class PlotView(QWidget):
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
            self.basisVectorInputs, self.sidePanelButtons)

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

        # self.initMainPlot()

    def initMainPlot(self):
        # Set Main Plot Area Layout
        main_plot_layout = QVBoxLayout()
        # main_plot_layout.addStretch()
        self.mainPlotArea.setLayout(main_plot_layout)

        # Create Matplotlib Figure and Canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Add the canvas to the main plot area
        main_plot_layout.addWidget(self.canvas)
        self.mainPlotArea.setStyleSheet(
            "background-color: #ffffff; border-left: 2px solid #ccc;")

    def render(self):
        # Render the plot using a plotting library
        pass
