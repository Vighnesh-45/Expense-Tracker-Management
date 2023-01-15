import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1366, 800))
        self.frame.setStyleSheet("background-color: rgb(9, 21, 30);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(150, 150, 1066, 500))
        self.frame_2.setStyleSheet("background-color: rgb(21, 46, 67);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1071, 501))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
       # self.setColumnWidth(4, 200)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(450, 70, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tab()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        self.tableWidget.setColumnWidth(0, 214)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        self.tableWidget.setColumnWidth(1, 214)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        self.tableWidget.setColumnWidth(2, 214)
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Transaction_Method"))
        self.tableWidget.setColumnWidth(3, 214)
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Type"))
        self.tableWidget.setColumnWidth(4, 214)

        self.label.setText(_translate("MainWindow", "HISTORY"))


    def tab(self):
        try:
            mydb = mc.connect(
                              host="localhost",
                              user="root",
                              password="H@rSHiTR24",
                              database="expense"
                              )
            myc = mydb.cursor()
            qr = "select Date,Description,Amount,Type,Transaction_Method from Transaction where Account_No = 200000002"
            myc.execute(qr)
            result = myc.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,
                                         column_number, QTableWidgetItem(str(data)))
        except mc.Error as e:
            print("Error occured")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
