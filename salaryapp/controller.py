from PyQt5.QtCore import QObject


class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def show_undoview(self):
        self.model.show_undoview()

    def undoview_clicked(self, index):
        self.model.undoview_clicked(index)
    
    def infodata_edit_clicked(self):
        self.model.infodata_edit_clicked()
        
    def infodata_done_clicked(self, listinfodata):
        self.model.infodata_done_clicked(listinfodata)

    def account_guide_checked(self, index):
        self.model.account_guide_checked(index)
    
    #def accountdata_clicked(self, listaccountdata):
    #    self.model.accountdata_clicked(listaccountdata)
        
    def create_account_clicked(self, dictdata):
        self.model.create_account_clicked(dictdata)
    
    def delete_account_clicked(self, dictdata):
        self.model.delete_account_clicked(dictdata)

    def preview_clicked(self, eid):
        self.model.preview(eid)

    def sumtotal(self):
        self.model.sumtotal()

    def get_date(self):
        self.model.get_date()

    def autocount(self, sum_data):
        self.model.autocount(sum_data)

    def close_account(self):
        self.model.close_account()

    def comboshow(self):
        self.model.comboshow()

    def selectdate(self, ym):
        self.model.selectdate(ym)