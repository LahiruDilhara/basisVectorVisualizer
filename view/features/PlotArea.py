from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from ..core.DataTypes import Vector
from ..viewModel.PlotAreaViewModel import PlotAreaViewModel


class PlotArea(QWidget):
    def __init__(self, viewModel: PlotAreaViewModel):
        super().__init__()
        self.viewModel = viewModel

        self.initUI()
        self.connectSignals()

    def initUI(self):
        # Set Main Plot Area Layout
        main_plot_layout = QVBoxLayout()
        # main_plot_layout.addStretch()
        self.setLayout(main_plot_layout)

        # Create Matplotlib Figure and Canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        plt.tight_layout()

        # Add the canvas to the main plot area
        main_plot_layout.addWidget(self.canvas)
        self.setStyleSheet(
            "background-color: #f4f4f4;")

        self.setCordinateSystem()

        self.canvas.mpl_connect("motion_notify_event", self.mouse_move_event)

    def connectSignals(self):
        self.viewModel.vectorUpdated.connect(self.plotVectorHandler)
        self.viewModel.plotLimitChanged.connect(self.plotSizeHandler)
        self.viewModel.plotCleared.connect(self.clearPlotHandler)
        pass

    def plotVectorHandler(self, x: int, y: int, color: str, name: str, originX: int = 0, originY: int = 0, thickness: int = 0):
        self.ax.quiver(originX, originY, x, y, angles='xy',
                       scale_units='xy', scale=1, color=color, label=name, width=(thickness/10000))
        self.drawPlot()

    def plotSizeHandler(self, xLim: list[int, int], yLim: list[int, int]):
        xAspect = self.width() / self.height()
        yAspect = 1

        self.ax.set_xlim(xLim[0] * xAspect,  xLim[1] * xAspect)
        self.ax.set_ylim(yLim[0] * yAspect, yLim[1] * yAspect)
        # self.ax.set_xlim(xLim)
        # self.ax.set_ylim(yLim)
        self.canvas.draw()

    def clearPlotHandler(self):
        self.ax.clear()
        self.setCordinateSystem()
        self.canvas.draw()

    def drawPlot(self):
        self.ax.legend()
        self.canvas.draw()

    def setCordinateSystem(self):
        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.axvline(0, color='black', linewidth=1)
        self.ax.grid(True, linestyle="--", alpha=0.5)

        xAspect = self.width() / self.height()
        yAspect = 1

        self.ax.set_xlim(-10 * xAspect, 10 * xAspect)
        self.ax.set_ylim(-10 * yAspect, 10 * yAspect)

        self.ax.grid(True, linestyle="--", linewidth=0.5)
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")

        # self.ax.set_aspect("equal")
        self.ax.set_adjustable('datalim')

    def mouse_move_event(self, event):
        if event.xdata is not None and event.ydata is not None:
            print(
                f"Mouse Coordinates: ({event.xdata:.2f}, {event.ydata:.2f})")
        else:
            print("Mouse Coordinates: ( , )")
