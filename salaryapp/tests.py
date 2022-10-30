import re
import tkinter as tk
from tkinter import ttk

#model模型處理邏輯運算
class Model:
    #初始化且輸入em
    def __init__(self, email):
        self.email = email
        
    #回傳em propterty只能讀取不能作為使用
    @property
    def email(self):
        return self.__email #雙底線

    #email 設定
    @email.setter
    def email(self, value):

        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        #fullmatch(匹配要求,字串)
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    #儲存em動作到em.txt
    def save(self):

        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')


#視圖，設計使用者介面與之溝通。
class View(ttk.Frame):
    #繼承父類別ttk.frame可以使用物件button,lebel等等
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)
        
        # ###讓使用者可以輸入字串in entry
        #如果將textvariable設置為其他字串則一開始確為entry為''

        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=50)
        #sticky=置中
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button 如果被點擊就觸發controller指示
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        #預設控制器函數
        self.controller = None

    #控制器方法 設定控制器 最後在Class app 在init被呼叫
    #設定控制器給view使用作資料來回後回傳給user
    def set_controller(self, controller):

        self.controller = controller
    #button點擊儲存listener
    def save_button_clicked(self):
        print(self.controller)
        #如果app有給予controller且為真 則Controller.save方法之後通知model進行model.save方法
        if self.controller:
            self.controller.save(self.email_var.get())
    #回傳錯誤
    def show_error(self, message):

        #設定msglabel
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        #2.5秒後隱藏訊息 after為tktiner方法 可以要求幾秒後執行甚麼事情
        self.message_label.after(2500, self.hide_message)
        self.email_entry['foreground'] = 'red'

    #回傳成功
    def show_success(self, message):

        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(2500, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')
    #設定隱藏該訊息 將label改為空字串即可
    def hide_message(self):

        self.message_label['text'] = ''            


#使用者操作Controller行為與model互動並view回傳給使用者
class Controller:
    #初始化模型與視圖 呼叫模型進行運算回傳再將資料給view回傳給user
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #當使用者成功save則呼叫model做save方法(作為呼叫控制)
    def save(self, email):

        try:
        #try如果成功，Model em值更改且save該em到資料庫(txt)必回傳視圖view成功畫面
            self.model.email = email
            self.model.save()
            self.view.show_success(f'The email {email} saved!')

        #如有例外就回傳該意外給視圖show給user
        except ValueError as error:
            # show an error message
            self.view.show_error(error)        

        #else:  如果完全沒錯
        #finally:不管如何都執行

#main完整App介面綜合MVC使用
class App(tk.Tk):
    #繼承父類別Tk才可使用tkinter並呼叫app執行
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        #新增一個模型且給所需參數email
        model = Model('adsf@sdf.aaa')

        #新增一個視圖並定位在00格
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        #新增一個控制器輸入模型與視圖參數預備使用
        #可以控制model1 model2 view1 view2 提高自由性
        controller = Controller(model, view)

        #定位這個控制器給view做使用
        view.set_controller(controller)

if __name__ == '__main__':
    #主程式呼叫
    app = App()
    app.mainloop()            