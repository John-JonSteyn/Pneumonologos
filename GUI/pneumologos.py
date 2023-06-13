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
       options = QFileDialog.Options()
       options |= QFileDialog.DontUseNativeDialog
       file_name, _ = QFileDialog.getOpenFileName(self, "Upload X-ray", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
       if file_name:
           pixmap = QPixmap(file_name)
           self.ui.label.setPixmap(pixmap.scaled(691, 691, Qt.AspectRatioMode.KeepAspectRatio))

    def analyse_xray(self):
       pixmap = self.ui.label.pixmap()
       if pixmap:
           img = PILImage.fromqpixmap(pixmap)
           pred, _, probs = self.learn.predict(img)
           self.ui.labelDiagnosis.setText(f"Diagnosis: {pred}")
           self.ui.lcdNumberProbability.display(probs[1])
       else:
           self.ui.labelDiagnosis.setText("Please upload an X-ray first.")
           self.ui.lcdNumberProbability.display(0.0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PneumologosApp()
    window.show()
    sys.exit(app.exec())
