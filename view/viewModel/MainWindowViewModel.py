from PySide6.QtCore import QObject, Signal

from ..Types import BasisVector
from ..core.DataTypes import Vector
import copy


class MainWindowViewModel(QObject):
    basisVectorChanged: Signal = Signal(BasisVector)
    # updated vector list, old vector, new vector
    vectorListChanged: Signal = Signal(object, Vector, Vector)

    def __init__(self):
        super().__init__()
        self.basisVector: BasisVector = BasisVector(1, 0, 0, 1)
        self.vectorList: list[Vector] = [
            Vector(1, "v1", 2, 4, True, 5, "red"),
            Vector(2, "v2", 4, 8, True, 50, "green"),
            Vector(4, "v4", 9, 10, False, 10, "yellow"),
            Vector(5, "v5", 14, 25, False, 20, "purple"),
        ]

    def onBasisVectorIxChange(self, value: str):
        newIx = self.intOrDefault(value, self.basisVector.ix)
        if (newIx == self.basisVector.ix):
            return
        self.basisVector.ix = newIx
        self.basisVectorChanged.emit(self.basisVector)

    def onBasisVectorIyChange(self, value: str):
        newIy = self.intOrDefault(value, self.basisVector.iy)
        if (newIy == self.basisVector.iy):
            return
        self.basisVector.iy = newIy
        self.basisVectorChanged.emit(self.basisVector)

    def onBasisVectorJxChange(self, value: str):
        newJx = self.intOrDefault(value, self.basisVector.jx)
        if (newJx == self.basisVector.jx):
            return
        self.basisVector.jx = newJx
        self.basisVectorChanged.emit(self.basisVector)

    def onBasisVectorJyChange(self, value: str):
        newJy = self.intOrDefault(value, self.basisVector.jy)
        if (newJy == self.basisVector.jy):
            return
        self.basisVector.jy = newJy
        self.basisVectorChanged.emit(self.basisVector)

    def intOrDefault(self, value: str, default: int = 0):
        if (str.isdigit(value)):
            return int(value)
        return default

    def onVectorToggle(self, vector: Vector, state: bool):
        oldVector = copy.copy(vector)
        for v in self.vectorList:
            if (v.id == vector.id):
                v.enabled = state
                self.vectorListChanged.emit(self.vectorList, oldVector, v)
                break
