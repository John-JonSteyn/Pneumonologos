# Form implementation generated from reading ui file 'Pneumologos.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 772)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxControls = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxControls.setGeometry(QtCore.QRect(10, 10, 241, 720))
        self.groupBoxControls.setObjectName("groupBoxControls")
        self.pushButtonUpload = QtWidgets.QPushButton(parent=self.groupBoxControls)
        self.pushButtonUpload.setGeometry(QtCore.QRect(10, 30, 221, 71))
        self.pushButtonUpload.setDefault(True)
        self.pushButtonUpload.setObjectName("pushButtonUpload")
        self.pushButtonAnalyse = QtWidgets.QPushButton(parent=self.groupBoxControls)
        self.pushButtonAnalyse.setGeometry(QtCore.QRect(10, 110, 221, 71))
        self.pushButtonAnalyse.setObjectName("pushButtonAnalyse")
        self.labelDiagnosis = QtWidgets.QLabel(parent=self.groupBoxControls)
        self.labelDiagnosis.setGeometry(QtCore.QRect(20, 300, 201, 101))
        self.labelDiagnosis.setText("")
        self.labelDiagnosis.setWordWrap(True)
        self.labelDiagnosis.setObjectName("labelDiagnosis")
        self.lcdNumberProbability = QtWidgets.QLCDNumber(parent=self.groupBoxControls)
        self.lcdNumberProbability.setGeometry(QtCore.QRect(40, 410, 101, 31))
        self.lcdNumberProbability.setObjectName("lcdNumberProbability")
        self.labelDisclaimer = QtWidgets.QLabel(parent=self.groupBoxControls)
        self.labelDisclaimer.setGeometry(QtCore.QRect(8, 545, 221, 161))
        self.labelDisclaimer.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.labelDisclaimer.setScaledContents(False)
        self.labelDisclaimer.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelDisclaimer.setWordWrap(True)
        self.labelDisclaimer.setObjectName("labelDisclaimer")
        self.groupBoxXRay = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxXRay.setGeometry(QtCore.QRect(259, 10, 681, 720))
        self.groupBoxXRay.setObjectName("groupBoxXRay")
        self.labelXRayDisplay = QtWidgets.QLabel(parent=self.groupBoxXRay)
        self.labelXRayDisplay.setGeometry(QtCore.QRect(10, 20, 691, 691))
        self.labelXRayDisplay.setText("")
        self.labelXRayDisplay.setObjectName("labelXRayDisplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxControls.setTitle(_translate("MainWindow", "CONTROLS"))
        self.pushButtonUpload.setText(_translate("MainWindow", "Upload"))
        self.pushButtonAnalyse.setText(_translate("MainWindow", "Analyse"))
        self.labelDisclaimer.setText(_translate("MainWindow", "Disclaimer: Pneumonologos is a proof of concept program and should not be relied upon for medical diagnosis. The results provided by this program are for informational purposes only and should not substitute professional medical advice. If you have any health concerns or questions regarding pneumonia or any other medical condition, please consult a qualified healthcare professional."))
        self.groupBoxXRay.setTitle(_translate("MainWindow", "XRAY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
