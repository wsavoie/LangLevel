from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ..util
import os
# from propertiesWindow_ui import Ui_Form
from .propertiesWindow_ui import Ui_Dialog
from preferences import p
#TODO fix this

sys.path.append("..") # Adds higher directory to python modules path.
# from manabi import MainWindowUI

class propertiesWindow(Ui_Dialog):
    def __init__(self,parent=None):
        self.parent=parent
        super(propertiesWindow,self).__init__()
        self.setupUi(parent)
        # self.tempPrefs = {}
    def setupUi(self, Form):
        super().setupUi(Form)
        self.tempPrefs = {}
        
        '''
            initialze all buttons in the basic tab
        '''
        #runShortcut, shortcut
        #X startMinimizedCheck
        #X properNounsCheck
        #X ignoreGrammarCheck
        
        # morphemizerButton
        # morphemizerPath
        self.setupCheck(self.startMinimizedCheck,'open_minimized')
        self.setupCheck(self.properNounsCheck, 'proper_nouns_known')
        self.setupCheck(self.ignoreGrammarCheck, 'ignoregrammarposition')



        '''
            initialze all buttons in the databases tab
        '''
        #TODO make a connection open 
        # dbFolderButton
        # dbFolderPath

        # lineEdit, caption, open_directory=False,startPath='',func=None
        self.dbFolderButton.clicked.connect(lambda: [None, util.getPath(self.dbFolderPath,'location of database folder',True), 
        self.setPrefText(self.dbFolderPath,'dbdir')][0])
        # frequencyButton
        # frequencyPath

        #db_list
        # up_db
        # down_db
        # add_db
        # del_db

        
        '''
            initialze all buttons in the import tab
        '''
        
        #X duo_check
        #X wk_check

        # wk_conn
        # duo_conn
         #X wk_api_token
        self.setupCheck(self.duo_check,'duo_check',
            lambda: [None, self.duo_username.setVisible(
                self.duo_check.isChecked()), self.duo_pass.setVisible(self.duo_check.isChecked()),self.duo_conn.setVisible(self.duo_check.isChecked())][0])
        self.setupCheck(self.wk_check,'wk_check',
            lambda: [None, self.wk_api_token.setVisible(self.wk_check.isChecked()), self.wk_conn.setVisible(self.wk_check.isChecked())][0])

        self.wk_api_token.editingFinished.connect(lambda: self.setPrefText(self.wk_api_token,'wk_api_key'))
        
        #TODO don't save password in plain text 
        self.duo_username.editingFinished.connect(lambda: self.setPrefText(self.duo_username,'duolingo_user'))
        self.duo_pass.editingFinished.connect(lambda: self.setPrefText(self.duo_pass,'duolingo_pass'))


        '''initialize values'''
        #X duo_username
        #X duo_pass
        #X wk_api_token
        self.duo_username.setText(p['DEFAULT']['duolingo_user'])
        self.duo_pass.setText(p['DEFAULT']['duolingo_pass'])
        self.wk_api_token.setText(p['DEFAULT']['wk_api_key'])


        self.duo_conn.setVisible(self.duo_check.isChecked())
        self.duo_username.setVisible(self.duo_check.isChecked())
        self.duo_pass.setVisible(self.duo_check.isChecked())
        self.wk_api_token.setVisible(self.wk_check.isChecked())
        self.wk_conn.setVisible(self.wk_check.isChecked())
        '''
            initialze all buttons in the anki tab
        '''
        # connectToAnki
        # ankiNoteTable
        


        # self.ignoreGrammarCheck.setChecked(p['DEFAULT'].getboolean('ignoregrammarposition'))
        # self.ignoreGrammarCheck.clicked['bool'].connect(lambda: util.on_check('ignoregrammarposition'))

        '''
            set actions 
        '''
        # self.runShortcut.setKeySequence()
        # QKeySequence().toString())
        self.applyCancelButton.clicked.connect(self.standardButtonPress)
        # self.applyCancelButton.setDefaultButton(QtWidgets.QDialogButtonBox.Apply)
        #  accepted.connect(self.applyChanges)
        
    def standardButtonPress(self, i):
        # QtWidgets.QPushButton.getText
        if i.text()=='Apply':
            self.applyChanges()
        else:        
            self.parent.close()
    def setPrefText(self, obj, prefName):
        '''send preference value to temp prefs '''
        self.tempPrefs[prefName]=obj.text()
    


        def applyChanges(self):
            print('applying changes')
            print(self.tempPrefs)
            for key,val in self.tempPrefs.items():
                p['DEFAULT'][key] = str(val)
            # self.tempPrefs.clear()

    def setupCheck(self,obj,prefName,func=None):
        """setup checkmark boxes, use func kwarg if you want to perform extra things"""
        obj.clicked['bool'].connect(lambda: [None, self.checkAction(obj, prefName),func()])
        obj.setChecked(p['DEFAULT'].getboolean(prefName))        
        self.tempPrefs[prefName]=obj.isChecked()

        

    #     obj.setChecked(p['DEFAULT'].getboolean(prefName))
        
    def checkAction(self,obj,prefName):
        self.tempPrefs[prefName]=obj.isChecked()
        # self.minimize_to_tray.clicked['bool'].connect(lambda: util.on_check('minimizetotray'))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = propertiesWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
def main(mainwindow):

    props = propertiesWindow(QtWidgets.QDialog(mainwindow))
    props.parent.show()