import os

UI_DIR = "./src/ui"
WIDGET_DIR = "./src/widget"


def _convert(ui):
    os.system(f"pyside6-uic {ui}.ui -o {ui}.py")


def convert():
    for ui in os.listdir(UI_DIR):
        if ui.endswith(".ui"):
            _convert(os.path.join(UI_DIR, ui[:-3]))


if __name__ == '__main__':
    convert()
