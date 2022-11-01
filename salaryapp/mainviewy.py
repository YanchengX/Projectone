from PyQt5 import QtCore, QtGui, QtWidgets

class MainView(QtWidgets.QMainWindow):
    def __init__(self, modelx):
        super().__init__()
        self.setupUi(self)
        self.modelx = modelx
        self.controller = None
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Account = QtWidgets.QWidget(self.centralwidget)
        self.Account.setGeometry(QtCore.QRect(550, 10, 532, 791))
        self.Account.setObjectName("Account")                           
        self.month = QtWidgets.QLabel(self.Account)
        self.month.setGeometry(QtCore.QRect(100, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.month.setFont(font)
        self.month.setObjectName("month")
        self.year = QtWidgets.QLabel(self.Account)
        self.year.setGeometry(QtCore.QRect(10, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.year.setFont(font)
        self.year.setObjectName("year")
        self.label_9 = QtWidgets.QLabel(self.Account)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 58, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Account)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 61, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Account)
        self.label_11.setGeometry(QtCore.QRect(10, 180, 58, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Account)
        self.label_12.setGeometry(QtCore.QRect(10, 210, 58, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Account)
        self.label_13.setGeometry(QtCore.QRect(10, 270, 58, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Account)
        self.label_14.setGeometry(QtCore.QRect(10, 360, 58, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Account)
        self.label_15.setGeometry(QtCore.QRect(10, 240, 58, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Account)
        self.label_16.setGeometry(QtCore.QRect(10, 450, 58, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Account)
        self.label_17.setGeometry(QtCore.QRect(10, 300, 58, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Account)
        self.label_18.setGeometry(QtCore.QRect(10, 330, 58, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Account)
        self.label_19.setGeometry(QtCore.QRect(10, 390, 58, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Account)
        self.label_20.setGeometry(QtCore.QRect(10, 420, 58, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Account)
        self.label_21.setGeometry(QtCore.QRect(320, 320, 58, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Account)
        self.label_22.setGeometry(QtCore.QRect(320, 350, 58, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.Account)
        self.label_23.setGeometry(QtCore.QRect(320, 380, 58, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Account)
        self.label_24.setGeometry(QtCore.QRect(320, 410, 58, 16))
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.Account)
        self.label_26.setGeometry(QtCore.QRect(10, 570, 58, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.Account)
        self.label_27.setGeometry(QtCore.QRect(320, 140, 58, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Account)
        self.label_28.setGeometry(QtCore.QRect(320, 170, 58, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.Account)
        self.label_29.setGeometry(QtCore.QRect(320, 200, 58, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.Account)
        self.label_30.setGeometry(QtCore.QRect(320, 230, 58, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.Account)
        self.label_31.setGeometry(QtCore.QRect(320, 260, 58, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.Account)
        self.label_32.setGeometry(QtCore.QRect(320, 290, 58, 16))
        self.label_32.setObjectName("label_32")
        self.basicsalary = QtWidgets.QLineEdit(self.Account)
        self.basicsalary.setGeometry(QtCore.QRect(100, 120, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.basicsalary.setFont(font)
        self.basicsalary.setObjectName("basicsalary")
        self.healthfee = QtWidgets.QLineEdit(self.Account)
        self.healthfee.setGeometry(QtCore.QRect(100, 330, 113, 22))
        self.healthfee.setObjectName("healthfee")
        self.sundayovertime = QtWidgets.QLineEdit(self.Account)
        self.sundayovertime.setGeometry(QtCore.QRect(410, 290, 113, 22))
        self.sundayovertime.setObjectName("sundayovertime")
        self.saturdayovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.saturdayovertime_meals.setGeometry(QtCore.QRect(410, 260, 113, 22))
        self.saturdayovertime_meals.setObjectName("saturdayovertime_meals")
        self.mealcall = QtWidgets.QLineEdit(self.Account)
        self.mealcall.setGeometry(QtCore.QRect(100, 420, 113, 22))
        self.mealcall.setObjectName("mealcall")
        self.otherminus = QtWidgets.QLineEdit(self.Account)
        self.otherminus.setGeometry(QtCore.QRect(100, 450, 113, 22))
        self.otherminus.setObjectName("otherminus")
        self.borrow = QtWidgets.QLineEdit(self.Account)
        self.borrow.setGeometry(QtCore.QRect(100, 390, 113, 22))
        self.borrow.setObjectName("borrow")
        self.normalfirstovertime = QtWidgets.QLineEdit(self.Account)
        self.normalfirstovertime.setGeometry(QtCore.QRect(410, 140, 113, 22))
        self.normalfirstovertime.setObjectName("normalfirstovertime")
        self.saturdayovertime = QtWidgets.QLineEdit(self.Account)
        self.saturdayovertime.setGeometry(QtCore.QRect(410, 230, 113, 22))
        self.saturdayovertime.setObjectName("saturdayovertime")
        self.laborpension = QtWidgets.QLineEdit(self.Account)
        self.laborpension.setGeometry(QtCore.QRect(100, 570, 113, 22))
        self.laborpension.setObjectName("laborpension")
        self.workerfee = QtWidgets.QLineEdit(self.Account)
        self.workerfee.setGeometry(QtCore.QRect(100, 300, 113, 22))
        self.workerfee.setObjectName("workerfee")
        self.responsiblebouns = QtWidgets.QLineEdit(self.Account)
        self.responsiblebouns.setGeometry(QtCore.QRect(100, 240, 113, 22))
        self.responsiblebouns.setObjectName("responsiblebouns")
        self.otherplus = QtWidgets.QLineEdit(self.Account)
        self.otherplus.setGeometry(QtCore.QRect(100, 270, 113, 22))
        self.otherplus.setObjectName("otherplus")
        self.dayoff = QtWidgets.QLineEdit(self.Account)
        self.dayoff.setGeometry(QtCore.QRect(100, 360, 113, 22))
        self.dayoff.setObjectName("dayoff")
        self.total_salary = QtWidgets.QLineEdit(self.Account)
        self.total_salary.setGeometry(QtCore.QRect(410, 610, 113, 22))
        self.total_salary.setObjectName("total_salary")
        self.overtimeother = QtWidgets.QLineEdit(self.Account)
        self.overtimeother.setGeometry(QtCore.QRect(410, 410, 113, 22))
        self.overtimeother.setObjectName("overtimeother")
        self.specialovertime = QtWidgets.QLineEdit(self.Account)
        self.specialovertime.setGeometry(QtCore.QRect(410, 350, 113, 22))
        self.specialovertime.setObjectName("specialovertime")
        self.sundayfovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.sundayfovertime_meals.setGeometry(QtCore.QRect(410, 320, 113, 22))
        self.sundayfovertime_meals.setObjectName("sundayfovertime_meals")
        self.specialovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.specialovertime_meals.setGeometry(QtCore.QRect(410, 380, 113, 22))
        self.specialovertime_meals.setObjectName("specialovertime_meals")
        self.normalovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.normalovertime_meals.setGeometry(QtCore.QRect(410, 200, 113, 22))
        self.normalovertime_meals.setObjectName("normalovertime_meals")
        self.allrbouns = QtWidgets.QLineEdit(self.Account)
        self.allrbouns.setGeometry(QtCore.QRect(100, 180, 113, 22))
        self.allrbouns.setObjectName("allrbouns")
        self.normalmeals = QtWidgets.QLineEdit(self.Account)
        self.normalmeals.setGeometry(QtCore.QRect(100, 150, 113, 22))
        self.normalmeals.setObjectName("normalmeals")
        self.openbouns = QtWidgets.QLineEdit(self.Account)
        self.openbouns.setGeometry(QtCore.QRect(100, 210, 113, 22))
        self.openbouns.setObjectName("openbouns")
        self.normalsecondovertime = QtWidgets.QLineEdit(self.Account)
        self.normalsecondovertime.setGeometry(QtCore.QRect(410, 170, 113, 22))
        self.normalsecondovertime.setObjectName("normalsecondovertime")
        self.pushButton_3 = QtWidgets.QPushButton(self.Account)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 730, 93, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Account)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 730, 93, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Account)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 730, 93, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Account)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 730, 93, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_33 = QtWidgets.QLabel(self.Account)
        self.label_33.setGeometry(QtCore.QRect(330, 610, 58, 16))
        self.label_33.setObjectName("label_33")
        self.pushButton_7 = QtWidgets.QPushButton(self.Account)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 0, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.ename_2 = QtWidgets.QLabel(self.Account)
        self.ename_2.setGeometry(QtCore.QRect(310, 30, 58, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ename_2.setFont(font)
        self.ename_2.setObjectName("ename_2")
        self.eid_2 = QtWidgets.QLabel(self.Account)
        self.eid_2.setGeometry(QtCore.QRect(220, 30, 58, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.eid_2.setFont(font)
        self.eid_2.setObjectName("eid_2")
        self.label_36 = QtWidgets.QLabel(self.Account)
        self.label_36.setGeometry(QtCore.QRect(60, 90, 58, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.Account)
        self.label_37.setGeometry(QtCore.QRect(370, 110, 58, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.Account)
        self.label_38.setGeometry(QtCore.QRect(10, 510, 61, 16))
        self.label_38.setObjectName("label_38")
        self.normaltotal = QtWidgets.QLineEdit(self.Account)
        self.normaltotal.setGeometry(QtCore.QRect(100, 510, 113, 22))
        self.normaltotal.setObjectName("normaltotal")
        self.label_39 = QtWidgets.QLabel(self.Account)
        self.label_39.setGeometry(QtCore.QRect(320, 510, 61, 16))
        self.label_39.setObjectName("label_39")
        self.overtimetotal = QtWidgets.QLineEdit(self.Account)
        self.overtimetotal.setGeometry(QtCore.QRect(410, 510, 113, 22))
        self.overtimetotal.setObjectName("overtimetotal")
        self.Show = QtWidgets.QWidget(self.centralwidget)
        self.Show.setGeometry(QtCore.QRect(9, 9, 532, 517))
        self.Show.setObjectName("Show")
        self.Totalpay = QtWidgets.QLabel(self.Show)
        self.Totalpay.setGeometry(QtCore.QRect(0, 490, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Totalpay.setFont(font)
        self.Totalpay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Totalpay.setObjectName("Totalpay")
        self.undoview = QtWidgets.QListView(self.Show)
        self.undoview.setGeometry(QtCore.QRect(0, 0, 531, 231))
        self.undoview.setObjectName("undoview")
        self.doneview = QtWidgets.QListView(self.Show)
        self.doneview.setGeometry(QtCore.QRect(0, 250, 531, 231))
        self.doneview.setObjectName("doneview")
        self.Basic_set = QtWidgets.QWidget(self.centralwidget)
        self.Basic_set.setGeometry(QtCore.QRect(10, 550, 532, 259))
        self.Basic_set.setObjectName("Basic_set")
        self.spectialdayoff = QtWidgets.QLineEdit(self.Basic_set)
        self.spectialdayoff.setGeometry(QtCore.QRect(370, 60, 154, 21))
        self.spectialdayoff.setObjectName("spectialdayoff")
        self.ename = QtWidgets.QLineEdit(self.Basic_set)
        self.ename.setGeometry(QtCore.QRect(80, 100, 154, 21))
        self.ename.setObjectName("ename")
        self.label = QtWidgets.QLabel(self.Basic_set)
        self.label.setGeometry(QtCore.QRect(10, 20, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Basic_set)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Basic_set)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Basic_set)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Basic_set)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Basic_set)
        self.label_6.setGeometry(QtCore.QRect(300, 100, 58, 16))
        self.label_6.setObjectName("label_6")
        self.seniority = QtWidgets.QLineEdit(self.Basic_set)
        self.seniority.setEnabled(True)
        self.seniority.setGeometry(QtCore.QRect(370, 20, 154, 21))
        self.seniority.setObjectName("seniority")
        self.eid = QtWidgets.QLineEdit(self.Basic_set)
        self.eid.setGeometry(QtCore.QRect(80, 20, 154, 21))
        self.eid.setObjectName("eid")
        self.pushButton = QtWidgets.QPushButton(self.Basic_set)
        self.pushButton.setGeometry(QtCore.QRect(330, 190, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Basic_set)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 190, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.basicsalary_2 = QtWidgets.QLineEdit(self.Basic_set)
        self.basicsalary_2.setGeometry(QtCore.QRect(370, 100, 154, 21))
        self.basicsalary_2.setObjectName("basicsalary_2")
        self.eproperty = QtWidgets.QLineEdit(self.Basic_set)
        self.eproperty.setGeometry(QtCore.QRect(80, 60, 154, 21))
        self.eproperty.setObjectName("eproperty")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 25))
        self.menubar.setObjectName("menubar")
        self.menumain = QtWidgets.QMenu(self.menubar)
        self.menumain.setObjectName("menumain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMain = QtWidgets.QAction(MainWindow)
        self.actionMain.setObjectName("actionMain")
        self.actionehistory = QtWidgets.QAction(MainWindow)
        self.actionehistory.setObjectName("actionehistory")
        self.menumain.addSeparator()
        self.menumain.addAction(self.actionMain)
        self.menumain.addAction(self.actionehistory)
        self.menubar.addAction(self.menumain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.month.setText(_translate("MainWindow", "month"))
        self.year.setText(_translate("MainWindow", "year"))
        self.label_9.setText(_translate("MainWindow", "基本底薪"))
        self.label_10.setText(_translate("MainWindow", "伙食津貼"))
        self.label_11.setText(_translate("MainWindow", "全勤獎金"))
        self.label_12.setText(_translate("MainWindow", "開門津貼"))
        self.label_13.setText(_translate("MainWindow", "其他+"))
        self.label_14.setText(_translate("MainWindow", "請假"))
        self.label_15.setText(_translate("MainWindow", "責任津貼"))
        self.label_16.setText(_translate("MainWindow", "其他-"))
        self.label_17.setText(_translate("MainWindow", "勞保費"))
        self.label_18.setText(_translate("MainWindow", "健保費"))
        self.label_19.setText(_translate("MainWindow", "借支"))
        self.label_20.setText(_translate("MainWindow", "代訂伙食"))
        self.label_21.setText(_translate("MainWindow", "休伙食"))
        self.label_22.setText(_translate("MainWindow", "國定加"))
        self.label_23.setText(_translate("MainWindow", "國定伙食"))
        self.label_24.setText(_translate("MainWindow", "加班其他"))
        self.label_26.setText(_translate("MainWindow", "勞退"))
        self.label_27.setText(_translate("MainWindow", "平加1"))
        self.label_28.setText(_translate("MainWindow", "平加2"))
        self.label_29.setText(_translate("MainWindow", "平加伙"))
        self.label_30.setText(_translate("MainWindow", "例假加"))
        self.label_31.setText(_translate("MainWindow", "例加伙食"))
        self.label_32.setText(_translate("MainWindow", "休加"))
        self.basicsalary.setText(_translate("MainWindow", "basicsalary"))
        self.healthfee.setText(_translate("MainWindow", "healthfee"))
        self.sundayovertime.setText(_translate("MainWindow", "sundayovertime"))
        self.saturdayovertime_meals.setText(_translate("MainWindow", "saturdayovertime_meals"))
        self.mealcall.setText(_translate("MainWindow", "mealcall"))
        self.otherminus.setText(_translate("MainWindow", "otherminus"))
        self.borrow.setText(_translate("MainWindow", "borrow"))
        self.normalfirstovertime.setText(_translate("MainWindow", "normalfirstovertime"))
        self.saturdayovertime.setText(_translate("MainWindow", "saturdayovertime"))
        self.laborpension.setText(_translate("MainWindow", "laborpension"))
        self.workerfee.setText(_translate("MainWindow", "workerfee"))
        self.responsiblebouns.setText(_translate("MainWindow", "responsiblebouns"))
        self.otherplus.setText(_translate("MainWindow", "otherplus"))
        self.dayoff.setText(_translate("MainWindow", "dayoff"))
        self.total_salary.setText(_translate("MainWindow", "total_salary"))
        self.overtimeother.setText(_translate("MainWindow", "overtimeother"))
        self.specialovertime.setText(_translate("MainWindow", "specialovertime"))
        self.sundayfovertime_meals.setText(_translate("MainWindow", "sundayfovertime_meals"))
        self.specialovertime_meals.setText(_translate("MainWindow", "specialovertime_meals"))
        self.normalovertime_meals.setText(_translate("MainWindow", "normalovertime_meals"))
        self.allrbouns.setText(_translate("MainWindow", "allrbouns"))
        self.normalmeals.setText(_translate("MainWindow", "normalmeals"))
        self.openbouns.setText(_translate("MainWindow", "openbouns"))
        self.normalsecondovertime.setText(_translate("MainWindow", "normalsecondovertime"))
        self.pushButton_3.setText(_translate("MainWindow", "修改"))
        self.pushButton_4.setText(_translate("MainWindow", "刪除"))
        self.pushButton_5.setText(_translate("MainWindow", "預覽"))
        self.pushButton_6.setText(_translate("MainWindow", "新增"))
        self.label_33.setText(_translate("MainWindow", "本月薪水"))
        self.pushButton_7.setText(_translate("MainWindow", "本月結算"))
        self.ename_2.setText(_translate("MainWindow", "ename"))
        self.eid_2.setText(_translate("MainWindow", "eid"))
        self.label_36.setText(_translate("MainWindow", "normal"))
        self.label_37.setText(_translate("MainWindow", "overtime"))
        self.label_38.setText(_translate("MainWindow", "一般總和"))
        self.normaltotal.setText(_translate("MainWindow", "normaltotal"))
        self.label_39.setText(_translate("MainWindow", "加班總和"))
        self.overtimetotal.setText(_translate("MainWindow", "overtimetotal"))
        self.Totalpay.setText(_translate("MainWindow", "1,000,000,000"))
        self.spectialdayoff.setText(_translate("MainWindow", "spectialdayoff"))
        self.ename.setText(_translate("MainWindow", "ename"))
        self.label.setText(_translate("MainWindow", "員工編號"))
        self.label_2.setText(_translate("MainWindow", "年資"))
        self.label_3.setText(_translate("MainWindow", "員工性質"))
        self.label_4.setText(_translate("MainWindow", "特休"))
        self.label_5.setText(_translate("MainWindow", "員工姓名"))
        self.label_6.setText(_translate("MainWindow", "基本底薪"))
        self.seniority.setText(_translate("MainWindow", "seniority"))
        self.eid.setText(_translate("MainWindow", "eid"))
        self.pushButton.setText(_translate("MainWindow", "修改"))
        self.pushButton_2.setText(_translate("MainWindow", "完成"))
        self.basicsalary_2.setText(_translate("MainWindow", "basicsalary"))
        self.eproperty.setText(_translate("MainWindow", "eproperty"))
        self.menumain.setTitle(_translate("MainWindow", "視窗"))
        self.actionMain.setText(_translate("MainWindow", "setvalue"))
        self.actionehistory.setText(_translate("MainWindow", "ehistory"))

    def show_undoview(self):
        #view禁止編輯
        self.undoview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.undoview.setModel(self.controller.model)
    
    def setcontroller(self, controller):
        self.controller = controller
        #之後來判斷是哪個controller 來進行擴充設定
        self.attachcontroller()

    #依照該controller對應 設定其他按鍵事件連結
    def attachcontroller(self):
        self.pushButton_5.clicked.connect(self.controller.preview)
        
        self.controller.show_undoview()

