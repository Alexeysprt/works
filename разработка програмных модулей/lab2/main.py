import os
import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from form_lab2 import Ui_Form

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.open.clicked.connect(self.open_file)

    def open_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Выберите файл', '', 'Все файлы (*.*)'
        )
        if file_path:
            filename = os.path.basename(file_path)
            extension = os.path.splitext(filename)[1]
            creation_time = os.path.getctime(file_path)
            modification_time = os.path.getmtime(file_path)
            creation_time_str = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            modification_time_str = datetime.datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

            self.label_7.setText(filename)
            self.label_8.setText(extension)
            self.label_9.setText(creation_time_str)
            self.label_10.setText(modification_time_str)
            self.label_6.setText('Автор')

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())