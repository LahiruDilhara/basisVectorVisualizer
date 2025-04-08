import sqlite3
from ..core.DataTypes import Vector


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
                color TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def addVectors(self, vectors: list[Vector]):
        for vector in vectors:
            enabled = 1 if vector.enabled else 0
            self.cursor.execute(
                "INSERT INTO vector (id,name,jScaler,iScaler,enabled,thickness,color) VALUES (?,?,?,?,?,?,?)", (vector.id, vector.name, vector.jScaler, vector.iScaler, enabled, vector.thickness, vector.color))
        self.conn.commit()

    def removeData(self):
        self.cursor.execute("DELETE FROM vector")

    def getVectors(self) -> list[Vector]:
        self.cursor.execute(
            "SELECT id,name,jScaler,iScaler,enabled,thickness,color FROM vector")
        rows = self.cursor.fetchall()

        vectors = [Vector(id=row[0], name=row[1], jScaler=row[2], iScaler=row[3],
                          enabled=1 if row[4] == 1 else 0, thickness=row[5], color=row[6]) for row in rows]
        return vectors

    def closeConnection(self):
        self.conn.close()
