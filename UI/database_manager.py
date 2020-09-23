from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import util

# from propertiesWindow_ui import Ui_Form
from .database_manager_ui import Ui_Dialog

#TODO fix this

sys.path.append("..") # Adds higher directory to python modules path.
# from manabi import MainWindowUI

class databaseWindow(Ui_Dialog):
    def __init__(self,parent=None):
        self.parent=parent
        super(databaseWindow,self).__init__()
        self.setupUi(parent)

    def setupUi(self, Form):
        super().setupUi(Form)
        '''
            initialize all values to values in property file

        '''

        '''
            set actions 
        '''
        # self.minimize_to_tray.clicked['bool'].connect(lambda: util.on_check('minimizetotray'))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = databaseWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
def main(mainwindow):
    
    db = databaseWindow(QtWidgets.QDialog(mainwindow))
    db.parent.show()