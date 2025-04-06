from view.MainWindow import MainWindow
import sys
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
