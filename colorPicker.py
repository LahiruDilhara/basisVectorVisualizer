from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QColorDialog
from PySide6.QtGui import QColor
import sys


class ColorChanger(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.button = QPushButton("Click to change color", self)
        self.button.clicked.connect(self.open_color_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.setWindowTitle("Color Picker Example")
        self.resize(300, 200)

    def open_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():  # Ensure a color was selected
            self.button.setStyleSheet(f"background-color: {color.name()};")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorChanger()
    window.show()
    sys.exit(app.exec())
