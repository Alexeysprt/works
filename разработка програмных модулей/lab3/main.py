from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import openpyxl
from docxtpl import DocxTemplate

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        
        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)

        
        self.lineEdit1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.verticalLayout.addWidget(self.lineEdit1)

        
        self.pushButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.verticalLayout.addWidget(self.pushButton1)

        
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)

        
        self.lineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.verticalLayout.addWidget(self.lineEdit2)

        
        self.pushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout.addWidget(self.pushButton2)

        
        self.label3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.verticalLayout.addWidget(self.label3)

        
        self.lineEdit3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit3.setObjectName("lineEdit3")
        self.verticalLayout.addWidget(self.lineEdit3)

       
        self.pushButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton3.setObjectName("pushButton3")
        self.verticalLayout.addWidget(self.pushButton3)

       
        self.pushButton4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton4.setObjectName("pushButton4")
        self.verticalLayout.addWidget(self.pushButton4)

      
        self.pushButton5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton5.setObjectName("pushButton5")
        self.verticalLayout.addWidget(self.pushButton5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Программа заполнения документов"))
        self.label1.setText(_translate("Dialog", "Путь к шаблону"))
        self.pushButton1.setText(_translate("Dialog", "Выбрать"))
        self.label2.setText(_translate("Dialog", "Путь к данным Excel"))
        self.pushButton2.setText(_translate("Dialog", "Выбрать"))
        self.label3.setText(_translate("Dialog", "Место сохранения"))
        self.pushButton3.setText(_translate("Dialog", "Выбрать"))
        self.pushButton4.setText(_translate("Dialog", "Выполнить"))
        self.pushButton5.setText(_translate("Dialog", "Выйти"))


class MainWindow(Ui_Dialog, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    
        self.pushButton1.clicked.connect(self.select_template_file)
        self.pushButton2.clicked.connect(self.select_excel_file)
        self.pushButton3.clicked.connect(self.select_output_directory)
        self.pushButton4.clicked.connect(self.process_data)
        self.pushButton5.clicked.connect(self.close)

    def select_template_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл шаблона", "", "Документы Word (*.docx)")
        if file_name:
            self.lineEdit1.setText(file_name)

    def select_excel_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл Excel", "", "Файлы Excel (*.xlsx *.xls)")
        if file_name:
            self.lineEdit2.setText(file_name)

    def select_output_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Выберите папку для сохранения файлов")
        if directory:
            self.lineEdit3.setText(directory)

    def process_data(self):
        template_path = self.lineEdit1.text()
        excel_path = self.lineEdit2.text()
        output_dir = self.lineEdit3.text()

        wb = openpyxl.load_workbook(excel_path)
        ws = wb.active
        data = []
        for row in ws.iter_rows(min_row=2):
                data.append({
                    'var': row[0].value,
                    'sar': row[1].value,
                    'gar': row[2].value
                })
        print(data)
        template = DocxTemplate(template_path)
        for i, record in enumerate(data):
                template.render(record)
                filename = f"{output_dir}/result_{i + 1}.docx"
                template.save(filename)
                print(f"Сохранён файл: {filename}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()