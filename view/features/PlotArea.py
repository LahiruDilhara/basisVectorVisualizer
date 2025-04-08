from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.patches as patches
import matplotlib.animation as animation

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

        # self.canvas.mpl_connect("motion_notify_event", self.mouse_move_event)

    def connectSignals(self):
        self.viewModel.vectorUpdated.connect(self.plotVectorHandler)
        self.viewModel.plotLimitChanged.connect(self.plotSizeHandler)
        self.viewModel.plotCleared.connect(self.clearPlotHandler)
        self.viewModel.shapeUpdated.connect(self.plotDrawHandler)

    def plotVectorHandler(self, x: int, y: int, color: str, name: str, originX: int = 0, originY: int = 0, thickness: int = 0):
        initialQuiver = self.ax.quiver(originX, originY, 0, 0, angles="xy",
                                       scale_units="xy", scale=1, color=color, label=name, width=(thickness/10000))

        self.ax.quiver(originX, originY, x, y, angles='xy',
                       scale_units='xy', scale=1, color=color, label=name, width=(thickness/10000))

        # def update(frame, U1, V1, U2, V2, quiver):
        #     # Calculate alpha based on frame but adjust it to prevent overshooting
        #     alpha = min(frame / 20, 1)  # Ensures alpha doesn't exceed 1

        #     # Interpolate the vector components smoothly
        #     U = (1 - alpha) * U1 + alpha * U2
        #     V = (1 - alpha) * V1 + alpha * V2

        #     quiver.set_UVC(U, V)  # Update quiver's vector
        #     return quiver,

        # ani = animation.FuncAnimation(
        #     self.figure, lambda f: update(f, 0, 0, x, y, initialQuiver), frames=52, interval=1, blit=False, repeat=False)

        self.drawPlot()

    def plotSizeHandler(self, xLim: list[int, int], yLim: list[int, int], offset: float = 1):
        graphWidth = abs(xLim[0]) + abs(xLim[1])
        graphHeight = abs(yLim[0]) + abs(yLim[1])

        figureWidth, figureHeight = self.figure.get_size_inches() * self.figure.dpi

        addedWidth, addedHeight = self.getAspectedAdedValues(
            figureWidth, figureHeight, graphWidth, graphHeight, offset=offset)

        xAddition = abs(addedWidth) / 2
        yAddtion = abs(addedHeight) / 2

        newXLim = [xLim[0] - xAddition, xLim[1] + xAddition]
        newYLim = [yLim[0] - yAddtion, yLim[1] + yAddtion]

        # print("\nadded x value", xAddition)
        # print("added y value", yAddtion)
        # print("given x limit", xLim)
        # print("given y limit", yLim)
        # print("new x limit", newXLim)
        # print("new y limit", newYLim)

        self.ax.set_xlim(newXLim[0], newXLim[1])
        self.ax.set_ylim(newYLim[0], newYLim[1])
        self.canvas.draw()

    def plotDrawHandler(self, vectorList: list[int, int], color: str, fill: bool):
        npVectors = np.array(vectorList)
        polygon = patches.Polygon(
            npVectors, closed=True, edgecolor=color, fill=fill, linewidth=2, facecolor=color)
        self.ax.add_patch(polygon)
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

    def getAspectedAdedValues(self, requiredAspectWidth, requiredAspectHeight, x1, y1, offset):
        m = ((requiredAspectWidth*y1) + (requiredAspectWidth*offset) -
             (requiredAspectHeight*x1)) / requiredAspectHeight
        return (m, offset)
