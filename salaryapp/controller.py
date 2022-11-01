from PyQt5.QtCore import QObject


class MainController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view


    def show_undoview(self):
        self.model.show_undoview()
        self.view.show_undoview()
        
    def preview(self):
        self.model.preview()