from typing import Optional

from PySide6 import QtGui
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QSizePolicy


class TableItemWidget(QWidget):
    imageData: Optional[bytes] = None
    text: QLineEdit
    image: QLabel
    cell: str

    def __init__(self, main, cell, text: str):
        super().__init__()
        self.main = main
        self.cell = cell

        self.text = QLineEdit(text)
        self.image = QLabel("이미지")
        self.image.setScaledContents(True)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setAcceptDrops(True)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.text)
        self.layout().addWidget(self.image)

    def setImage(self, data: bytes):
        self.imageData = data
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(data))
        self.image.setPixmap(pixmap)

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

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if event.mimeData().hasUrls():
            extension = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']
            url = event.mimeData().urls()[0].toLocalFile()
            if url.split('.')[-1] in extension:
                with open(url, 'rb') as f:
                    data = f.read()
                    self.setImage(data)
