import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap
from PIL import Image as PILImage
from fastai.vision.all import *
from pneumologos_ui import Ui_MainWindow


class PneumologosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def upload_xray(self):
       pass

    def analyse_xray(self):
       pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PneumologosApp()
    window.show()
    sys.exit(app.exec())
