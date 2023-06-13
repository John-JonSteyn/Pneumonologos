import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from pneumologos_ui import Ui_MainWindow
from fastai.vision.all import *

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
