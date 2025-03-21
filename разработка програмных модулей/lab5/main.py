import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btn_get_data = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_data.setGeometry(QtCore.QRect(680, 30, 100, 28))
        self.btn_get_data.setObjectName("btn_get_data")
        self.btn_get_data.clicked.connect(self.get_news)
        
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(680, 70, 100, 28))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_clear.clicked.connect(self.clear_table)
        
        self.news_table = QtWidgets.QTableWidget(self.centralwidget)
        self.news_table.setGeometry(QtCore.QRect(10, 110, 770, 480))
        self.news_table.setObjectName("news_table")
        self.news_table.setColumnCount(2)
        self.news_table.setHorizontalHeaderLabels(['Новости', 'Время'])
        
        Dialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def get_news(self):
        url = 'https://www.infox.ru/archive/2025-03-04#doc349049'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        news_items = soup.find_all('h3')
        time_items = soup.find_all('div', class_='date')

        for i in range(min(len(news_items), len(time_items))):
            rowPosition = self.news_table.rowCount()
            self.news_table.insertRow(rowPosition)
            
            self.news_table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(news_items[i].text.strip()))
            self.news_table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(time_items[i].text.strip()))

    def clear_table(self):
        self.news_table.setRowCount(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новости"))
        self.btn_get_data.setText(_translate("Dialog", "Получить данные"))
        self.btn_clear.setText(_translate("Dialog", "Очистить"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())