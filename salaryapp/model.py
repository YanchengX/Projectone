import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal, QStringListModel

class Model(QStringListModel):
    def __init__(self):
        super(Model, self).__init__()
        self.conn = sqlite3.connect('employee_salary.db')
        self.cursor = self.conn.cursor()

        self.click_emp = pyqtSignal()

        # counting py 的變數套入
        
    def show_undoview(self):
        self.cursor.execute('SELECT * FROM basicinfo WHERE 1')
        self.data = self.cursor.fetchall()
        
        self.strdata = []
        for tupledata in self.data: #(a,3,7,8,,54,3)
            tmp = ''
            for i in range(3):
                tmp += ''.join(tupledata[i])
                tmp += ''.join(' / ')
            self.strdata.append(tmp)

        # = return的意思
        self.setStringList(self.strdata)

    def preview(self):
        print('fuck you')