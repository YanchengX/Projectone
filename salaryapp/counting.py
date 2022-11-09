#薪水DB測試

from errno import EIDRM, ENAMETOOLONG
import sqlite3

import math

conn = sqlite3.connect('employee_salary.db')

cur = conn.cursor()

# normal value
workerfee_rate = 0.115 * 0.2
healthfee_rate = 0.0517 * 0.3
openbouns_value = 50
allrbouns_value = 1000
responsiblebouns_value = 1000
meal_value = 60
overtime1 = 1/8/30*1.34
overtime2 = 1/8/30*1.67


# basicinfo

eid = 'A02'
eproperty = '正職'
ename	= 'andchange'
seniority = 2
specialdayoff = 8
basicsalary = 25250

#eventdata

caseid = 1      #if登入成功就 + 1
#eid            
year = '2022'   #if套用就就切換到當月
month	= '10'


#normal

# eid
# year	
# month
normalmeals     = 21 * meal_value
openbouns	    = openbouns_value * 0
responsiblebouns= responsiblebouns_value * (seniority//5)
otherplus	    = 200
workerfee	    = math.ceil(basicsalary * workerfee_rate)
healthfee       = math.ceil(basicsalary * healthfee_rate)
dayoff	        = 0 * math.ceil(basicsalary/30)
borrow	        = 0
mealcall	    = 0 * meal_value
otherminus      = 0

allrbouns	    = allrbouns_value if dayoff == 0 else 0
normaltotal = basicsalary + normalmeals + allrbouns + openbouns + responsiblebouns + otherplus - workerfee - healthfee - dayoff - borrow - mealcall - otherminus

#overtime

# eid
# year	
# month
normalfirstovertime     = math.ceil(basicsalary * overtime1) * 14 #加班時數變數
normalsecondovertime    = math.ceil(basicsalary * overtime2) * 7
saturdayovertime        = math.ceil(basicsalary * overtime1) * 4 + math.ceil(basicsalary * overtime2) * 12
specialovertime	        = math.ceil(basicsalary * overtime1) * 0 + math.ceil(basicsalary * overtime2) * 0
sundayovertime	        = math.ceil(basicsalary * overtime1) * 0 + math.ceil(basicsalary * overtime2) * 0 #+補假一天
normalovertime_meals    = 7 * meal_value
saturdayovertime_meals	= 2 * meal_value
specialovertime_meals   = 0 * meal_value
sundayfovertime_meals	= 0 * meal_value
overtimeother           = 0
overtimetotal           = normalfirstovertime + normalsecondovertime + saturdayovertime + specialovertime + sundayovertime + normalovertime_meals + saturdayovertime_meals + specialovertime_meals + overtimeother + sundayfovertime_meals

#eventdata

total_salary = overtimetotal + normaltotal
laborpension = round(basicsalary * 0.06)


# #basicinfo insert

# conn.execute("INSERT INTO basicinfo VALUES(:eid, :eproperty, :ename, :seniority, :specialdayoff, :basicsalary)"
# ,{
#     "eid":eid,
#     "eproperty":eproperty,
#     "ename":ename,
#     "seniority":seniority,
#     "specialdayoff":specialdayoff,
#     "basicsalary":basicsalary
# })

# #eventdata insert

# conn.execute("INSERT INTO eventdata VALUES(:caseid, :eid, :year, :month, :total_salary, :laborpension)"
# ,{
#     "caseid":caseid,
#     "eid":eid,
#     "year":year,
#     "month":month,
#     "total_salary":total_salary,
#     "laborpension":laborpension
# })


# #normal insert

# conn.execute("INSERT INTO normal VALUES(:eid, :year, :month, :normalmeals, :allrbouns,	:openbouns, :responsiblebouns, :otherplus, :workerfee, :healthfee, :dayoff, :borrow, :mealcall, :otherminus, :normaltotal)"
# ,{

# "eid":eid,
# "year":year,
# "month":month,
# "normalmeals":normalmeals,
# "allrbouns":allrbouns,
# "openbouns":openbouns,
# "responsiblebouns":responsiblebouns,
# "otherplus":otherplus,
# "workerfee":workerfee,
# "healthfee":healthfee,
# "dayoff":dayoff,
# "borrow":borrow,
# "mealcall":mealcall,
# "otherminus":otherminus,
# "normaltotal":normaltotal
# })

# #overtime insert

# conn.execute("INSERT INTO overtime VALUES(:eid, :year, :month, :normalfirstovertime, :normalsecondovertime, :saturdayovertime, :specialovertime, :sundayovertime, :normalovertime_meals, :saturdayovertime_meals, :specialovertime_meals, :sundayfovertime_meals, :overtimeother, :overtimetotal)",{

# "eid":eid,
# "year":year,	
# "month":month,
# "normalfirstovertime":normalfirstovertime,     
# "normalsecondovertime":normalsecondovertime,
# "saturdayovertime":saturdayovertime,       
# "specialovertime":specialovertime,	        
# "sundayovertime":sundayovertime,	       
# "normalovertime_meals":normalovertime_meals,   
# "saturdayovertime_meals":saturdayovertime_meals,
# "specialovertime_meals":specialovertime_meals, 
# "sundayfovertime_meals":sundayfovertime_meals,
# "overtimeother":overtimeother, 
# "overtimetotal":overtimetotal
# })


#setvalue insert

# conn.execute("INSERT INTO setvalue VALUES(:workerfee_rate, :healthfee_rate, :openbouns_value, :allrbouns_value, :responsiblebouns_value, :meal_value, :overtime1, :overtime2)"
# ,{
#     "workerfee_rate":workerfee_rate,
#     "healthfee_rate":healthfee_rate,
#     "openbouns_value":openbouns_value,
#     "allrbouns_value":allrbouns_value,
#     "responsiblebouns_value":responsiblebouns_value,
#     "meal_value":meal_value,
#     "overtime1":overtime1,
#     "overtime2":overtime2
# })




# # JOIN 顯示連接兩表
# a = conn.execute("SELECT employee.eid, employee.year, employee.month, overtime.overtimetotal FROM overtime LEFT JOIN employee ON overtime.eid = employee.eid")
# print(a.fetchall())


# a = conn.execute("SELECT * FROM overtime WHERE 1")
# print(a.fetchall())
# a = conn.execute("SELECT * FROM normal WHERE 1")
# print(a.fetchall())


#delete

# conn.execute("DELETE from normal WHERE eid = :eid",{'eid' : eid})
# conn.execute("DELETE from overtime WHERE eid = :eid", {'eid':eid})
# conn.execute("DELETE from basicinfo WHERE eid = :eid", {'eid':eid})
# conn.execute("DELETE from eventdata WHERE eid = :eid", {'eid':eid})


#update

#conn.execute("UPDATE basicinfo SET basicsalary = 30000 WHERE eid='A02'")


conn.commit()
conn.close()