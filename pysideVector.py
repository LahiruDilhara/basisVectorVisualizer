import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class VectorDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Triangle Display")
        self.setGeometry(100, 100, 600, 600)

        # Layout
        layout = QVBoxLayout()

        # Create Matplotlib Figure and Canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Button to trigger plot
        self.plot_button = QPushButton("Plot Triangle")
        self.plot_button.clicked.connect(self.plot_triangle)

        # Add to Layout
        layout.addWidget(self.plot_button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_triangle(self):
        # Define three vectors
        v1 = np.array([3, 4])
        v2 = np.array([-2, 1])
        v3 = np.array([1, -3])

        # Clear the previous plot
        self.ax.clear()

        # Plot coordinate axes
        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.axvline(0, color='black', linewidth=1)
        self.ax.grid(True, linestyle="--", alpha=0.5)

        # Plot vectors
        self.ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label="V1")
        self.ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='g', label="V2")
        self.ax.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='b', label="V3")

        # Draw the triangle
        triangle = np.array([v1, v2, v3, v1])
        self.ax.plot(triangle[:, 0], triangle[:, 1], 'k-', linewidth=2, label="Triangle")

        # Set limits
        all_x = [v1[0], v2[0], v3[0]]
        all_y = [v1[1], v2[1], v3[1]]
        self.ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
        self.ax.set_ylim(min(all_y) - 1, max(all_y) + 1)

        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VectorDisplay()
    window.show()
    sys.exit(app.exec())