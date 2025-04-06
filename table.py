from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PySide6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create layout
        layout = QVBoxLayout()

        # Create QTableWidget (you can also use QTableView if you prefer)
        table = QTableWidget()
        table.setRowCount(3)  # 3 rows
        table.setColumnCount(3)  # 3 columns

        # Hide gridlines and headers
        table.setShowGrid(False)  # Hides the gridlines
        table.horizontalHeader().setVisible(False)  # Hides the column headers
        table.verticalHeader().setVisible(False)  # Hides the row headers

        # Add content to cells
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f"Item {row + 1},{col + 1}")
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Align text to center
                table.setItem(row, col, item)

        # Add table to layout
        layout.addWidget(table)
        
        # Set layout to window
        self.setLayout(layout)
        self.setWindowTitle("Table Without Borders")
        self.setGeometry(100, 100, 400, 300)

# Run the application
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())