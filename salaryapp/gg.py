# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 415)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_netprice = QtWidgets.QLabel(self.centralwidget)
        self.label_netprice.setGeometry(QtCore.QRect(260, 282, 421, 41))
        self.label_netprice.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_netprice.setText("")
        self.label_netprice.setObjectName("label_netprice")

        self.doubleSpinBox_price = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_price.setGeometry(QtCore.QRect(260, 60, 421, 41))
        self.doubleSpinBox_price.setObjectName("doubleSpinBox_price")
        ####################################
        # Link to function when value changes
        self.doubleSpinBox_price.valueChanged.connect(self.Refresh)
        ####################################

        self.doubleSpinBox_discount = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_discount.setGeometry(QtCore.QRect(260, 160, 421, 41))
        self.doubleSpinBox_discount.setObjectName("doubleSpinBox_discount")
        ####################################
        # Link to function when value changes
        self.doubleSpinBox_discount.valueChanged.connect(self.Refresh)
        ####################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Price:"))
        self.label_2.setText(_translate("MainWindow", "Discount:"))
        self.label_3.setText(_translate("MainWindow", "Net Price:"))

    ##########################################
    # Function for refreshing the output label
    def Refresh(self):
        price = self.doubleSpinBox_price.value()
        discount = self.doubleSpinBox_discount.value()
        netprice = price * (1 - discount)
        self.label_netprice.setText(str(netprice))
    ##########################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())