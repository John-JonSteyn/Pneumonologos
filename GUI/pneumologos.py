import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap
from PIL import Image as PILImage
from PIL import Image
from fastai.vision.all import *
from pneumologos_ui import Ui_MainWindow


class PneumologosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonUpload.clicked.connect(self.upload_xray)
        self.ui.pushButtonAnalyse.clicked.connect(self.analyse_xray)
        self.image_path = ""

    def upload_xray(self):
        options = QFileDialog.Option(QFileDialog.Option.ReadOnly | QFileDialog.Option.DontUseNativeDialog)
        file_dialog = QFileDialog(self, "Upload X-ray", "", "JPEG Files (*.jpeg *.jpg);;All Files (*)", options=QFileDialog.Option(options))
        file_dialog.fileSelected.connect(self.process_selected_file)
        file_dialog.show()

    def process_selected_file(self, file_name):
        if file_name:
            pixmap = QPixmap(file_name)
            self.ui.labelXRayDisplay.setPixmap(
                pixmap.scaled(691, 691, Qt.AspectRatioMode.KeepAspectRatio)
            )
            self.image_path = file_name
            
            # Reset diagnosis, progress bar, and LCD
            self.ui.labelDiagnosis.setText("Diagnosis: Not Diagnosed")
            self.ui.progressBarAnalyse.setValue(0)
            self.ui.lcdNumberProbability.display(0.0)
        else:
            self.ui.labelXRayDisplay.setText("No image selected.")
            self.image_path = ""

        # Update progress bar
        if file_name:
            total_size = os.path.getsize(file_name)
            chunk_size = 1024 * 1024  # 1 MB
            with open(file_name, "rb") as file:
                uploaded_size = 0
                while True:
                    data = file.read(chunk_size)
                    if not data:
                        break
                    # Process the chunk (e.g., upload to a server)
                    uploaded_size += len(data)
                    progress = int(uploaded_size / total_size * 100)
                    self.ui.progressBarUpload.setValue(progress)

    def analyse_xray(self):
        if self.image_path:
            img = Image.open(self.image_path)
            img = img.resize((224, 224))  # Resize image to a fixed size
            learn = load_learner("currentModel.pkl")
            
            # Update progressBarAnalyse
            self.ui.progressBarAnalyse.setValue(0)
            
            # Evaluate the image
            pred, _, probs = learn.predict(img)
            
            # Update progress bar to completion
            self.ui.progressBarAnalyse.setValue(100)
            
            self.ui.labelDiagnosis.setText(f"Diagnosis: {pred}")
            self.ui.lcdNumberProbability.display(float(probs[1]))
        else:
            self.ui.labelDiagnosis.setText("Please upload an X-ray first.")
            self.ui.lcdNumberProbability.display(0.0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PneumologosApp()
    window.show()
    sys.exit(app.exec())
