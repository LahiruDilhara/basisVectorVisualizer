from .view.pages.MainWindow import MainWindow
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from .view.viewModel import MainWindowViewModel
from .domain.Database import Database


def main():
    app = QApplication(sys.argv)

    # Set application configurations
    app.setWindowIcon(QIcon("assets/icons/icons8-vector-96.png"))
    app.setDesktopFileName("Base Vector")

    database = Database()
    mainViewModel = MainWindowViewModel.MainWindowViewModel(database=database)
    # mainViewModel.setParent(None)
    window = MainWindow(mainViewModel)
    window.show()
    # window.showMaximized()
    sys.exit(app.exec())

