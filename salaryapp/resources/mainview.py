# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainview.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.undoview.setGeometry(QtCore.QRect(0, 0, 531, 481))
        self.undoview.setObjectName("undoview")
        self.Basic_set = QtWidgets.QWidget(self.centralwidget)
        self.Basic_set.setGeometry(QtCore.QRect(10, 540, 531, 259))
        self.Basic_set.setObjectName("Basic_set")
        self.spectialdayoff = QtWidgets.QLineEdit(self.Basic_set)
        self.spectialdayoff.setGeometry(QtCore.QRect(370, 60, 154, 21))
        self.spectialdayoff.setText("")
        self.spectialdayoff.setObjectName("spectialdayoff")
        self.ename = QtWidgets.QLineEdit(self.Basic_set)
        self.ename.setGeometry(QtCore.QRect(80, 100, 154, 21))
        self.ename.setText("")
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
        self.seniority.setText("")
        self.seniority.setObjectName("seniority")
        self.eid = QtWidgets.QLineEdit(self.Basic_set)
        self.eid.setGeometry(QtCore.QRect(80, 20, 154, 21))
        self.eid.setText("")
        self.eid.setObjectName("eid")
        self.pushButton = QtWidgets.QPushButton(self.Basic_set)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Basic_set)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 180, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.basicsalary_2 = QtWidgets.QLineEdit(self.Basic_set)
        self.basicsalary_2.setGeometry(QtCore.QRect(370, 100, 154, 21))
        self.basicsalary_2.setText("")
        self.basicsalary_2.setObjectName("basicsalary_2")
        self.eproperty = QtWidgets.QLineEdit(self.Basic_set)
        self.eproperty.setGeometry(QtCore.QRect(80, 60, 154, 21))
        self.eproperty.setText("")
        self.eproperty.setObjectName("eproperty")
        self.line_2 = QtWidgets.QFrame(self.Basic_set)
        self.line_2.setGeometry(QtCore.QRect(10, 0, 541, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.Basic_set)
        self.line_4.setGeometry(QtCore.QRect(0, 10, 16, 221))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.Basic_set)
        self.line_3.setGeometry(QtCore.QRect(520, 10, 20, 221))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.Basic_set)
        self.line_5.setGeometry(QtCore.QRect(10, 220, 521, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Account = QtWidgets.QWidget(self.centralwidget)
        self.Account.setGeometry(QtCore.QRect(550, 10, 532, 791))
        self.Account.setObjectName("Account")
        self.month = QtWidgets.QLabel(self.Account)
        self.month.setGeometry(QtCore.QRect(140, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.month.setFont(font)
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.month.setObjectName("month")
        self.year = QtWidgets.QLabel(self.Account)
        self.year.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.year.setFont(font)
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.label_9 = QtWidgets.QLabel(self.Account)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 58, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Account)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 61, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Account)
        self.label_11.setGeometry(QtCore.QRect(10, 410, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Account)
        self.label_12.setGeometry(QtCore.QRect(10, 180, 58, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Account)
        self.label_13.setGeometry(QtCore.QRect(10, 240, 58, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Account)
        self.label_14.setGeometry(QtCore.QRect(10, 270, 58, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Account)
        self.label_15.setGeometry(QtCore.QRect(10, 210, 58, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Account)
        self.label_16.setGeometry(QtCore.QRect(10, 360, 58, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Account)
        self.label_17.setGeometry(QtCore.QRect(10, 440, 58, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Account)
        self.label_18.setGeometry(QtCore.QRect(10, 470, 58, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Account)
        self.label_19.setGeometry(QtCore.QRect(10, 300, 58, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Account)
        self.label_20.setGeometry(QtCore.QRect(10, 330, 61, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Account)
        self.label_21.setGeometry(QtCore.QRect(290, 320, 58, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Account)
        self.label_22.setGeometry(QtCore.QRect(290, 350, 58, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.Account)
        self.label_23.setGeometry(QtCore.QRect(290, 380, 58, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Account)
        self.label_24.setGeometry(QtCore.QRect(290, 410, 61, 16))
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.Account)
        self.label_26.setGeometry(QtCore.QRect(10, 600, 58, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.Account)
        self.label_27.setGeometry(QtCore.QRect(290, 140, 58, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Account)
        self.label_28.setGeometry(QtCore.QRect(290, 170, 58, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.Account)
        self.label_29.setGeometry(QtCore.QRect(290, 200, 58, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.Account)
        self.label_30.setGeometry(QtCore.QRect(290, 230, 58, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.Account)
        self.label_31.setGeometry(QtCore.QRect(290, 260, 58, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.Account)
        self.label_32.setGeometry(QtCore.QRect(290, 290, 58, 16))
        self.label_32.setObjectName("label_32")
        self.basicsalary = QtWidgets.QLineEdit(self.Account)
        self.basicsalary.setGeometry(QtCore.QRect(100, 120, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.basicsalary.setFont(font)
        self.basicsalary.setObjectName("basicsalary")
        self.healthfee = QtWidgets.QLineEdit(self.Account)
        self.healthfee.setGeometry(QtCore.QRect(100, 470, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.healthfee.setFont(font)
        self.healthfee.setObjectName("healthfee")
        self.sundayovertime = QtWidgets.QLineEdit(self.Account)
        self.sundayovertime.setGeometry(QtCore.QRect(380, 290, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sundayovertime.setFont(font)
        self.sundayovertime.setObjectName("sundayovertime")
        self.saturdayovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.saturdayovertime_meals.setGeometry(QtCore.QRect(380, 260, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saturdayovertime_meals.setFont(font)
        self.saturdayovertime_meals.setObjectName("saturdayovertime_meals")
        self.mealcall = QtWidgets.QLineEdit(self.Account)
        self.mealcall.setGeometry(QtCore.QRect(100, 330, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mealcall.setFont(font)
        self.mealcall.setObjectName("mealcall")
        self.otherminus = QtWidgets.QLineEdit(self.Account)
        self.otherminus.setGeometry(QtCore.QRect(100, 360, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.otherminus.setFont(font)
        self.otherminus.setObjectName("otherminus")
        self.borrow = QtWidgets.QLineEdit(self.Account)
        self.borrow.setGeometry(QtCore.QRect(100, 300, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.borrow.setFont(font)
        self.borrow.setObjectName("borrow")
        self.normalfirstovertime = QtWidgets.QLineEdit(self.Account)
        self.normalfirstovertime.setGeometry(QtCore.QRect(380, 140, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalfirstovertime.setFont(font)
        self.normalfirstovertime.setObjectName("normalfirstovertime")
        self.saturdayovertime = QtWidgets.QLineEdit(self.Account)
        self.saturdayovertime.setGeometry(QtCore.QRect(380, 230, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saturdayovertime.setFont(font)
        self.saturdayovertime.setObjectName("saturdayovertime")
        self.laborpension = QtWidgets.QLineEdit(self.Account)
        self.laborpension.setGeometry(QtCore.QRect(100, 600, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.laborpension.setFont(font)
        self.laborpension.setObjectName("laborpension")
        self.workerfee = QtWidgets.QLineEdit(self.Account)
        self.workerfee.setGeometry(QtCore.QRect(100, 440, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.workerfee.setFont(font)
        self.workerfee.setObjectName("workerfee")
        self.responsiblebouns = QtWidgets.QLineEdit(self.Account)
        self.responsiblebouns.setGeometry(QtCore.QRect(100, 210, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.responsiblebouns.setFont(font)
        self.responsiblebouns.setObjectName("responsiblebouns")
        self.otherplus = QtWidgets.QLineEdit(self.Account)
        self.otherplus.setGeometry(QtCore.QRect(100, 240, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.otherplus.setFont(font)
        self.otherplus.setObjectName("otherplus")
        self.dayoff = QtWidgets.QLineEdit(self.Account)
        self.dayoff.setGeometry(QtCore.QRect(100, 270, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dayoff.setFont(font)
        self.dayoff.setObjectName("dayoff")
        self.total_salary = QtWidgets.QLineEdit(self.Account)
        self.total_salary.setGeometry(QtCore.QRect(380, 630, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total_salary.setFont(font)
        self.total_salary.setObjectName("total_salary")
        self.overtimeother = QtWidgets.QLineEdit(self.Account)
        self.overtimeother.setGeometry(QtCore.QRect(380, 410, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overtimeother.setFont(font)
        self.overtimeother.setObjectName("overtimeother")
        self.specialovertime = QtWidgets.QLineEdit(self.Account)
        self.specialovertime.setGeometry(QtCore.QRect(380, 350, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.specialovertime.setFont(font)
        self.specialovertime.setObjectName("specialovertime")
        self.sundayfovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.sundayfovertime_meals.setGeometry(QtCore.QRect(380, 320, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sundayfovertime_meals.setFont(font)
        self.sundayfovertime_meals.setObjectName("sundayfovertime_meals")
        self.specialovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.specialovertime_meals.setGeometry(QtCore.QRect(380, 380, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.specialovertime_meals.setFont(font)
        self.specialovertime_meals.setObjectName("specialovertime_meals")
        self.normalovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.normalovertime_meals.setGeometry(QtCore.QRect(380, 200, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalovertime_meals.setFont(font)
        self.normalovertime_meals.setObjectName("normalovertime_meals")
        self.allrbouns = QtWidgets.QLineEdit(self.Account)
        self.allrbouns.setGeometry(QtCore.QRect(100, 410, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.allrbouns.setFont(font)
        self.allrbouns.setObjectName("allrbouns")
        self.normalmeals = QtWidgets.QLineEdit(self.Account)
        self.normalmeals.setGeometry(QtCore.QRect(100, 150, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.normalmeals.setFont(font)
        self.normalmeals.setObjectName("normalmeals")
        self.openbouns = QtWidgets.QLineEdit(self.Account)
        self.openbouns.setGeometry(QtCore.QRect(100, 180, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.openbouns.setFont(font)
        self.openbouns.setObjectName("openbouns")
        self.normalsecondovertime = QtWidgets.QLineEdit(self.Account)
        self.normalsecondovertime.setGeometry(QtCore.QRect(380, 170, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalsecondovertime.setFont(font)
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
        self.label_33.setGeometry(QtCore.QRect(290, 630, 58, 16))
        self.label_33.setObjectName("label_33")
        self.pushButton_7 = QtWidgets.QPushButton(self.Account)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 0, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.ename_2 = QtWidgets.QLabel(self.Account)
        self.ename_2.setGeometry(QtCore.QRect(390, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ename_2.setFont(font)
        self.ename_2.setObjectName("ename_2")
        self.eid_2 = QtWidgets.QLabel(self.Account)
        self.eid_2.setGeometry(QtCore.QRect(300, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.eid_2.setFont(font)
        self.eid_2.setObjectName("eid_2")
        self.label_36 = QtWidgets.QLabel(self.Account)
        self.label_36.setGeometry(QtCore.QRect(100, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.Account)
        self.label_37.setGeometry(QtCore.QRect(380, 110, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.Account)
        self.label_38.setGeometry(QtCore.QRect(10, 530, 61, 16))
        self.label_38.setObjectName("label_38")
        self.normaltotal = QtWidgets.QLineEdit(self.Account)
        self.normaltotal.setGeometry(QtCore.QRect(100, 530, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normaltotal.setFont(font)
        self.normaltotal.setObjectName("normaltotal")
        self.label_39 = QtWidgets.QLabel(self.Account)
        self.label_39.setGeometry(QtCore.QRect(290, 530, 61, 16))
        self.label_39.setObjectName("label_39")
        self.overtimetotal = QtWidgets.QLineEdit(self.Account)
        self.overtimetotal.setGeometry(QtCore.QRect(380, 530, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overtimetotal.setFont(font)
        self.overtimetotal.setObjectName("overtimetotal")
        self.label_7 = QtWidgets.QLabel(self.Account)
        self.label_7.setGeometry(QtCore.QRect(220, 120, 58, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Account)
        self.label_8.setGeometry(QtCore.QRect(220, 150, 58, 21))
        self.label_8.setObjectName("label_8")
        self.label_25 = QtWidgets.QLabel(self.Account)
        self.label_25.setGeometry(QtCore.QRect(220, 180, 58, 21))
        self.label_25.setObjectName("label_25")
        self.label_34 = QtWidgets.QLabel(self.Account)
        self.label_34.setGeometry(QtCore.QRect(220, 210, 58, 21))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.Account)
        self.label_35.setGeometry(QtCore.QRect(220, 240, 58, 21))
        self.label_35.setObjectName("label_35")
        self.label_40 = QtWidgets.QLabel(self.Account)
        self.label_40.setGeometry(QtCore.QRect(220, 360, 58, 21))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.Account)
        self.label_41.setGeometry(QtCore.QRect(220, 300, 58, 21))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.Account)
        self.label_42.setGeometry(QtCore.QRect(220, 410, 58, 21))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.Account)
        self.label_43.setGeometry(QtCore.QRect(220, 270, 58, 21))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.Account)
        self.label_44.setGeometry(QtCore.QRect(220, 440, 58, 21))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.Account)
        self.label_45.setGeometry(QtCore.QRect(220, 330, 58, 21))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.Account)
        self.label_46.setGeometry(QtCore.QRect(220, 470, 58, 21))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.Account)
        self.label_47.setGeometry(QtCore.QRect(220, 530, 58, 21))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.Account)
        self.label_48.setGeometry(QtCore.QRect(220, 600, 58, 21))
        self.label_48.setObjectName("label_48")
        self.label_51 = QtWidgets.QLabel(self.Account)
        self.label_51.setGeometry(QtCore.QRect(500, 140, 58, 21))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.Account)
        self.label_52.setGeometry(QtCore.QRect(500, 170, 58, 21))
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.Account)
        self.label_53.setGeometry(QtCore.QRect(500, 200, 58, 21))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.Account)
        self.label_54.setGeometry(QtCore.QRect(500, 230, 58, 21))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.Account)
        self.label_55.setGeometry(QtCore.QRect(500, 260, 58, 21))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.Account)
        self.label_56.setGeometry(QtCore.QRect(500, 290, 58, 21))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.Account)
        self.label_57.setGeometry(QtCore.QRect(500, 320, 58, 21))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.Account)
        self.label_58.setGeometry(QtCore.QRect(500, 350, 58, 21))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.Account)
        self.label_59.setGeometry(QtCore.QRect(500, 380, 58, 21))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.Account)
        self.label_60.setGeometry(QtCore.QRect(500, 410, 58, 21))
        self.label_60.setObjectName("label_60")
        self.label_63 = QtWidgets.QLabel(self.Account)
        self.label_63.setGeometry(QtCore.QRect(500, 530, 58, 21))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.Account)
        self.label_64.setGeometry(QtCore.QRect(500, 630, 58, 21))
        self.label_64.setObjectName("label_64")
        self.label_50 = QtWidgets.QLabel(self.Account)
        self.label_50.setGeometry(QtCore.QRect(90, 50, 58, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_61 = QtWidgets.QLabel(self.Account)
        self.label_61.setGeometry(QtCore.QRect(240, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.line = QtWidgets.QFrame(self.Account)
        self.line.setGeometry(QtCore.QRect(0, 70, 531, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionMain = QtWidgets.QAction(MainWindow)
        self.actionMain.setObjectName("actionMain")
        self.actionehistory = QtWidgets.QAction(MainWindow)
        self.actionehistory.setObjectName("actionehistory")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actiondelete = QtWidgets.QAction(MainWindow)
        self.actiondelete.setObjectName("actiondelete")
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionchistory = QtWidgets.QAction(MainWindow)
        self.actionchistory.setObjectName("actionchistory")
        self.actionehistory_2 = QtWidgets.QAction(MainWindow)
        self.actionehistory_2.setObjectName("actionehistory_2")
        self.menu.addAction(self.actionnew)
        self.menu.addAction(self.actiondelete)
        self.menu_2.addAction(self.actionsetting)
        self.menu_3.addAction(self.actionchistory)
        self.menu_3.addAction(self.actionehistory_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Totalpay.setText(_translate("MainWindow", "1,000,000,000"))
        self.label.setText(_translate("MainWindow", "員工編號"))
        self.label_2.setText(_translate("MainWindow", "年資"))
        self.label_3.setText(_translate("MainWindow", "員工性質"))
        self.label_4.setText(_translate("MainWindow", "特休"))
        self.label_5.setText(_translate("MainWindow", "員工姓名"))
        self.label_6.setText(_translate("MainWindow", "基本底薪"))
        self.pushButton.setText(_translate("MainWindow", "修改"))
        self.pushButton_2.setText(_translate("MainWindow", "完成"))
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
        self.basicsalary.setText(_translate("MainWindow", "0"))
        self.healthfee.setText(_translate("MainWindow", "0"))
        self.sundayovertime.setText(_translate("MainWindow", "0"))
        self.saturdayovertime_meals.setText(_translate("MainWindow", "0"))
        self.mealcall.setText(_translate("MainWindow", "0"))
        self.otherminus.setText(_translate("MainWindow", "0"))
        self.borrow.setText(_translate("MainWindow", "0"))
        self.normalfirstovertime.setText(_translate("MainWindow", "0"))
        self.saturdayovertime.setText(_translate("MainWindow", "0"))
        self.laborpension.setText(_translate("MainWindow", "0"))
        self.workerfee.setText(_translate("MainWindow", "0"))
        self.responsiblebouns.setText(_translate("MainWindow", "0"))
        self.otherplus.setText(_translate("MainWindow", "0"))
        self.dayoff.setText(_translate("MainWindow", "0"))
        self.total_salary.setText(_translate("MainWindow", "0"))
        self.overtimeother.setText(_translate("MainWindow", "0"))
        self.specialovertime.setText(_translate("MainWindow", "0"))
        self.sundayfovertime_meals.setText(_translate("MainWindow", "0"))
        self.specialovertime_meals.setText(_translate("MainWindow", "0"))
        self.normalovertime_meals.setText(_translate("MainWindow", "0"))
        self.allrbouns.setText(_translate("MainWindow", "0"))
        self.normalmeals.setText(_translate("MainWindow", "0"))
        self.openbouns.setText(_translate("MainWindow", "0"))
        self.normalsecondovertime.setText(_translate("MainWindow", "0"))
        self.pushButton_3.setText(_translate("MainWindow", "試算"))
        self.pushButton_4.setText(_translate("MainWindow", "刪除"))
        self.pushButton_5.setText(_translate("MainWindow", "預覽"))
        self.pushButton_6.setText(_translate("MainWindow", "新增"))
        self.label_33.setText(_translate("MainWindow", "本月薪水"))
        self.pushButton_7.setText(_translate("MainWindow", "本月結算"))
        self.ename_2.setText(_translate("MainWindow", "ename"))
        self.eid_2.setText(_translate("MainWindow", "eid"))
        self.label_36.setText(_translate("MainWindow", "一般項"))
        self.label_37.setText(_translate("MainWindow", "加班項"))
        self.label_38.setText(_translate("MainWindow", "一般總和"))
        self.normaltotal.setText(_translate("MainWindow", "0"))
        self.label_39.setText(_translate("MainWindow", "加班總和"))
        self.overtimetotal.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "元"))
        self.label_8.setText(_translate("MainWindow", "次"))
        self.label_25.setText(_translate("MainWindow", "次"))
        self.label_34.setText(_translate("MainWindow", "元"))
        self.label_35.setText(_translate("MainWindow", "元"))
        self.label_40.setText(_translate("MainWindow", "元"))
        self.label_41.setText(_translate("MainWindow", "元"))
        self.label_42.setText(_translate("MainWindow", "元"))
        self.label_43.setText(_translate("MainWindow", "小時"))
        self.label_44.setText(_translate("MainWindow", "元"))
        self.label_45.setText(_translate("MainWindow", "次"))
        self.label_46.setText(_translate("MainWindow", "元"))
        self.label_47.setText(_translate("MainWindow", "元"))
        self.label_48.setText(_translate("MainWindow", "元"))
        self.label_51.setText(_translate("MainWindow", "小時"))
        self.label_52.setText(_translate("MainWindow", "小時"))
        self.label_53.setText(_translate("MainWindow", "次"))
        self.label_54.setText(_translate("MainWindow", "天"))
        self.label_55.setText(_translate("MainWindow", "次"))
        self.label_56.setText(_translate("MainWindow", "天"))
        self.label_57.setText(_translate("MainWindow", "次"))
        self.label_58.setText(_translate("MainWindow", "天"))
        self.label_59.setText(_translate("MainWindow", "次"))
        self.label_60.setText(_translate("MainWindow", "元"))
        self.label_63.setText(_translate("MainWindow", "元"))
        self.label_64.setText(_translate("MainWindow", "元"))
        self.label_50.setText(_translate("MainWindow", "年"))
        self.label_61.setText(_translate("MainWindow", "月"))
        self.menu.setTitle(_translate("MainWindow", "員工"))
        self.menu_2.setTitle(_translate("MainWindow", "設定"))
        self.menu_3.setTitle(_translate("MainWindow", "資料"))
        self.actionMain.setText(_translate("MainWindow", "setvalue"))
        self.actionehistory.setText(_translate("MainWindow", "ehistory"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actiondelete.setText(_translate("MainWindow", "delete"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))
        self.actionchistory.setText(_translate("MainWindow", "chistory"))
        self.actionehistory_2.setText(_translate("MainWindow", "ehistory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
