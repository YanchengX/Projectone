from PyQt5 import QtCore, QtGui, QtWidgets


class New_emp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(259, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.inputt.setFont(font)
        self.inputt.setAlignment(QtCore.Qt.AlignCenter)
        self.inputt.setObjectName("inputt")
        self.verticalLayout.addWidget(self.inputt)
        self.neid = QtWidgets.QLabel(self.centralwidget)
        self.neid.setObjectName("neid")
        self.verticalLayout.addWidget(self.neid)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.neproperty = QtWidgets.QLabel(self.centralwidget)
        self.neproperty.setObjectName("neproperty")
        self.verticalLayout.addWidget(self.neproperty)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.nename = QtWidgets.QLabel(self.centralwidget)
        self.nename.setObjectName("nename")
        self.verticalLayout.addWidget(self.nename)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.newemp = QtWidgets.QPushButton(self.centralwidget)
        self.newemp.setObjectName("newemp")
        self.verticalLayout.addWidget(self.newemp)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputt.setText(_translate("MainWindow", "輸入資料"))
        self.neid.setText(_translate("MainWindow", "員工編號:"))
        self.neproperty.setText(_translate("MainWindow", "員工性質:"))
        self.nename.setText(_translate("MainWindow", "員工姓名:"))
        self.newemp.setText(_translate("MainWindow", "新增"))

