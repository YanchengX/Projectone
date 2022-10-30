from tkinter import *
import customtkinter
import sqlite3

#一進入畫面就select載入數據，如果editing才帶入salary...函數than編輯
#testing完在分區塊。

customtkinter.set_appearance_mode("dark")
#
customtkinter.set_default_color_theme("green")


class Model:
    def __init__(self):
        self.conn = sqlite3.connect('salary.db')
        self.cursor =  self.conn.cursor()
        self.salary = 0
        self.workhour = 0
        self.employee_name = 'default_name'
        self.employee_id = 'default_id'
        self.datacontainer = None

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        self._salary = value
    
    @property
    def workhour(self):
        return self._workhour
    @workhour.setter
    def workhour(self,hour):
        self._workhour = hour
    
    @property
    def employee_name(self):
        return self._employee_name
    @employee_name.setter
    def employee_name(self,name):
        self._employee_name = name

    @property
    def get_imformation(self):
        return "{},{},{}".format(self.employee_name, self.workhour, self.salary)


    #display
    def display(self):
        self.cursor.execute("SELECT * FROM salary WHERE 1")
        self.datacontainer = self.cursor.fetchall()

        return self.datacontainer
    #search
    #update
    #remove



#VIEW
#Main
class View_main(PanedWindow):
    #nasted class
    class View_info(PanedWindow):
        def __init__(self, master):
            super().__init__(master, showhandle=True, orient='vertical', relief='flat', bg='black', width=400, height=150)
            self.info_win = Frame(self, padx=10, pady=10, height=400, width=150)
            self.info_win1 = Frame(self, padx=10, pady=10, height=400, width=150)
            self.add(self.info_win)
            self.add(self.info_win1)

            self.tree = Treeview(self, columns=('id' ,'name' ,'workhour' ,'salary'), show='headings')
            self.tree.heading('id', text='ID')
            self.tree.heading('name', text='姓名')
            self.tree.heading('workhour', text='工時')
            self.tree.heading('salary', text='薪水')

        def info_showsheet(self,data):
            for i in data:
                self.tree.insert('', END, values=i[0])
            self.tree.pack()
            self.add(self.tree)

    class View_setting(PanedWindow):
        def __init__(self, master):
            super().__init__(master, showhandle=True, orient='vertical', relief='flat', bg='black', width=400, height=150)
            self.setting = Label(master, text='settingview')
            self.add(self.setting)

    class View_editing(PanedWindow):
        def __init__(self, master):
            super().__init__(master, showhandle=True, orient='vertical', relief='flat', bg='black', width=400, height=150)
            self.editing = Label(master, text='editingview')
            self.add(self.editing)

    class View_chart(PanedWindow):
        def __init__(self, master):
            super().__init__(master, showhandle=True, orient='vertical', relief='flat', bg='pink', width=400, height=150)
            self.chart = Label(master, text='chartview')
            self.add(self.chart)

#init    
    def __init__(self, master):
        super().__init__(master, showhandle=True, width=1200, height=800)
        
        #layout
        self.view_info = self.View_info(master) #master = tk
        self.view_setting = self.View_setting(master)
        self.view_editing = self.View_editing(master)
        self.view_chart = self.View_chart(master)
        
        self.view_info.add(self.view_setting)
        self.view_editing.add(self.view_chart)

        self.add(self.view_info)
        self.add(self.view_editing)
        
        self.inf = ''

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        self.displayed()

    def displayed(self):
        if self.controller:
            data =  self.controller.display()
            # self.view_info.info_showsheet(data)
            print(data)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    #call model to show info
    def display(self):
        try:
            return self.model.display()
        except ValueError as error:
            print(error)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Salary_System')
        self.geometry('800x600')
        
        #MODEL
        model = Model()
        print(model.get_imformation)

        #VIEW
        view_main = View_main(self)

        view_main.pack(padx=10,pady=10)
        #CONTROLLER
        controller = Controller(model,view_main)
        view_main.set_controller(controller)


if __name__ == "__main__":
    
    app = App()
    app.mainloop()