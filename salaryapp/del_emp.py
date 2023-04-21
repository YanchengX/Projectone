from PyQt5 import QtCore, QtGui, QtWidgets


class Del_emp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(150, 150)
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
        self.dcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dcomboBox.setObjectName("dcomboBox")
        self.verticalLayout.addWidget(self.dcomboBox)
        self.delbutton = QtWidgets.QPushButton(self.centralwidget)
        self.delbutton.setObjectName("delbutton")
        self.verticalLayout.addWidget(self.delbutton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputt.setText(_translate("MainWindow", "刪除員工"))
        self.neid.setText(_translate("MainWindow", "員工編號:"))
        self.delbutton.setText(_translate("MainWindow", "刪除"))
