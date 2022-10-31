#main_app
import sys
from PyQt5 import QtCore, QtWidgets

from model import Model
from mainviewy import MainView
from controller import MainController

class MainController(QtCore.QObject):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view

class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        
        self.model = Model()

        self.main_view = MainView()
        self.main_view.show()
            
        self.maincontroller = MainController(self.model, self.main_view)
        self.main_view.set_controller(self.maincontroller)

if __name__ == "__main__":

    app = App(sys.argv)
    sys.exit(app.exec_())
