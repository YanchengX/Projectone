import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal, QStringListModel
import math
from doct import Preview

class Model(QStringListModel):
    click_emp = pyqtSignal(dict)
    info_edit_click = pyqtSignal()
    info_done_click = pyqtSignal(str)
    account_guide_signal = pyqtSignal(str)
    create_click = pyqtSignal(str)
    delete_click = pyqtSignal(str)
    preview_click = pyqtSignal(list)
    date_signal = pyqtSignal(list)
    sumtotalsignal = pyqtSignal(str)
    auto_count_value = pyqtSignal(dict)
    closeAccount = pyqtSignal(str)

    def __init__(self):
        super(Model, self).__init__()
        self.conn = sqlite3.connect('employee_salary.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM basicinfo WHERE 1')
        self.infodata = self.cursor.fetchall()
        
        #account 變數用sumdata包含在內        
        self.d = None
        
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
        self.test = self.cursor.execute("SELECT eid FROM eventdata WHERE eid=:eid AND year = :year AND month = :month",{  'eid':self.infodata[index][0],  'year':self.year,  'month':self.month})
        if self.test.fetchone() != None:
            self.emp = self.cursor.execute("SELECT * FROM basicinfo LEFT JOIN eventdata ON basicinfo.eid = eventdata.eid LEFT JOIN normal ON basicinfo.eid = normal.eid LEFT JOIN overtime ON basicinfo.eid = overtime.eid WHERE eventdata.year = :year AND eventdata.month = :month AND basicinfo.eid =:eid",
            {
                'year' : self.year,
                'month': self.month,
                'eid' : self.infodata[index][0]
            })
            e = self.emp.fetchone()
            self.data = {
            "eid": e[0],
            "eproperty":e[1],
            "ename":e[2],
            "seniority":e[3],
            "specialdayoff":e[4],
            "basicsalary":e[5],
            #----------
            "caseid":e[6],
            "year":e[8],
            "month":e[9],
            "total_salary":e[11],
            "laborpension":e[12],
            "normalmeals":e[16],
            "allrbouns":e[17],
            "openbouns":e[18],
            "responsiblebouns":e[19],
            "otherplus":e[20],
            "workerfee":e[21],
            "healthfee":e[22],
            "dayoff":e[23],
            "borrow":e[24],
            "mealcall":e[25],
            "otherminus":e[26],
            "normaltotal":e[27],
            #----------
            "normalfirstovertime":e[31],     
            "normalsecondovertime":e[32],
            "saturdayovertime":e[33],       
            "specialovertime":e[34],	        
            "sundayovertime":e[35],	       
            "normalovertime_meals":e[36],   
            "saturdayovertime_meals":e[37],
            "specialovertime_meals":e[38], 
            "sundayfovertime_meals":e[39],
            "overtimeother":e[40], 
            "overtimetotal":e[41]
        }
        else:
            self.emp = self.cursor.execute("SELECT * FROM basicinfo WHERE eid =:eid ",{'eid':self.infodata[index][0]})
            e = self.emp.fetchone()
            self.data = {
            "eid": e[0],
            "eproperty":e[1],
            "ename":e[2],
            "seniority":e[3],
            "specialdayoff":e[4],
            "basicsalary":e[5],
            #----------
            "caseid": 0,
            "year": self.year,
            "month":self.month,
            "total_salary":0,
            "laborpension":0,
            "normalmeals":0,
            "allrbouns":0,
            "openbouns":0,
            "responsiblebouns":0,
            "otherplus":0,
            "workerfee":0,
            "healthfee":0,
            "dayoff":0,
            "borrow":0,
            "mealcall":0,
            "otherminus":0,
            "normaltotal":0,
            #----------
            "normalfirstovertime":0,     
            "normalsecondovertime":0,
            "saturdayovertime":0,       
            "specialovertime":0,	        
            "sundayovertime":0,	       
            "normalovertime_meals":0,   
            "saturdayovertime_meals":0,
            "specialovertime_meals":0, 
            "sundayfovertime_meals":0,
            "overtimeother":0, 
            "overtimetotal":0
        }
        self.click_emp.emit(self.data)


    def account_guide_checked(self, index):
        self.idata = self.cursor.execute('SELECT basicinfo.salarychecked FROM basicinfo WHERE basicinfo.eid =:eid',{'eid':self.infodata[index][0]})
        self.checked =  self.idata.fetchone()
        self.account_guide_signal.emit(str(self.checked[0]))


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


    def create_account_clicked(self, dictdata):
        #find all event
        self.tmp = self.cursor.execute("SELECT eventdata.caseid, eventdata.eid, eventdata.year, eventdata.month FROM eventdata WHERE 1")
        self.eventdata = self.tmp.fetchall()
        
        #caseid logic
        item = self.eventdata[len(self.eventdata)-1][0] if self.eventdata else 0
        self.caseid = item
        self.count = 0
        
        for item in self.eventdata:
            #update
            if dictdata["eid"] in item and str(self.year) in item and str(self.month) in item:
                #event normal overtime\
                self.cursor.execute("UPDATE eventdata SET total_salary = :total_salary ,laborpension = :laborpension WHERE eid = :eid and year = :year and month = :month",
                {
                    "eid":dictdata["eid"],
                    "year":dictdata["year"],
                    "month":dictdata["month"],
                    "total_salary":dictdata["total_salary"],
                    "laborpension":dictdata["laborpension"]
                })
                self.cursor.execute("UPDATE normal SET normalmeals = :normalmeals, allrbouns = :allrbouns, openbouns = :openbouns, responsiblebouns = :responsiblebouns, otherplus = :otherplus, workerfee = :workerfee, healthfee = :healthfee, dayoff = :dayoff, borrow = :borrow, mealcall = :mealcall, otherminus = :otherminus, normaltotal = :normaltotal WHERE eid = :eid and year = :year and month = :month",
                {
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
                self.cursor.execute("UPDATE overtime SET normalfirstovertime = :normalfirstovertime, normalsecondovertime = :normalsecondovertime, saturdayovertime = :saturdayovertime, specialovertime = :specialovertime, sundayovertime = :sundayovertime, normalovertime_meals = :normalovertime_meals, saturdayovertime_meals = :saturdayovertime_meals, specialovertime_meals = :specialovertime_meals, sundayfovertime_meals = :sundayfovertime_meals, overtimeother = :overtimeother, overtimetotal = :overtimetotal  WHERE eid = :eid and year = :year and month = :month",
                {
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
                self.create_click.emit(dictdata['eid'] + "".join('###'))
                self.count += 1
                break
        if self.count == False:
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
            self.create_click.emit(dictdata['eid'])
        self.conn.commit()


    def delete_account_clicked(self,dictdata):
        try:
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
        except ValueError as e:
            print(e)


    def sumtotal(self):
        self.totalpay = 0
        self.total =  self.cursor.execute("SELECT total_salary FROM eventdata WHERE year = :year and month = :month"
        ,{
            'year':str(self.year),
            'month':str(self.month)
            })
        data = self.total.fetchall()
        for item in data:
            self.totalpay += int(item[0])
        self.salary = format(self.totalpay,',')
        self.sumtotalsignal.emit(self.salary)


    def preview(self, eid):
        self.emp = self.cursor.execute("SELECT * FROM basicinfo LEFT JOIN eventdata ON basicinfo.eid = eventdata.eid LEFT JOIN normal ON basicinfo.eid = normal.eid LEFT JOIN overtime ON basicinfo.eid = overtime.eid WHERE eventdata.year = :year AND eventdata.month = :month AND basicinfo.eid =:eid",
        {
            'year' : self.year,
            'month': self.month,
            'eid' : eid
        })
        self.pre = Preview(self.emp)
        self.preview_click.emit([eid])


    def get_date(self):
        self.date_signal.emit([self.year, self.month])

    #-------autoItem
    def autocount(self, sum_data):
        self.d = sum_data
        #auto
        self.d['allrbouns'] = self.allrbouns_value if self.d['dayoff'] == 0 else 0
        self.d['workerfee'] = math.ceil(self.d['basicsalary'] * self.workerfee_rate)
        self.d['healthfee'] = math.ceil(self.d['basicsalary'] * self.healthfee_rate)
        #nomal
        self.d['normalmeals']*= self.meal_value
        self.d['openbouns']*= self.openbouns_value
        self.d['responsiblebouns']*= self.responsiblebouns_value
        self.d['dayoff']*= math.ceil(self.d['basicsalary']/30/8)
        self.d['mealcall']*= self.meal_value
        #overtime
        self.d['normalfirstovertime']*= math.ceil(self.d['basicsalary']*self.overtime1)
        self.d['normalsecondovertime']*= math.ceil(self.d['basicsalary']*self.overtime2) 
        self.d['normalovertime_meals']*= self.meal_value
        self.d['saturdayovertime'] = self.d['saturdayovertime'] * (math.ceil(self.d['basicsalary']*self.overtime1) * 2 + math.ceil(self.d['basicsalary']*self.overtime2) * 6)
        self.d['saturdayovertime_meals']*= self.meal_value
        self.d['sundayovertime'] = self.d['sundayovertime'] * (math.ceil(self.d['basicsalary']*self.overtime1) * 2 + math.ceil(self.d['basicsalary']*self.overtime2) * 6)
        self.d['sundayfovertime_meals']*= self.meal_value   
        self.d['specialovertime'] = self.d['specialovertime'] * (math.ceil(self.d['basicsalary']*self.overtime1) * 2 + math.ceil(self.d['basicsalary']*self.overtime2) * 6)
        self.d['specialovertime_meals']*= self.meal_value

        normalt = 0
        overt = 0
        ########
        normalt = self.d['basicsalary'] + self.d['normalmeals'] + self.d['openbouns'] + self.d['responsiblebouns'] + self.d['otherplus'] + self.d['allrbouns'] - self.d['dayoff'] - self.d['borrow'] - self.d['mealcall'] - self.d['otherminus'] - self.d['workerfee'] - self.d['healthfee']
        overt = self.d['normalfirstovertime'] + self.d['normalsecondovertime'] + self.d['normalovertime_meals'] + self.d['saturdayovertime'] + self.d['saturdayovertime_meals'] + self.d['sundayovertime'] + self.d['sundayfovertime_meals'] + self.d['specialovertime'] + self.d['specialovertime_meals'] + self.d['overtimeother']
        ########
        self.d['normaltotal'] = normalt
        self.d['overtimetotal'] = overt
        self.d['laborpension'] = round(self.d['basicsalary'] * 0.06)
        self.d['total_salary'] = normalt + overt
        #emit auto data and count
        autodata = {
            'all':str(self.d['allrbouns']),
            'worker':str(self.d['workerfee']),
            'health':str(self.d['healthfee']),
            'normalt':str(self.d['normaltotal']),
            'overt':str(self.d['overtimetotal']),
            'labor':str(self.d['laborpension']),
            'total':str(self.d['total_salary'])
        }
        self.auto_count_value.emit(autodata)


    def close_account(self):
        #當月結算->
        # 接收combobox年月份，對到該node如果.next = none 可以執行該event
        # new node year and month, 
        # db 將emp 的salarychecked 改為0 -> 需跟year, month配合 每月一個salarycheck 在搭配eid
        # 
        #           
        self.closeAccount.emit('fuck')

    def select_date(self):
        pass





class dataNode:
    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month
        self.next = None
