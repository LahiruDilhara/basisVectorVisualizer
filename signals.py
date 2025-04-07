from PySide6.QtCore import QObject, Signal

class BasisVector(QObject):
    basisVectorChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._valid = True

    def mark_as_invalid(self):
        self._valid = False
        self.deleteLater()

    def emit_signal(self, value):
        if self._valid:
            self.basisVectorChanged.emit(value)
        else:
            print("Attempt to emit signal from a deleted object")

# Test the object emission
basis_vector = BasisVector()
basis_vector.basisVectorChanged.connect(lambda x: print(f"Signal emitted with value {x}"))
basis_vector.emit_signal(4)

basis_vector.mark_as_invalid()  # Mark the object as invalid (deleted)
basis_vector.emit_signal(10)  # Will print "Attempt to emit signal from a de