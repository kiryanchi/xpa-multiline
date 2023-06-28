from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView


class TableWidget(QTableWidget):
    def __init__(self) -> None:
        super().__init__(0, 3)

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setAcceptDrops(True)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.StrongFocus)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setDefaultSectionSize(self.height() // 3)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.verticalHeader().setDefaultSectionSize(self.height() // 3)
        self.horizontalHeader().setDefaultSectionSize(self.width() // 3)
