from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from ..core.DataTypes import Vector


class PlotArea(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set Main Plot Area Layout
        main_plot_layout = QVBoxLayout()
        # main_plot_layout.addStretch()
        self.setLayout(main_plot_layout)

        # Create Matplotlib Figure and Canvas
        figure, ax = plt.subplots()
        canvas = FigureCanvas(figure)

        plt.tight_layout()

        # Add the canvas to the main plot area
        main_plot_layout.addWidget(canvas)
        self.setStyleSheet(
            "background-color: #f4f4f4;")

    def plotVectors(self, vectorList: list[Vector]):
        pass

    def clearPlot(self):
        pass
