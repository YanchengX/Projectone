#for practicing sqlite3 in future Model.
import sqlite3
#connect DB
connection = sqlite3.connect('salary.db')

#cursor座標 to do CRUD and so on..
c = connection.cursor()

# #CREATE
# c.execute("""CREATE TABLE salary(
#     id text,
#     name text,
#     workhour integer,
#     salary integer
# )""")

# #commit 保存至db庫 and close
# connection.commit()
# connection.close

# READ - SELECT

# c.execute("SELECT * FROM employee WHERE 1")
# c.execute("SELECT * FROM employee WHERE employee_name=:employee_name",{'employee_name': employee_name})

# #Update

# c.execute("")

# conn = sqlite3.connect(':memory:')
# c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""")

#insert 

c.execute("INSERT INTO salary VALUES (:id ,:name, :workhour, :salary)", {'id':'A02','name':'Yan','workhour':150,'salary':69696969})
connection.commit()
connection.close()
# #read select
# def get_emps_by_name(lastname):
#     c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
#     return c.fetchall()

# #update
# def update_pay(emp, pay):
#     with conn:
#         c.execute("""UPDATE employees SET pay = :pay
#                     WHERE first = :first AND last = :last""",
#                   {'first': emp.first, 'last': emp.last, 'pay': pay})
# #remove
# def remove_emp(emp):
#     with conn:
#         c.execute("DELETE from employees WHERE first = :first AND last = :last",
#                   {'first': emp.first, 'last': emp.last})
