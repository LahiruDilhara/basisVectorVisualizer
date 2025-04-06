from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


def PlotArea():
    # Set Main Plot Area Layout
    plotArea = QWidget()
    main_plot_layout = QVBoxLayout()
    # main_plot_layout.addStretch()
    plotArea.setLayout(main_plot_layout)

    # Create Matplotlib Figure and Canvas
    figure, ax = plt.subplots()
    canvas = FigureCanvas(figure)

    # Add the canvas to the main plot area
    main_plot_layout.addWidget(canvas)
    plotArea.setStyleSheet(
        "background-color: #ffffff; border-left: 2px solid #ccc;")

    return plotArea
