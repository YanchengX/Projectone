from PyQt5.QtCore import QObject


class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def show_undoview(self):
        self.model.show_undoview()

    def undoview_clicked(self):
        self.model.undoview_clicked()

    def preview(self):
        self.model.preview()
