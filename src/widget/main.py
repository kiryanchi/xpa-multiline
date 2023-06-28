from PySide6.QtWidgets import QMainWindow, QFileDialog
from openpyxl.utils.exceptions import InvalidFileException

from src.handler.excel import Excel
from src.ui.mainWidget import Ui_MainWindow
from src.ui.tableItemWidget import TableItemWidget
from src.ui.tableWidget import TableWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    excel: Excel

    def __init__(self):
        super().__init__()
        self.tableWidget = TableWidget()
        self.setupUi()

    def setupUi(self, **kwargs):
        super().setupUi(self)
        self.setWindowTitle("XPA 다회선")

        self.frame_image.layout().addWidget(self.tableWidget)

        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save_file)

    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "파일 열기", "", "Excel Files (*.xlsx)")

        try:
            self.excel = Excel(file)
        except InvalidFileException:
            return
        self.load_ui()
        self.load_data()

        self.setWindowTitle(f"XPA 다회선 - {file}")

    def save_file(self):
        file, _ = QFileDialog.getSaveFileName(self, "파일 저장", "", "Excel Files (*.xlsx)")

        self.excel.customer = self.lineEdit_customer.text()
        self.excel.address = self.lineEdit_address.text()

        for c in ['D', 'E', 'F']:
            text = self.tableWidget.cellWidget(0, ord(c) - ord('D')).text.text()
            self.excel.set_text(f"{c}15", text)

            for r in range(1, self.tableWidget.rowCount()):
                text = self.tableWidget.cellWidget(r, ord(c) - ord('D')).text.text()
                self.excel.set_text(f"{c}{r * 2 + 17}", text)

        for c in ['D', 'E', 'F']:
            # 공사 확인
            if f"{c}15" in self.excel.images:
                tableItemWidget: TableItemWidget = self.tableWidget.cellWidget(0, ord(c) - ord('D'))
                if tableItemWidget.imageData:
                    if self.tableWidget.cellWidget(0, ord(c) - ord('D')).imageData != self.excel.images[f"{c}15"]._data():
                        self.excel.set_image(f"{c}15", self.tableWidget.cellWidget(0, ord(c) - ord('D')).imageData)
                else:
                    del self.excel.images[f"{c}15"]
            else:
                if self.tableWidget.cellWidget(0, ord(c) - ord('D')).imageData:
                    self.excel.set_image(f"{c}15", self.tableWidget.cellWidget(0, ord(c) - ord('D')).imageData)

            # 객실별 사진
            for r in range(1, self.tableWidget.rowCount()):
                row = r * 2 + 17
                if f"{c}{row}" in self.excel.images:
                    if self.tableWidget.cellWidget(r, ord(c) - ord('D')).imageData:
                        if self.tableWidget.cellWidget(r, ord(c) - ord('D')).imageData != self.excel.images[f"{c}{row}"]._data():
                            self.excel.set_image(f"{c}{row}", self.tableWidget.cellWidget(r, ord(c) - ord('D')).imageData)
                    else:
                        del self.excel.images[f"{c}{row}"]
                else:
                    if self.tableWidget.cellWidget(r, ord(c) - ord('D')).imageData:
                        self.excel.set_image(f"{c}{row}", self.tableWidget.cellWidget(r, ord(c) - ord('D')).imageData)

        self.excel.save(file)

    def load_ui(self):
        self.tableWidget.setRowCount(self.excel.image_row)

        col = {0: 'D', 1: 'E', 2: 'F'}

        for r in range(self.tableWidget.rowCount()):
            for c in range(self.tableWidget.columnCount()):
                cell = col[c] + (str(r * 2 + 17) if r > 0 else '15')
                self.tableWidget.setCellWidget(r, c, TableItemWidget(self, cell, self.excel.get_text(cell)))

    def load_data(self):
        self.lineEdit_customer.setText(self.excel.customer)
        self.lineEdit_address.setText(self.excel.address)

        for c in ['D', 'E', 'F']:
            # 공사 확인
            if f"{c}15" in self.excel.images:
                image_data = self.excel.images[f"{c}15"]._data()
                self.tableWidget.cellWidget(0, ord(c) - ord('D')).setImage(image_data)

            # 객실별 사진
            for r in range(1, self.tableWidget.rowCount()):
                row = r * 2 + 17
                if f"{c}{row}" in self.excel.images:
                    image_data = self.excel.images[f"{c}{row}"]._data()
                    self.tableWidget.cellWidget(r, ord(c) - ord('D')).setImage(image_data)
