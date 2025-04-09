from dataclasses import dataclass


@dataclass
class Vector():
    id: int
    name: str
    iScaler: int
    jScaler: int
    enabled: bool
    thickness: int
    color: str


@dataclass
class BasisVector():
    ix: float
    iy: float
    jx: float
    jy: float
