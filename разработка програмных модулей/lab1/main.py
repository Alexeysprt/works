import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow1.ui", self)
        self.pushButton.clicked.connect(self.time)
        self.pushButton_2.clicked.connect(self.champion)
        self.names = ["Валентин", "Вова", "Семен"]

    def time(self):
        print("Произведен подсчет общего времени")
        
        res1 = int(self.lineEdit.text()) + int(self.lineEdit_2.text()) + int(self.lineEdit_3.text())
        self.lineEdit_4.setText(str(res1))

        res2 = int(self.lineEdit_9.text()) + int(self.lineEdit_12.text()) + int(self.lineEdit_10.text())
        self.lineEdit_11.setText(str(res2))

        res3 = int(self.lineEdit_13.text()) + int(self.lineEdit_16.text()) + int(self.lineEdit_14.text())
        self.lineEdit_15.setText(str(res3))

    def champion(self):
        try:
            val1 = int(self.lineEdit_4.text())
            val2 = int(self.lineEdit_11.text())
            val3 = int(self.lineEdit_15.text())
        except ValueError:
            print("Error")
            return
        
        values = [val1, val2, val3]
        
        min_value = min(values)
        min_index = values.index(min_value)
        
        champion_name = self.names[min_index]
        
        self.lineEdit_17.setText(champion_name)
            

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()