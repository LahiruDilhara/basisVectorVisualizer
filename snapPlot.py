import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create Matplotlib figure
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Create a QLabel to display coordinates
        self.coord_label = QLabel("Mouse Coordinates: ( , )")

        # Layout for Matplotlib and QLabel
        layout = QVBoxLayout()
        layout.addWidget(NavigationToolbar(self.canvas, self))  # Toolbar
        layout.addWidget(self.canvas)
        layout.addWidget(self.coord_label)
        self.setLayout(layout)

        # Define some vector points to snap to
        self.points = [(0, 10), (1, 20), (2, 25), (3, 30)]
        self.x, self.y = zip(*self.points)
        
        # Plot vector points
        self.ax.plot(self.x, self.y, marker="o", linestyle=" ", color="red")

        # Add a label for each point
        for i, point in enumerate(self.points):
            self.ax.text(point[0], point[1], f"({point[0]},{point[1]})", fontsize=12, ha="right", color="black")
        
        self.canvas.draw()

        # Connect mouse movement event
        self.canvas.mpl_connect("motion_notify_event", self.mouse_move_event)

    def mouse_move_event(self, event):
        """Update coordinates and display nearest point."""
        if event.xdata is not None and event.ydata is not None:
            # Snap to the nearest point
            nearest_point = self.snap_to_point(event.xdata, event.ydata)

            # Update the label to display the coordinates
            self.coord_label.setText(f"Mouse Coordinates: ({nearest_point[0]:.2f}, {nearest_point[1]:.2f})")
            
            # Remove all previous text annotations
            for text in self.ax.texts:
                text.remove()

            # Add new annotations for the points
            for point in self.points:
                self.ax.text(point[0], point[1], f"({point[0]},{point[1]})", fontsize=12, ha="right", color="black")

            # Display the snapped point with updated coordinates
            self.ax.text(nearest_point[0], nearest_point[1], f"Snapped: ({nearest_point[0]:.2f}, {nearest_point[1]:.2f})", 
                         fontsize=12, ha="left", color="blue", fontweight="bold")

            self.canvas.draw()

    def snap_to_point(self, x, y):
        """Find the nearest point from the list of vector points."""
        min_distance = float('inf')
        nearest_point = None

        for (px, py) in self.points:
            distance = ((x - px) ** 2 + (y - py) ** 2) ** 0.5  # Euclidean distance
            if distance < min_distance:
                min_distance = distance
                nearest_point = (px, py)
        
        return nearest_point

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matplotlib Mouse Snap Coordinates")
        self.setGeometry(100, 100, 800, 600)

        self.matplotlib_widget = MatplotlibWidget()
        self.setCentralWidget(self.matplotlib_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())