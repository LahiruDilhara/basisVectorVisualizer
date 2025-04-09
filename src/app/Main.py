from .view.pages.MainWindow import MainWindow
import sys
from PySide6.QtWidgets import QApplication

from .view.viewModel import MainWindowViewModel
from .domain.Database import Database


def main():
    app = QApplication(sys.argv)
    database = Database()
    mainViewModel = MainWindowViewModel.MainWindowViewModel(database=database)
    # mainViewModel.setParent(None)
    window = MainWindow(mainViewModel)
    window.show()
    # window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
