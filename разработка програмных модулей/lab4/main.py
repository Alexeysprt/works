from PyQt5 import QtCore, QtGui, QtWidgets
import json

class InterfaceDataViewer(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.load_json_data()

        self.pushButton.clicked.connect(self.get_data)
        self.pushButton_2.clicked.connect(self.clear_table)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(589, 387)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 10, 160, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 10, 361, 321))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels(["DN", "portT", "Speed", "MTU"])

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Interface Data Viewer"))
        self.pushButton.setText(_translate("Dialog", "Get Data"))
        self.pushButton_2.setText(_translate("Dialog", "Clear Table"))

    def load_json_data(self):
        try:
            with open('exer1-interface-data.json', 'r') as file:
                jsondata = file.read()
                self.json_object = json.loads(jsondata)
        except FileNotFoundError:
            print("File not found!")

    def get_data(self):
        if hasattr(self, 'json_object'):
            self.tableWidget_2.setRowCount(len(self.json_object['imdata']))
            for row, item in enumerate(self.json_object['imdata']):
                dn = item["l1PhysIf"]["attributes"]["dn"]
                portT = item["l1PhysIf"]["attributes"]["portT"]
                speed = item["l1PhysIf"]["attributes"]["speed"]
                mtu = item["l1PhysIf"]["attributes"]["mtu"]
                
                self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(dn)))
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(portT))
                self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(speed))
                self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(mtu))

    def clear_table(self):
        self.tableWidget_2.setRowCount(0)

import sys
app = QtWidgets.QApplication(sys.argv)
dialog = InterfaceDataViewer()
dialog.show()
sys.exit(app.exec_())