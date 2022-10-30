from textwrap import fill
from tkinter import *
from tkinter import ttk
import customtkinter
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('employee_salary.db')
        self.cursor =  self.conn.cursor()

        self.eid = 'A01'
        self.eproperty = '工讀'
        self.ename	= 'yan'
        self.seniority = 0
        self.specialdayoff = 8
        self.basicsalary = 25250

    # @property
    # def get_imformation(self):
    #     return "{},{},{},{}".format(self.employee_id,self.employee_name, self.workhour, self.salary)

    #display
    def display(self):
        self.cursor.execute("SELECT eid, eproperty, ename, basicsalary FROM basicinfo WHERE 1")
        self.datacontainer = self.cursor.fetchall()

        return self.datacontainer
    #search
    #update
    #remove

#VIEW
#Main
class View_main(Frame):
    def __init__(self, master):
        super().__init__(master, width=1200, height=768, bg='gray', relief='flat')
        
        self.controller = None
        self.info_view = self.View_info(self)
        self.editting_view = self.View_editing(self)
        self.chart_view = self.View_chart(self)
        
        #布局layout
        self.info_view.grid(column=0,row=0,columnspan=1,ipadx=100,ipady=100, sticky=N+W)
        self.editting_view.grid(column=1, row=0, ipadx=100, ipady=100, sticky=N+E)
        self.chart_view.grid(column=1, row=1, ipadx=100, ipady=100, sticky=S+E)
        
        #button-event
        self.info_view.tree.bind('<Double-1>',self.info_click)

    def displayed(self):
        if self.controller:
            data =  self.controller.display()
            self.info_view.info_showsheet(data)
            print(data)
    
    def info_click(self,event):
        for selected_item in self.info_view.tree.selection():
            item = self.info_view.tree.item(selected_item)            
        record = item['values']
        print(event)
        self.show_edit(record)

    def show_edit(self,data):
        self.editting_view.default.destroy()
        self.editting_view.edit_id['text'] = data[0]
        self.editting_view.edit_name['text'] = data[1]
        self.editting_view.edit_workhour['text'] = data[2]
        self.editting_view.edit_salary['text'] = data[3]
        
    def set_controller(self, controller):
        self.controller = controller
        self.displayed()
        
    #set default view beforeclick info > editingview and chartview
    #set design done
    #infoview click event

    #nasted class-----------------------------------------------
    class View_info(Frame):
        def __init__(self, master):
            super().__init__(master, bg='blue', width=200, height=200)
            self.tree = ttk.Treeview(self, columns=('eid','eproperty' ,'ename' ,'basic_salary'), show='headings')
            self.tree.heading('eid', text='ID')
            self.tree.heading('eproperty', text='性質',anchor='nw')
            self.tree.heading('ename', text='姓名',anchor='nw')
            self.tree.heading('basic_salary', text='基本薪資',anchor='nw')  

        def info_showsheet(self, data):
            for i in data:
                self.tree.insert('', END, values=i)
            self.tree.pack(padx=0,pady=0)
            
    class View_editing(Frame):
        def __init__(self, master):
            super().__init__(master, bg='orange', width=500, height=200)

            self.eid = Label(self, text='編號',font=('Arial', 25))
            self.ename = Label(self, text='姓名',font=('Arial', 25))
            self.eworkhour = Label(self, text='工時',font=('Arial', 25))
            self.esalary = Label(self, text='薪水',font=('Arial', 25))
            self.default = Label(self, text='選擇一位員工進行編輯')
            self.default.grid(column=0,row=0,sticky=W+N)

            #layout
            self.eid.grid(column=0, row=0)
            self.ename.grid(column=1,row=0,sticky=N)
            self.eworkhour.grid(column=2,row=0,sticky=N)
            self.esalary.grid(column=3,row=0,sticky=N)
            
    class View_chart(Frame):
        def __init__(self, master):
            super().__init__(master, bg='blue', width=400, height=200)

    class View_setting(Toplevel):
        def __init__(self, master):
            super().__init__(master, bg='white', width=1200, height=200)
            self.setivew = Label(self,text='setview')
            self.setivew.pack(padx=0,pady=0,expand=TRUE)

    class View_check(Toplevel):
        def __init__(self, master):
            super().__init__(master)

    
    #nasted class-----------------------------------------------


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
        self.geometry('1200x768')
        #MODEL

        model = Model()
        
        #VIEW
        
        view_main = View_main(self)
        view_main.pack(padx=0,pady=0,ipadx=300,ipady=300,expand=TRUE)
        
        #CONTROLLER
        
        controller = Controller(model,view_main)
        view_main.set_controller(controller)

if __name__ == "__main__":
    
    app = App()
    app.mainloop()
