from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QToolBar, QToolButton
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QFont, QColor, QWheelEvent, QIcon, QAction
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.backend_bases import MouseEvent

from ...core.DataTypes import Vector
from ..viewModel.PlotAreaViewModel import PlotAreaViewModel

from importlib import resources

file_path = resources.files("basisvectorvisualizer.assets.icons");


class MTooBar(NavigationToolbar2QT):
    def __init__(self, canvas, parent=None, coordinates=True):
        super().__init__(canvas, parent, coordinates)

        customIcons = {
            "home": "assets/icons/icons8-home-512.png",
            "back": "assets/icons/icons8-left-arrow-96.png",
            "forward": "assets/icons/icons8-right-arrow-96.png",
            "zoom": "assets/icons/icons8-zoom-to-extents-100.png",
            "pan": "assets/icons/icons8-move-100.png",
            "settings": "assets/icons/icons8-settings-500.png",
            "graph": "assets/icons/icons8-graph-96.png",
            "save": "assets/icons/icons8-save-100.png",
        }

        # change the default icons
        for action in self.actions():
            if action.text() == "Home":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-home-512.png"))))
            if action.text() == "Back":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-left-arrow-96.png"))))
            if action.text() == "Forward":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-right-arrow-96.png"))))
            if action.text() == "Pan":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-move-100.png"))))
            if action.text() == "Zoom":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-zoom-to-extents-100.png"))))
            if action.text() == "Subplots":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-settings-500.png"))))
            if action.text() == "Customize":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-graph-96.png"))))
            if action.text() == "Save":
                action.setIcon(QIcon(str(file_path.joinpath("icons8-save-100.png"))))

        # Set icons size
        self.setIconSize(QSize(32, 32))


class PlotArea(QWidget):
    def __init__(self, viewModel: PlotAreaViewModel):
        super().__init__()
        self.viewModel = viewModel

        self.vectorAnimationDict: dict[int, animation.Animation] = {}

        self.initUI()
        self.connectSignals()
        self.animationCounter = 0

    def initUI(self):
        # Set Main Plot Area Layout
        main_plot_layout = QVBoxLayout()
        # main_plot_layout.addStretch()
        self.setLayout(main_plot_layout)

        # Create Matplotlib Figure and Canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.toolBox = MTooBar(self.canvas, self)
        # self.toolBox = NavigationToolbar2QT(self.canvas, self)

        plt.tight_layout()

        # Add the canvas to the main plot area
        main_plot_layout.addWidget(self.toolBox)
        main_plot_layout.addWidget(self.canvas)
        self.setStyleSheet(
            "background-color: #f4f4f4;")

        self.canvas.mpl_connect("scroll_event", self.onScroll)

        self.setCordinateSystem()

        # self.canvas.mpl_connect("motion_notify_event", self.mouse_move_event)
    def onScroll(self, event: MouseEvent):
        ZOOMVALUE = 1
        xLimit = self.ax.get_xlim()
        yLimit = self.ax.get_ylim()

        if (event.xdata == None or event.ydata == None):
            return

        xNegativeLimitToMouse = event.xdata - xLimit[0]
        xPositiveLimitToMouse = xLimit[1] - event.xdata
        yNegativeLimitToMouse = event.ydata - yLimit[0]
        yPositiveLimitToMouse = yLimit[1] - event.ydata

        xNToxPRatio = xNegativeLimitToMouse / xPositiveLimitToMouse
        yNToyPRatio = yNegativeLimitToMouse / yPositiveLimitToMouse

        xPostiveSideAddition = ZOOMVALUE
        xNegativeSideAddition = ZOOMVALUE * xNToxPRatio

        yPositiveSideAddition = ZOOMVALUE
        yNegativeSideAddition = ZOOMVALUE * yNToyPRatio

        # Get direction
        direction = 1 if event.button == "up" else -1

        # Set Directed additions
        newXNLimit = xLimit[0] + \
            (xNegativeSideAddition * direction)
        newXPLimit = xLimit[1] - (xPostiveSideAddition * direction)
        newYNLimit = yLimit[0] + \
            (yNegativeSideAddition * direction)
        newYPLimit = yLimit[1] - \
            (yPositiveSideAddition * direction)

        # self.ax.set_xlim(newXNLimit, newXPLimit)
        # self.ax.set_ylim(newYNLimit, newYPLimit)
        # print(
        #     f"cXLimit: {xLimit} , cYLimit: {yLimit}. nXLimit: {[newXNLimit,newXPLimit]} , nYLimit: {[newYNLimit,newYPLimit]}\n")
        self.plotSizeHandler(
            xLim=[newXNLimit, newXPLimit], yLim=[newYNLimit, newYPLimit], offset=1)

    def connectSignals(self):
        self.viewModel.vectorUpdated.connect(self.plotVectorHandler)
        self.viewModel.plotLimitChanged.connect(self.plotSizeHandler)
        self.viewModel.plotCleared.connect(self.clearPlotHandler)
        self.viewModel.shapeUpdated.connect(self.plotDrawHandler)

    def plotVectorHandler(self, x: int, y: int, color: str, name: str, originX: int = 0, originY: int = 0, thickness: int = 0):
        initialQuiver = self.ax.quiver(originX, originY, 0, 0, angles="xy",
                                       scale_units="xy", scale=1, color=color, label=name, width=(thickness/1000))

        # self.ax.quiver(originX, originY, x, y, angles='xy',
        #                scale_units='xy', scale=1, color=color, label=name, width=(thickness/10000))
        animationId = self.animationCounter

        ani: animation.TimedAnimation = animation.FuncAnimation(
            self.figure, lambda f: self.update(f, 0, 0, x, y, initialQuiver, totalFrames=10, id=animationId), frames=10, interval=1, blit=False, repeat=False)
        # save the animation until it finished
        animationId = self.addAnimation(ani, animationId)

        # increment animation counter
        self.animationCounter += 1

        self.drawPlot()

    def addAnimation(self, ani: animation.Animation, id: int):
        self.vectorAnimationDict[id] = ani

    def removeAnimation(self, id: int):
        if id in self.vectorAnimationDict:
            del self.vectorAnimationDict[id]

    def animationFinished(self, ani):
        pass
        # if ani in self.vectorAnimationDict:
        #     self.vectorAnimationDict.remove(ani)

    def plotSizeHandler(self, xLim: list[int, int], yLim: list[int, int], offset: float = 1):
        graphWidth = abs(xLim[0]) + abs(xLim[1])
        graphHeight = abs(yLim[0]) + abs(yLim[1])

        figureWidth, figureHeight = self.figure.get_size_inches() * self.figure.dpi

        addedWidth, addedHeight = self.getAspectedAdedValues(
            figureWidth, figureHeight, graphWidth, graphHeight, offset=offset)

        xAddition = addedWidth / 2
        yAddtion = addedHeight / 2

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
        if (len(vectorList) <= 1):
            return
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
        cTd = requiredAspectWidth / requiredAspectHeight
        m = cTd * (y1 + offset) - x1
        # m = ((requiredAspectWidth*y1) + (requiredAspectWidth*offset) -
        #      (requiredAspectHeight*x1)) / requiredAspectHeight
        return (m, offset)

    def update(self, frame, U1, V1, U2, V2, quiver, totalFrames, id: int):
        progress = frame / (totalFrames - 1)

        U = (U2 - U1) * progress
        V = (V2 - V1) * progress

        quiver.set_UVC(U, V)

        if frame == totalFrames - 1:
            QTimer.singleShot(1, lambda: self.removeAnimation(id))

        return quiver,
