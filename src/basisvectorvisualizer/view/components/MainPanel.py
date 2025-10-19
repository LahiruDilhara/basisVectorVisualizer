from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from ..features import ToolBar, PlotArea
from ..widgets import Column, Row, ToolButton

from ..viewModel.PlotAreaViewModel import PlotAreaViewModel
from ...core.DataTypes import Vector, BasisVector


def MainPanel(plotViewModel: PlotAreaViewModel, toolBarButtons: list[QPushButton] = []):
    return Row.Row(spacing=10, alignment=Qt.AlignmentFlag.AlignTop, subWidgets=[
        Row.RowItem(item=ToolBar.ToolBar(
            spacing=10, alignment=Qt.AlignmentFlag.AlignLeft, toolButtons=toolBarButtons)),
        Row.RowItem(item=PlotArea.PlotArea(plotViewModel), stretch=1),
    ])
