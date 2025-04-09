from ..core.DataTypes import Vector
import numpy as np


class VectorService():
    def __init__(self):
        pass

    def vectorFromBases(self, iScaler: int, jScaler: int, iBase: list[int, int], jBase: list[int, int]) -> np.ndarray[int, int]:
        iBaseVector = np.array(iBase)
        jBaseVector = np.array(jBase)

        return iBaseVector * iScaler + jBaseVector * jScaler
