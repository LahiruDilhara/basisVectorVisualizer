import sqlite3
from ..core.DataTypes import Vector
from ..core.DataTypes import BasisVector


class Database():
    def __init__(self):
        self.conn = sqlite3.connect("plotDatabase.db")
        self.cursor = self.conn.cursor()

        self.initDatabase()

    def initDatabase(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vector(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                jScaler REAL NOT NULL,
                iScaler REAL NOT NULL,
                enabled INTEGER NOT NULL,
                thickness INTEGER NOT NULL,
                color TEXT NOT NULL,
                listOrder INTEGER NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS basis(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ix REAL NOT NULL,
                iy REAL NOT NULL,
                jx REAL NOT NULL,
                jy REAL NOT NULL
            )
        """)
        self.conn.commit()

    def addVectors(self, vectors: list[Vector]):
        for index, vector in enumerate(vectors):
            enabled = 1 if vector.enabled else 0
            self.cursor.execute(
                "INSERT INTO vector (id,name,jScaler,iScaler,enabled,thickness,color,listOrder) VALUES (?,?,?,?,?,?,?,?)", (vector.id, vector.name, vector.jScaler, vector.iScaler, enabled, vector.thickness, vector.color, index))
        self.conn.commit()

    def removeVectorsData(self):
        self.cursor.execute("DELETE FROM vector")

    def getVectors(self) -> list[Vector]:
        self.cursor.execute(
            "SELECT id,name,jScaler,iScaler,enabled,thickness,color FROM vector ORDER BY listOrder")
        rows = self.cursor.fetchall()

        vectors = [Vector(id=row[0], name=row[1], jScaler=row[2], iScaler=row[3],
                          enabled=1 if row[4] == 1 else 0, thickness=row[5], color=row[6]) for row in rows]
        return vectors

    def setBasis(self, basisVector: BasisVector):
        self.cursor.execute("DELETE FROM basis")
        self.cursor.execute("INSERT INTO basis(ix,iy,jx,jy) VALUES (?,?,?,?)",
                            (basisVector.ix, basisVector.iy, basisVector.jx, basisVector.jy))
        self.conn.commit()

    def getBasis(self) -> BasisVector:
        basisVector = BasisVector(1, 0, 0, 1)
        self.cursor.execute("SELECT ix,iy,jx,jy FROM basis")
        rows = self.cursor.fetchall()

        for row in rows:
            basisVector.ix = row[0]
            basisVector.iy = row[1]
            basisVector.jx = row[2]
            basisVector.jy = row[3]

        return basisVector

    def closeConnection(self):
        self.conn.close()
