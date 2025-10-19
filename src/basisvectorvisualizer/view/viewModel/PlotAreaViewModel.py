from PySide6.QtCore import QObject, Signal

from ..Types import  ToolBoxState
from ...core.DataTypes import Vector,BasisVector
import copy
import numpy as np
import math

from ...domain.VectorService import VectorService


class PlotAreaViewModel(QObject):

    vectorUpdated: Signal = Signal(float, float, str, str, int, int, int)

    plotLimitChanged: Signal = Signal(object, object, int)

    plotCleared: Signal = Signal()

    shapeUpdated: Signal = Signal(object, str, bool)

    def __init__(self, vectorService: VectorService, basisVector: BasisVector, vectorList: list[Vector], toolBoxState: ToolBoxState):
        super().__init__()
        self.service: VectorService = vectorService

        # State
        self.basisVector: BasisVector = basisVector
        self.vectorList: list[Vector] = vectorList
        self.toolBoxState: ToolBoxState = toolBoxState

    def setVectorList(self, vectorList: list[Vector]):
        self.vectorList = vectorList
        self.refreshPlot()

    def setBasisVector(self, basisVector: BasisVector):
        self.basisVector = basisVector
        self.refreshPlot()

    def setToolBoxState(self, toolBoxState: ToolBoxState):
        self.toolBoxState = toolBoxState
        self.refreshPlot()

    def plotVectors(self):
        if (not self.toolBoxState.plotVectors):
            return
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

        self.plotLimitChanged.emit([minX, maxX], [minY, maxY], 5)

    def plotStandardBasisVectors(self):
        if not self.toolBoxState.plotStandardBasisVectors:
            return
        self.vectorUpdated.emit(
            1, 0, "#cc0000", "Standard i", 0, 0, 5)
        self.vectorUpdated.emit(
            0, 1, "#0000cc", "Standard j", 0, 0, 5)
        self.setPlotSize([[1, 0], [0, 1]])

    def plotCurrentBasisVectors(self):
        if not self.toolBoxState.plotCurrentBasisVectors:
            return
        self.vectorUpdated.emit(
            self.basisVector.ix, self.basisVector.iy, "#b300b3", "Current i", 0, 0, 5)
        self.vectorUpdated.emit(
            self.basisVector.jx, self.basisVector.jy, "#29a329", "Current j", 0, 0, 5)
        self.setPlotSize([[self.basisVector.ix, self.basisVector.iy], [
                         self.basisVector.jx, self.basisVector.jy]])

    def plotShape(self):
        if (not self.toolBoxState.drawShape):
            return
        basei = [self.basisVector.ix, self.basisVector.iy]
        basej = [self.basisVector.jx, self.basisVector.jy]
        processedVectors: list[int, int] = []
        for vector in self.vectorList:
            if (not vector.enabled):
                continue
            processedVector = self.service.vectorFromBases(
                iScaler=vector.iScaler, jScaler=vector.jScaler, iBase=basei, jBase=basej)
            processedVectors.append(processedVector)
        self.shapeUpdated.emit(
            processedVectors, self.toolBoxState.fillColor, self.toolBoxState.fillShape)
        self.setPlotSize(processedVectors)

    def clearPlot(self):
        self.plotCleared.emit()

    def refreshPlot(self):
        self.clearPlot()
        self.plotStandardBasisVectors()
        self.plotCurrentBasisVectors()
        self.plotVectors()
        self.plotShape()
