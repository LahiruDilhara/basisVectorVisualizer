from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLayout, QHBoxLayout, QFrame, QLabel, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from ..widgets import Column, HorizontalLabeledCard, LabeledInput, Row, sidePanelButton, VerticalLabeledCard, ScrollCard
from ..features import BasisVectorInput, SidePaneltButtonSet, SidePanelVectorList
from typing import Callable

from ..core.DataTypes import Vector


class SidePanel(QWidget):
    def __init__(self, basisVectorInputSpec: BasisVectorInput.BasisVectorInputSpec, sidePanelButtonSetSpec: list[SidePaneltButtonSet.SidePanelButtonSpec], vectorList: list[Vector], onVectorToggle: Callable[[Vector, bool], None] = None):
        super().__init__()
        self.layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.basisVectorInputSpec = basisVectorInputSpec
        self.sidePanelButtonSetSpec = sidePanelButtonSetSpec
        self.vectorList = vectorList
        self.onVectorToggle = onVectorToggle

        self.initUi()

    def initUi(self):
        # Create Side Panel Title
        title_label = QLabel("Plot Configuration")
        title_label.setFont(QFont("Arial", 18, weight=QFont.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(
            "padding: 10px; background-color: white; border-radius: 8px;")

        # Create Basis Vector Secion
        basisVectorFeature = BasisVectorInput.BasisVectorInput(
            self.basisVectorInputSpec)

        # Create Vector List Secion
        vectorListFeature = SidePanelVectorList.SidePanelVectorList(
            vectorList=self.vectorList, onToggle=self.onVectorToggle)
        scrollableVectorList = ScrollCard.ScrollCard(
            vectorListFeature, resizable=True)

        # Create SidePanel Button Secion
        sidePanelButtonFeature = SidePaneltButtonSet.SidePanelButtonSet(
            self.sidePanelButtonSetSpec, spacing=10)

        # Create Row

        row = Row.Row(spacing=20, alignment=Qt.AlignmentFlag.AlignTop, subWidgets=[
            Row.RowItem(title_label),
            Row.RowItem(basisVectorFeature),
            Row.RowItem(scrollableVectorList, 1),
            Row.RowItem(sidePanelButtonFeature)
        ])
        self.layout.addWidget(row)
