import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from PIL import Image as PILImage
from PIL import Image
from fastai.vision.all import *
from pneumologos_ui import Ui_MainWindow


class ImageProcessor:
    def __init__(self, model_path):
        self.model = load_learner(model_path)

    def process_image(self, img_path):
        try:
            img = Image.open(img_path)
            img = img.resize((224, 224))  # Resize image to a fixed size
            pred, _, probs = self.model.predict(img)
            return pred, float(probs[1])
        except Exception as e:
            # Handle any exceptions that may occur during image processing
            print(f"An error occurred during image processing: {e}")
            return None, None


class PneumologosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonUpload.clicked.connect(self.upload_xray)
        self.ui.pushButtonAnalyse.clicked.connect(self.analyse_xray)
        self.image_path = ""
        self.image_processor = ImageProcessor("currentModel.pkl")

    def upload_xray(self):
        options = (
            QFileDialog.Option.ReadOnly | QFileDialog.Option.DontUseNativeDialog
        )
        file_dialog = QFileDialog(
            self,
            "Upload X-ray",
            "",
            "JPEG Files (*.jpeg *.jpg);;All Files (*)",
            options=QFileDialog.Option(options),
        )
        file_dialog.fileSelected.connect(self.handle_file_selection)
        file_dialog.show()

    def handle_file_selection(self, file_name):
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

            # Update progress bar
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
        else:
            self.ui.labelXRayDisplay.setText("No image selected.")
            self.image_path = ""

    def analyse_xray(self):
        if self.image_path:
            self.ui.progressBarAnalyse.setValue(0)
            self.ui.pushButtonAnalyse.setEnabled(False)  # Disable the button during analysis

            # Process the image
            pred, probability = self.image_processor.process_image(self.image_path)

            # Update progress bar
            self.ui.progressBarAnalyse.setValue(100)

            if pred is not None and probability is not None:
                self.ui.labelDiagnosis.setText(f"Diagnosis: {pred}")
                self.ui.lcdNumberProbability.display(probability)
            else:
                # Show an error message if image processing fails
                QMessageBox.critical(
                    self,
                    "Error",
                    "An error occurred during image analysis.",
                    QMessageBox.StandardButton.Ok,
                )

            self.ui.pushButtonAnalyse.setEnabled(True)  # Re-enable the button after analysis
        else:
            self.ui.labelDiagnosis.setText("Please upload an X-ray first.")
            self.ui.lcdNumberProbability.display(0.0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PneumologosApp()
    window.show()
    sys.exit(app.exec())
