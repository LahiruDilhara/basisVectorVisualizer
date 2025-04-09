from PySide6.QtCore import QObject, Signal, QTimer

from ..Types import  ToolBoxState
from ...core.DataTypes import Vector,BasisVector
from ...domain.Database import Database
import copy


class MainWindowViewModel(QObject):

    basisVectorChanged: Signal = Signal(BasisVector)
    # updated vector list, old vector, new vector
    vectorListChanged: Signal = Signal(object)

    toolBoxStateChanged: Signal = Signal(ToolBoxState)

    plotVectors: Signal = Signal(BasisVector)

    def __init__(self, database: Database):
        super().__init__()
        self.basisVector: BasisVector = BasisVector(1, 0, 0, 1)
        self.database = database
        self.vectorList: list[Vector] = []
        self.toolBoxState: ToolBoxState = ToolBoxState(
            plotVectors=False, plotStandardBasisVectors=False, plotCurrentBasisVectors=False, drawShape=False, fillShape=False, fillColor="#4CAF50")

        self.initDatabase()

    def initDatabase(self):
        self.vectorList = self.database.getVectors()
        self.basisVector = self.database.getBasis()

        # QTimer.singleShot(
        #     0, lambda: self.basisVectorChanged.emit(self.basisVector))
        # QTimer.singleShot(
        #     0, lambda: self.vectorListChanged.emit(self.vectorList))

    def onSave(self):
        self.database.removeVectorsData()
        self.database.addVectors(self.vectorList)
        self.database.setBasis(self.basisVector)

    def onBasisVectorIxChange(self, value: str):
        newIx = self.floatOrDefault(value, self.basisVector.ix)
        if (newIx == self.basisVector.ix):
            return
        self.basisVector.ix = newIx
        self.basisVectorChanged.emit(self.basisVector)

    def onBasisVectorIyChange(self, value: str):
        newIy = self.floatOrDefault(value, self.basisVector.iy)
        if (newIy == self.basisVector.iy):
            return
        self.basisVector.iy = newIy
        self.basisVectorChanged.emit(self.basisVector)

    def onBasisVectorJxChange(self, value: str):
        newJx = self.floatOrDefault(value, self.basisVector.jx)
        if (newJx == self.basisVector.jx):
            return
        self.basisVector.jx = newJx
        self.basisVectorChanged.emit(self.basisVector)

    def onBasisVectorJyChange(self, value: str):
        newJy = self.floatOrDefault(value, self.basisVector.jy)
        if (newJy == self.basisVector.jy):
            return
        self.basisVector.jy = newJy
        self.basisVectorChanged.emit(self.basisVector)

    def intOrDefault(self, value: str, default: int = 0):
        stripedValue = value.strip("-")
        if (str.isdigit(stripedValue)):
            return int(value)
        return default

    def floatOrDefault(self, value: str, default: float = 0):
        try:
            fValue = float(value)
            return fValue
        except:
            return default

    def onVectorToggle(self, vector: Vector, state: bool):
        for v in self.vectorList:
            if (v.id == vector.id):
                v.enabled = state
                self.vectorListChanged.emit(self.vectorList)
                break

    def onVectorDelete(self, id: str):
        for index, vector in enumerate(self.vectorList):
            if (vector.id == id):
                self.vectorList.pop(index)
                break

        self.vectorListChanged.emit(self.vectorList)

    def onVectorMoveUp(self, id: str):
        index = -1

        for i, vector in enumerate(self.vectorList):
            if (vector.id == id):
                index = i
                break

        if (index == -1):
            return

        if (index > 0):
            item = self.vectorList.pop(index)
            self.vectorList.insert(index - 1, item)

        self.vectorListChanged.emit(self.vectorList)

    def onVectorMoveDown(self, id: str):
        index = -1

        for i, vector in enumerate(self.vectorList):
            if (vector.id == id):
                index = i
                break

        if (index == -1):
            return

        if (index < len(self.vectorList) - 1):
            item = self.vectorList.pop(index)
            self.vectorList.insert(index + 1, item)

        self.vectorListChanged.emit(self.vectorList)

    def onVectorAdd(self, vector: Vector):
        if (vector in self.vectorList or vector == None):
            return
        id = self.getId()
        vector.id = id
        self.vectorList.append(vector)
        self.vectorListChanged.emit(self.vectorList)

    def onPlotVectorToolToggle(self, state: bool):
        if (state == self.toolBoxState.plotVectors):
            return
        self.toolBoxState.plotVectors = state
        self.toolBoxStateChanged.emit(self.toolBoxState)

    def onPlotStandardBasisVectorsToolToggle(self, state: bool):
        if (state == self.toolBoxState.plotStandardBasisVectors):
            return
        self.toolBoxState.plotStandardBasisVectors = state
        self.toolBoxStateChanged.emit(self.toolBoxState)

    def onPlotCurrentBasisVectorsToolToggle(self, state: bool):
        if (state == self.toolBoxState.plotCurrentBasisVectors):
            return
        self.toolBoxState.plotCurrentBasisVectors = state
        self.toolBoxStateChanged.emit(self.toolBoxState)

    def onDrawShapeToolToggle(self, state: bool):
        if (state == self.toolBoxState.drawShape):
            return
        self.toolBoxState.drawShape = state
        self.toolBoxStateChanged.emit(self.toolBoxState)

    def onFillShapeToolToggle(self, state: bool):
        if (state == self.toolBoxState.fillShape):
            return
        self.toolBoxState.fillShape = state
        self.toolBoxStateChanged.emit(self.toolBoxState)

    def onFillColorToolToggle(self, color: str):
        if (color == self.toolBoxState.fillColor):
            return
        self.toolBoxState.fillColor = color
        self.toolBoxStateChanged.emit(self.toolBoxState)

    def getId(self):
        max = -1
        for i in self.vectorList:
            if (i.id > max):
                max = i.id
        return max + 1

    def emitPlotVectors(self):
        pass
