from view.pages.MainWindow import MainWindow
import sys
from PySide6.QtWidgets import QApplication

from view.viewModel import MainWindowViewModel


def main():
    app = QApplication(sys.argv)
    mainViewModel = MainWindowViewModel.MainWindowViewModel()
    # mainViewModel.setParent(None)
    window = MainWindow(mainViewModel)
    window.show()
    # window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
