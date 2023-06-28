from PySide6.QtWidgets import QApplication

from src.widget.main import MainWindow


def start():
    app = QApplication([])
    main = MainWindow()
    main.show()
    app.exec()


if __name__ == "__main__":
    start()
