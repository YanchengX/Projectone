import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal, QStringListModel
import math
from doct import Preview

class Model(QStringListModel):
    click_emp = pyqtSignal(dict)            #員工click
    info_edit_click = pyqtSignal()          #一般編輯click
    info_done_click = pyqtSignal(str)       #一般完成click
    account_guide_signal = pyqtSignal(str)  #防呆引導
    create_click = pyqtSignal(str)          #新增
    delete_click = pyqtSignal(str)          #刪除
    preview_click = pyqtSignal(list)        #預覽
    date_signal = pyqtSignal(list)          #日期
    sumtotalsignal = pyqtSignal(str)        #總計
    auto_count_value = pyqtSignal(dict)     #自動計算
    closeAccount = pyqtSignal(str)          #單月結算
    comboevent = pyqtSignal(list)           #combox信號
    dateselectsignal = pyqtSignal(list)     #選擇combox date
    latesignal = pyqtSignal(bool)           #最後單月判斷
    
    #subclass

    newemp = pyqtSignal(str)                #新增員工
    delemp = pyqtSignal(str)                #刪除員工
    valuesetting = pyqtSignal(str)          #新增員工
    emphis = pyqtSignal(str)                #新增員工
    comhis = pyqtSignal(str)                #新增員工


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
        self.year = None
        self.month = None
        self.date_event()

        
        #normal_value參數
        self.workerfee_rate = 0.115 * 0.2
        self.healthfee_rate = 0.0517 * 0.3
        self.openbouns_value = 50
        self.allrbouns_value = 1000
        self.responsiblebouns_value = 1000
        self.meal_value = 60
        self.overtime1 = 1/8/30*1.34
        self.overtime2 = 1/8/30*1.67


    '''listview show'''
    def show_undoview(self):
        self.strdata = []
        # join basicinfo and total.salary and salarychecked -> eid year month is must unique
        self.viewdata = self.cursor.execute("SELECT basicinfo.eid, basicinfo.eproperty, basicinfo.ename, checks.year, checks.month, checks.salary_checked, eventdata.total_salary FROM basicinfo LEFT JOIN checks ON basicinfo.eid = checks.eid LEFT JOIN eventdata ON basicinfo.eid = eventdata.eid AND checks.year = eventdata.year AND checks.month = eventdata.month WHERE checks.year = :year AND checks.month = :month",{
            'year':self.year,
            'month':self.month
        })

        for listdata in self.viewdata:
            print(listdata)
            #eid eproperty name checks year month salary
            tmp = ''
            for i in range(3):
                tmp += ''.join(listdata[i])
                tmp += ''.join(' / ')
            if listdata[5] == 0:
                tmp += ''.join('未登錄')
            if listdata[5] == 1:
                tmp += ''.join(str(listdata[6]))

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
            "total_salary":e[10],
            "laborpension":e[11],
            "normalmeals":e[15],
            "allrbouns":e[16],
            "openbouns":e[17],
            "responsiblebouns":e[18],
            "otherplus":e[19],
            "workerfee":e[20],
            "healthfee":e[21],
            "dayoff":e[22],
            "borrow":e[23],
            "mealcall":e[24],
            "otherminus":e[25],
            "normaltotal":e[26],
            #----------
            "normalfirstovertime":e[30],     
            "normalsecondovertime":e[31],
            "saturdayovertime":e[32],       
            "specialovertime":e[33],	        
            "sundayovertime":e[34],	       
            "normalovertime_meals":e[35],   
            "saturdayovertime_meals":e[36],
            "specialovertime_meals":e[37], 
            "sundayfovertime_meals":e[38],
            "overtimeother":e[39], 
            "overtimetotal":e[40]
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


    '''button guide in select date when salarychecked is 0 or 1
        #to be contiune to solve'''
    def account_guide_checked(self, index):
        check = self.cursor.execute('SELECT checks.eid, checks.salary_checked FROM checks WHERE eid = :eid AND year = :year AND month = :month',{
            'eid' : self.infodata[index][0],
            'year' : self.year,
            'month' : self.month
        })
        c = check.fetchone()
        self.account_guide_signal.emit(str(c[1]))
        #self.idata = self.cursor.execute('SELECT basicinfo.salarychecked FROM basicinfo WHERE basicinfo.eid =:eid',{'eid':self.infodata[index][0]})


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


    '''新增/更新event
        #update salary checked完成'''
    def create_account_clicked(self, dictdata):
        #find all event
        self.tmp = self.cursor.execute("SELECT eventdata.caseid, eventdata.eid, eventdata.year, eventdata.month FROM eventdata WHERE 1")
        self.eventdata = self.tmp.fetchall()
        
        #caseid logic -> usingstack and combine delete
        item = self.eventdata[len(self.eventdata)-1][0] if self.eventdata else 0
        self.caseid = item
        self.count = 0
         
        for item in self.eventdata:
            #update
            if dictdata["eid"] in item and str(self.year) in item and str(self.month) in item:
                #event normal overtime
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
            #該月尚未insert
        if self.count == 0:
            self.caseid += 1        
            #salarychecked update
            self.cursor.execute("UPDATE checks SET salary_checked = 1 WHERE eid = :eid AND year = :year AND month = :month",
            {
                'eid':dictdata['eid'],
                'year':dictdata['year'],
                'month':dictdata['month'],
            })
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

    '''刪除event'''
    def delete_account_clicked(self,dictdata):
        try:
            #delete -> event, normal, overtime, checks
            self.cursor.execute("UPDATE checks SET salary_checked = 0 WHERE eid = :eid AND year = :year AND month = :month",
            {
                'eid':dictdata['eid'],
                'year':dictdata['year'],
                'month':dictdata['month'],
            })
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

    '''總額計算'''
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

    '''當月結算事件 當現在指向為lastest date才能進行event'''
    def close_account(self):
        #日期進程
        if int(self.month) + 1 > 12:
            self.year = str(int(self.year) + 1)
            self.month = str(1)
        else:
            self.month = str(int(self.month) + 1)

        #find latest date
        a = self.cursor.execute('SELECT dateid FROM date')
        latest = a.fetchall()[-1][0] #tuple

        #new next date
        self.cursor.execute('INSERT INTO date VALUES(:dateid, :year, :month)',{
            'dateid': latest + 1,
            'year': self.year,
            'month': self.month
        })

        #更新下個月預設salarychecked = 0
        validemp = self.cursor.execute("SELECT basicinfo.eid FROM basicinfo WHERE 1")
        for i in validemp.fetchall():    
            self.cursor.execute("INSERT INTO checks VALUES(:eid, :year, :month, :salary_checked)",{
            'eid':i[0],
            "year":self.year,
            "month":self.month,
            'salary_checked': 0
            })
        self.conn.commit()
        self.closeAccount.emit('更新紀錄日期為 {} 年 {} 月'.format(self.year, self.month))
        self.comboshow()


    '''combobox日期顯示additems事件 要改成date查詢已紀錄事宜'''
    def comboshow(self):
        date = self.cursor.execute('SELECT date.year, date.month FROM date')
        listdate = []
        #set listdate and tostring
        for da in date:
            #prevent duplicate date-> 
            strdata = '{}-{}'.format(da[0],da[1])
            if strdata in listdate:
                print('duplicate date error')
            else:
                listdate.append(da[0] + '-' + da[1])
        self.comboevent.emit(listdate)

    
    '''combobox選擇日期event'''
    def selectdate(self, ym):
        # 偵測該date
        if ym != '':
            sel = ym.split('-')
            self.year, self.month = sel[0], sel[1]
            self.dateselectsignal.emit(ym.split('-'))
        
    

    '''當月結算防呆'''
    def islatest(self, year, month):
        late = self.cursor.execute('SELECT * FROM date')
        a = late.fetchall()     #id,y,m
        boo =  True if year.text() == a[-1][1] and month.text() == a[-1][2] else False
        self.latesignal.emit(boo)



    '''初始化程式date指向的event'''
    def date_event(self):
        isnull = self.cursor.execute("SELECT * FROM date")
        a = isnull.fetchall()
        if a == []:
            #default
            self.cursor.execute('INSERT INTO date VALUES(:dateid, :year, :month)',{
                'dateid': 0,
                'year':'2022',
                'month':'10'
            })
            insert = self.cursor.execute('SELECT * FROM date')
            item = insert.fetchone()
            self.year = item[0]
            self.month = item[1]
            self.conn.commit()
        else:
            #latest (dateid year month)
            self.year = a[-1][1]
            self.month = a[-1][2]

#####################################################################################
#Sub class
    
    '''新增員工 db-> basicinfo, checks'''
    def new_emp(self, data):
        #id property name seniority dayoffspectial basic-salary
        try:
            ymd = data['date'].split('/')
            self.cursor.execute("INSERT INTO basicinfo VALUES('{}','{}','{}','{}','{}','{}')".format(
                data['eid'], data['eproperty'], data['ename'], 0, 0, 0))
            self.cursor.execute("INSERT INTO checks VALUES('{}','{}','{}',{})".format(
                data['eid'], ymd[0], ymd[1], 0))
            self.conn.commit()
            self.newemp.emit('新增員工成功')
        except:
            print('輸入錯誤')

    # def del_emp(self):

    
    # def value_set(self):


    # def emp_history(self):

    
    # def com_history(self):
    