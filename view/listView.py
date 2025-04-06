from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List Display Example")
        self.setGeometry(100, 100, 300, 300)

        # Layout
        layout = QVBoxLayout()

        # Create a QListWidget to display list items
        self.listWidget = QListWidget()

        # Add items to the list
        self.listWidget.addItem("Item 1")
        self.listWidget.addItem("Item 2")
        self.listWidget.addItem("Item 3")

        # Add the list widget to the layout
        layout.addWidget(self.listWidget)

        # Button to clear the list
        clear_button = QPushButton("Clear List")
        clear_button.clicked.connect(self.clearList)
        layout.addWidget(clear_button)

        self.setLayout(layout)

    def clearList(self):
        # Clear all items in the list
        self.listWidget.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()