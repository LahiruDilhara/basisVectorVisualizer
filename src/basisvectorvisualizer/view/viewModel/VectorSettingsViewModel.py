from PySide6.QtCore import QObject, Signal

from ..Types import ToolBoxState
from ...core.DataTypes import Vector, BasisVector
from typing import Callable
import copy


class VectorSettingsViewModel(QObject):

    def __init__(self):
        super().__init__()
        self.name = "vector name"
        self.iScaler = 0.0
        self.jScaler = 0.0
        self.thickness = 1
        self.color = "#4CAF50"
        self.enabled = True

    def setName(self, value):
        self.name = value

    def setIScaler(self, value):
        self.iScaler = value

    def setJScaler(self, value):
        self.jScaler = value

    def setThickness(self, value):
        self.thickness = value

    def setColor(self, value):
        self.color = value

    def setEnabled(self, value):
        self.enabled = value

    def addVector(self, setVector: Callable[[Vector], None]):
        vector = Vector(id=0, name=self.name, iScaler=self.iScaler, jScaler=self.jScaler,
                        enabled=self.enabled, thickness=self.thickness, color=self.color)
        if not self.validateVector(vector):
            return

        setVector(vector)

    def validateVector(self, vector: Vector) -> bool:
        if (vector.thickness <= 0):
            return False
        if (len(vector.name) <= 1):
            return False
        if (len(vector.color) <= 2):
            return False
        return True
