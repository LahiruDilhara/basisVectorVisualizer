from PySide6.QtCore import QObject, Signal

from ..Types import BasisVector, ToolBoxState
from ..core.DataTypes import Vector
import copy
import numpy as np

from ..domain.VectorService import VectorService


class PlotAreaViewModel(QObject):

    vectorUpdated: Signal = Signal(int, int, str, str, int, int, int)

    plotLimitChanged: Signal = Signal(object, object)

    plotCleared: Signal = Signal()

    def __init__(self, vectorService: VectorService):
        super().__init__()
        self.service: VectorService = vectorService

        # State
        self.basisVector: BasisVector = None
        self.vectorList: list[Vector] = None

    def SetPlotVectors(self, basisVector: BasisVector, vectorList: list[Vector]):
        self.basisVector = basisVector
        self.vectorList = vectorList
        self.clearPlot()
        self.PlotVectors()

    def PlotVectors(self):
        basei = [self.basisVector.ix, self.basisVector.iy]
        basej = [self.basisVector.jx, self.basisVector.jy]
        processedVectors: list[np.ndarray[int, int]] = []
        for vector in self.vectorList:
            if (not vector.enabled):
                continue
            processedVector = self.service.vectorFromBases(
                iScaler=vector.iScaler, jScaler=vector.jScaler, iBase=basei, jBase=basej)
            processedVectors.append(processedVector)
            self.vectorUpdated.emit(
                processedVector[0], processedVector[1], vector.color, vector.name, 0, 0, vector.thickness)
        self.setPlotSize(processedVectors)

    def setPlotSize(self, vectors: list[np.ndarray[int, int]]):
        minX = 0
        maxX = 0
        minY = 0
        maxY = 0

        for vector in vectors:
            if vector[0] > maxX:
                maxX = vector[0]
            elif vector[0] < minX:
                minX = vector[0]

            if vector[1] > maxY:
                maxY = vector[1]
            elif vector[1] < minY:
                minY = vector[1]

        minX -= 10
        maxX += 10
        minY -= 10
        maxY += 10
        self.plotLimitChanged.emit([minX, maxX], [minY, maxY])

    def plotActionHandler(self, toolBoxState: ToolBoxState):
        self.clearPlot()
        if toolBoxState.plotStandardBasisVectors:
            self.plotStandardBasisVectors()
        if self.basisVector == None or self.vectorList == None:
            return
        if toolBoxState.plotVectors:
            self.PlotVectors()

    def plotStandardBasisVectors(self):
        self.vectorUpdated.emit(
            1, 0, "#000000", "i", 0, 0, 50)
        self.vectorUpdated.emit(
            0, 1, "#000000", "j", 0, 0, 50)

    def clearPlot(self):
        self.plotCleared.emit()
