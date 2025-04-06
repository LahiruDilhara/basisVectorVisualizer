from dataclasses import dataclass


@dataclass
class Vector():
    id: str
    name: str
    iScaler: int
    jScaler: int
    enabled: bool
    thickness: int
    color: str
