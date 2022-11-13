import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal, QStringListModel
import math

class Model(QStringListModel):
    click_emp = pyqtSignal(list)
    info_edit_click = pyqtSignal()
    info_done_click = pyqtSignal(str)
    accountdata_click = pyqtSignal(list)
    create_click = pyqtSignal(str)
    delete_click = pyqtSignal(str)
    date_signal = pyqtSignal(list)
    

    def __init__(self):
        super(Model, self).__init__()
        self.conn = sqlite3.connect('employee_salary.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM basicinfo WHERE 1')
        self.infodata = self.cursor.fetchall()
        
        #account 變數用accountlistdata包含在內        
        self.accountlistdata = None
        
        self.caseid = 0
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

        self.viewdata = self.cursor.execute("SELECT basicinfo.eid, basicinfo.eproperty, basicinfo.ename, basicinfo.salarychecked, eventdata.total_salary FROM basicinfo LEFT JOIN eventdata ON basicinfo.eid = eventdata.eid")        

        for listdata in self.viewdata: #(a,3,7,8,,54,3)
            tmp = ''
            for i in range(3):
                tmp += ''.join(listdata[i])
                tmp += ''.join(' / ')
            
            if listdata[3] == 0:
                tmp += ''.join('未登錄')
            if listdata[3] == 1:
                tmp += ''.join(str(listdata[4]))

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

    def create_account_clicked(self, dictdata):
        
        self.tmp = self.cursor.execute("SELECT eventdata.caseid, eventdata.eid, eventdata.year, eventdata.month FROM eventdata WHERE 1")
        self.eventdata = self.tmp.fetchall()
        tmp = self.eventdata[len(self.eventdata)-1][0]
        self.caseid = tmp
        self.count = 0
        for item in self.eventdata:
            if dictdata["eid"] in item and str(self.year) in item and str(self.month) in item:
                print('重複新增該員工薪水，請進行修改或刪除重試')
                self.count += 1
                break
        if self.count == False:
            print(self.caseid)
            self.caseid += 1        
            # update salarychecked
            self.cursor.execute("UPDATE basicinfo SET salarychecked = 1 WHERE eid = :eid",{'eid':dictdata['eid']})
            #insert data
            self.cursor.execute("INSERT INTO eventdata VALUES(:caseid, :eid, :year, :month, :total_salary, :laborpension)"
            ,{
                "caseid":self.caseid,
                "eid":dictdata["eid"],
                "year":dictdata["year"],
                "month":dictdata["month"],
                "total_salary":dictdata["total_salary"],
                "laborpension":dictdata["laborpension"]
            })
            self.cursor.execute("INSERT INTO normal VALUES(:eid, :year, :month, :normalmeals, :allrbouns, :openbouns, :responsiblebouns, :otherplus, :workerfee, :healthfee, :dayoff, :borrow, :mealcall, :otherminus, :normaltotal)"
            ,{
                "eid":dictdata["eid"],
                "year":dictdata["year"],
                "month":dictdata["month"],
                "normalmeals":dictdata["normalmeals"],
                "allrbouns":dictdata["allrbouns"],
                "openbouns":dictdata["openbouns"],
                "responsiblebouns":dictdata["responsiblebouns"],
                "otherplus":dictdata["otherplus"],
                "workerfee":dictdata["workerfee"],
                "healthfee":dictdata["healthfee"],
                "dayoff":dictdata["dayoff"],
                "borrow":dictdata["borrow"],
                "mealcall":dictdata["mealcall"],
                "otherminus":dictdata["otherminus"],
                "normaltotal":dictdata["normaltotal"],
            })

            self.cursor.execute("INSERT INTO overtime VALUES(:eid, :year, :month, :normalfirstovertime, :normalsecondovertime, :saturdayovertime, :specialovertime, :sundayovertime, :normalovertime_meals, :saturdayovertime_meals, :specialovertime_meals, :sundayfovertime_meals, :overtimeother, :overtimetotal)"
            ,{
                "eid":dictdata["eid"],
                "year":dictdata["year"],	
                "month":dictdata["month"],
                "normalfirstovertime":dictdata["normalfirstovertime"],     
                "normalsecondovertime":dictdata["normalsecondovertime"],
                "saturdayovertime":dictdata["saturdayovertime"],
                "specialovertime":dictdata["specialovertime"],
                "sundayovertime":dictdata["sundayovertime"],
                "normalovertime_meals":dictdata["normalovertime_meals"],
                "saturdayovertime_meals":dictdata["saturdayovertime_meals"],
                "specialovertime_meals":dictdata["specialovertime_meals"], 
                "sundayfovertime_meals":dictdata["sundayfovertime_meals"],
                "overtimeother":dictdata["overtimeother"], 
                "overtimetotal":dictdata["overtimetotal"]
            })
            self.conn.commit()
            self.show_undoview()

    def delete_account_clicked(self,dictdata):
        self.cursor.execute("UPDATE basicinfo SET salarychecked = 0 WHERE eid = :eid",{'eid':dictdata['eid']})
        self.cursor.execute("DELETE FROM eventdata WHERE eid = :eid AND year = :year AND month = :month",
        {
            'eid':dictdata['eid'],
            'year':dictdata['year'],
            'month':dictdata['month']
        })
        self.cursor.execute("DELETE FROM normal WHERE eid = :eid AND year = :year AND month = :month",
        {
            'eid':dictdata['eid'],
            'year':dictdata['year'],
            'month':dictdata['month']
        })
        self.cursor.execute("DELETE FROM overtime WHERE eid = :eid AND year = :year AND month = :month",
        {
            'eid':dictdata['eid'],
            'year':dictdata['year'],
            'month':dictdata['month']
        })
        self.conn.commit()
        self.delete_click.emit(dictdata['eid'])
        self.show_undoview()

    def get_date(self):
        self.date_signal.emit([self.year, self.month])

    def preview(self):
        print('fuck you')

