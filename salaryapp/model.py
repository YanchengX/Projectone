import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal, QStringListModel
import math

class Model(QStringListModel):
    click_emp = pyqtSignal(list)
    info_edit_click = pyqtSignal()
    info_done_click = pyqtSignal(str)
    accountdata_click = pyqtSignal(list)
    create_click = pyqtSignal(str)
    date_signal = pyqtSignal(list)

    def __init__(self):
        super(Model, self).__init__()
        self.conn = sqlite3.connect('employee_salary.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM basicinfo WHERE 1')
        self.infodata = self.cursor.fetchall()
        
        #account 變數用accountlistdata包含在內        
        self.accountlistdata = None
        
        #year,month
        self.year = 2022
        self.month = 10

        #normal_value參數
        self.workerfee_rate = 0.115 * 0.2
        self.healthfee_rate = 0.0517 * 0.3
        self.openbouns_value = 50
        self.allrbouns_value = 1000
        self.responsiblebouns_value = 1000
        self.meal_value = 60
        self.overtime1 = 1/8/30*1.34
        self.overtime2 = 1/8/30*1.67


    def show_undoview(self):
        self.strdata = []
        for tupledata in self.infodata: #(a,3,7,8,,54,3)
            tmp = ''
            for i in range(3):
                tmp += ''.join(tupledata[i])
                tmp += ''.join(' / ')
            self.strdata.append(tmp)
        self.setStringList(self.strdata)

    def undoview_clicked(self, index):
        self.click_emp.emit(list(self.infodata[index]))

    def infodata_edit_clicked(self):
        self.info_edit_click.emit()
    
    def infodata_done_clicked(self, listinfodata):
        self.cursor.execute("UPDATE basicinfo SET eproperty=:eproperty, ename=:ename, seniority=:seniority, spectialdayoff=:spectialdayoff, basicsalary=:basicsalary WHERE eid =:eid"
        ,{
            'eid':listinfodata[0],
            'eproperty':listinfodata[1],
            'ename':listinfodata[2],
            'seniority':listinfodata[3],
            'spectialdayoff':listinfodata[4],
            'basicsalary':listinfodata[5],
        })
        self.conn.commit()
        #update basicinfo
        self.cursor.execute('SELECT * FROM basicinfo WHERE 1')
        self.infodata = self.cursor.fetchall()
        # self.returndata = [eid,eproperty,ename,seniority,spectialdayoff,basicsalary]
        self.info_done_click.emit(listinfodata[0])
    

    def accountdata_clicked(self, accountlistdata):

        #0 int(self.basicsalary.text()),
        #1 int(self.normalmeals.text()),
        #2 int(self.openbouns.text()),
        #3 int(self.responsiblebouns.text()),
        #4 int(self.otherplus.text()),
        #5 int(self.dayoff.text()),
        #6 int(self.borrow.text()),
        #7 int(self.mealcall.text()),
        #8 int(self.otherminus.text()), 
        # #-------normal
        #9 int(self.normalfirstovertime.text()),
        #10 int(self.normalsecondovertime.text()),
        #11 int(self.normalovertime_meals.text()),
        #12 int(self.saturdayovertime.text()),
        #13 int(self.saturdayovertime_meals.text()),
        #14 int(self.sundayovertime.text()),
        #15 int(self.sundayfovertime_meals.text()),
        #16 int(self.specialovertime.text()),
        #17 int(self.specialovertime_meals.text()),
        #18 int(self.overtimeother.text()),
        # #-------ovetime
        #19 int(self.allrbouns.text()),
        #20 int(self.workerfee.text()),
        #21 int(self.healthfee.text()),
        #22 int(self.normaltotal.text()),
        #23 int(self.overtimetotal.text()),
        #24 int(self.laborpension.text()),
        #25 int(self.total_salary.text()),    
        # #-------autoItem

        #model 處理auto試算邏輯 但不接觸DB
        self.accountlistdata = accountlistdata
        #auto
        self.accountlistdata[19] = self.allrbouns_value if self.accountlistdata[5] == 0 else 0
        self.accountlistdata[20] = math.ceil(self.accountlistdata[0] * self.workerfee_rate)
        self.accountlistdata[21] = math.ceil(self.accountlistdata[0] * self.healthfee_rate)
        #nomal
        self.accountlistdata[1]*= self.meal_value
        self.accountlistdata[2]*= self.openbouns_value
        self.accountlistdata[3]*= self.responsiblebouns_value
        self.accountlistdata[5]*= math.ceil(self.accountlistdata[0]/30/8)
        self.accountlistdata[7]*= self.meal_value
        #overtime
        self.accountlistdata[9]*= math.ceil(self.accountlistdata[0]*self.overtime1)
        self.accountlistdata[10]*= math.ceil(self.accountlistdata[0]*self.overtime2) 
        self.accountlistdata[11]*= self.meal_value
        self.accountlistdata[12] = self.accountlistdata[12] * (math.ceil(self.accountlistdata[0]*self.overtime1) * 2 + math.ceil(self.accountlistdata[0]*self.overtime2) * 6)
        self.accountlistdata[13]*= self.meal_value
        self.accountlistdata[14] = self.accountlistdata[14] * (math.ceil(self.accountlistdata[0]*self.overtime1) * 2 + math.ceil(self.accountlistdata[0]*self.overtime2) * 6)
        self.accountlistdata[15]*= self.meal_value   
        self.accountlistdata[16] = self.accountlistdata[16] * (math.ceil(self.accountlistdata[0]*self.overtime1) * 2 + math.ceil(self.accountlistdata[0]*self.overtime2) * 6)
        self.accountlistdata[17]*= self.meal_value
        
        # total 
        tmp = 0
        for i in range(0,5):
            tmp += self.accountlistdata[i]
        for i in range(5,9):
            tmp -= self.accountlistdata[i]
        self.accountlistdata[22] = tmp + self.accountlistdata[19] -self.accountlistdata[20] - self.accountlistdata[21]
        
        tmp = 0
        for i in range(9,19):
            tmp += self.accountlistdata[i]
        self.accountlistdata[23] = tmp 

        #self.accountlistdata[23] 9~18 

        self.accountlistdata[24] = round(self.accountlistdata[0] * 0.06)
        self.accountlistdata[25] = self.accountlistdata[22] + self.accountlistdata[23]
        
        self.autodata = []
        for i in range(19,26):
            self.autodata.append(self.accountlistdata[i])

        self.accountdata_click.emit(self.autodata)


    def create_account_clicked(self, accountlistdata):
        
        self.create_click.emit('fuck')
    
    def get_date(self):
        self.date_signal.emit([self.year, self.month])

    def preview(self):
        print('fuck you')

