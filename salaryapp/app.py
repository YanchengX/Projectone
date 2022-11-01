#main_app
import sys
from PyQt5 import QtWidgets

from model import Model
from mainviewy import MainView
from controller import MainController

class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        
        self.model = Model()

        self.main_view = MainView(self.model)
        self.main_view.show()

        self.maincontroller = MainController(self.model, self.main_view)
        self.main_view.setcontroller(self.maincontroller)
if __name__ == "__main__":

    app = App(sys.argv)
    sys.exit(app.exec_())
