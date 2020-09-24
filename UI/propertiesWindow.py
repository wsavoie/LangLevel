from PyQt5 import QtCore, QtGui, QtWidgets

import sys
# import ..util
import os
# from propertiesWindow_ui import Ui_Form
from .propertiesWindow_ui import Ui_Dialog
from preferences import p

#TODO fix the line below
sys.path.append("..") # Adds higher directory to python modules path.
# from manabi import MainWindowUI
import util

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
         ####################BASIC#######################
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

        '''initialize values'''




        '''
        ####################DATABASES#######################
            initialze all buttons in the DATABASES tab
        '''
     
        # dbFolderButton
        # dbFolderPath
        
        self.dbFolderButton.clicked.connect(lambda: [None, getPath(self.dbFolderPath,'location of database folder',True), 
        self.setPrefText(self.dbFolderPath,'dbdir')][0])



        # self.dbFolderButton.clicked.connect(lambda le: getPath(self.dbFolderPath,'location of database folder',True))
        # frequencyButton
        # frequencyPath
        self.frequencyButton.clicked.connect(lambda: [None, getPath(self.frequencyPath,'language frequency file',False,
            startPath=os.path.normpath(self.dbFolderPath.text()),filter_='text file (*.txt)'), 
        self.setPrefText(self.frequencyPath,'frequencylist')][0])
        #db_list
        # up_db
        # down_db
        # add_db
        # del_db

        self.add_db.clicked.connect(lambda: self.addDb())

        self.up_db.clicked.connect(lambda: self.changeDbPos(-1))
        self.down_db.clicked.connect(lambda: self.changeDbPos(1))
        self.del_db.clicked.connect(lambda: self.deleteDb())
        
        print('db list length',len(self.db_list))

        ''' initialize values '''
        self.dbFolderPath.setText(p['DEFAULT']['dbdir'])
        self.frequencyPath.setText(p['DEFAULT']['frequencylist'])
        self.initListWidget(self.db_list,'database_union')
        #TODO propagate database to external list



        '''
        ####################IMPORT#######################
            initialze all buttons in the IMPORT tab
        '''
        #TODO make a connection open button thing
        #X duo_check
        #X wk_check
        # wk_db_label
        # wk_db_name
        # wk_conn
        # duo_conn
         #X wk_api_token
        self.setupCheck(self.duo_check,'duo_check',
            lambda: [None, self.duo_username.setEnabled(self.duo_check.isChecked()),
                self.duo_pass.setEnabled(self.duo_check.isChecked()),self.duo_conn.setEnabled(self.duo_check.isChecked()), 
                self.duo_label.setEnabled(self.duo_check.isChecked()), self.duo_db_name.setEnabled(self.duo_check.isChecked())][0])
        
        self.setupCheck(self.wk_check,'wk_check',
            lambda: [None, self.wk_api_token.setEnabled(self.wk_check.isChecked()), self.wk_conn.setEnabled(self.wk_check.isChecked()),
            self.wk_label.setEnabled(self.wk_check.isChecked()),self.wk_db_name.setEnabled(self.wk_check.isChecked())][0])

        self.wk_api_token.editingFinished.connect(lambda: self.setPrefText(self.wk_api_token,'wk_api_key'))
        self.wk_db_name.editingFinished.connect(lambda: self.setPrefText(self.wk_db_name,'wk_db_name'))

        #TODO don't save password in plain text 
        self.duo_username.editingFinished.connect(lambda: self.setPrefText(self.duo_username,'duolingo_user'))
        self.duo_pass.editingFinished.connect(lambda: self.setPrefText(self.duo_pass,'duolingo_pass'))
        self.duo_db_name.editingFinished.connect(lambda: self.setPrefText(self.duo_db_name,'duo_db_name'))

        '''initialize values'''
        #X duo_username
        #X duo_pass
        #X wk_api_token
        self.duo_username.setText(p['DEFAULT']['duolingo_user'])
       
        self.wk_db_name.setText(p['DEFAULT']['wk_db_name'])
        self.duo_db_name.setText(p['DEFAULT']['duo_db_name'])

        # util.retrive_pass()
        #TODO do not store plaintext version
        self.wk_api_token.setText(p['DEFAULT']['wk_api_key'])
        self.duo_pass.setText(p['DEFAULT']['duolingo_pass'])

        # self.duo_conn.setVisible(self.duo_check.isChecked())

        self.duo_conn.setEnabled(self.duo_check.isChecked())
        self.duo_username.setEnabled(self.duo_check.isChecked())
        self.duo_pass.setEnabled(self.duo_check.isChecked())
        self.duo_label.setEnabled(self.duo_check.isChecked())
        self.duo_db_name.setEnabled(self.duo_check.isChecked())
        self.wk_api_token.setEnabled(self.wk_check.isChecked())
        self.wk_conn.setEnabled(self.wk_check.isChecked())
        self.wk_label.setEnabled(self.wk_check.isChecked())
        self.wk_db_name.setEnabled(self.wk_check.isChecked())
        
        '''
        ####################ANKI#######################
            initialze all buttons in the ANKI tab
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
    def initListWidget(self,db,prefName):
        dbstr=p['DEFAULT'][prefName]
        paths=dbstr.split('|')
        for path in paths:
            db.addItem(os.path.normpath(path))
    def deleteDb(self):
        self.db_list.takeItem(self.db_list.currentRow())
        self.tempPrefs['database_union'] = self.getDbString(self.db_list)

    def addDb(self):
        paths= getPath2(self.db_list,'db files',False,startPath=os.path.normpath(self.dbFolderPath.text()), filter_='Database file(s) (*.db)')
        print(paths)
        for path in paths:
            self.db_list.addItem(os.path.normpath(path))
        self.tempPrefs['database_union']=self.getDbString(self.db_list)
    def getDbString(self,db):
        dbstr=''
        for i in range(len(db)):
            # print(db.item(i).text())
            dbstr+= db.item(i).text() + '|'
        return dbstr[:-1]
    def changeDbPos(self, dir_):
        '''change load order of databases'''
        CR=self.db_list.currentRow()
        
        if ((CR + dir_) >= 0) and ((CR+dir_) < len(self.db_list)):
            CI=self.db_list.takeItem(CR)
            self.db_list.insertItem(CR + dir_, CI)
            self.db_list.setCurrentRow(CR+dir_)
            # self.db_list.takeItem(CR)
            self.tempPrefs['database_union']=self.getDbString(self.db_list)
        else:
            return  
    
    def standardButtonPress(self, buttonText):
        '''apply or close button press'''
        # QtWidgets.QPushButton.getText
        if buttonText.text()=='Apply':
            self.applyChanges()
        else:        
            self.parent.close()

    def setPrefText(self, obj, prefName):
        '''send preference value to temp prefs '''
        self.tempPrefs[prefName]=obj.text()
    
    def downArrow(self):
        lambda: self.db_list.currentIndex(min(len(self.db_list),self.db_list.currentIndex()+1))
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


def getPath(lineEdit, caption, open_directory=False,startPath='',filter_=''):  # LineEdit -> GUI ()
    '''get database files from explorer add them to lineEdit'''
    try:
        if open_directory:
            path =  QtWidgets.QFileDialog.getExistingDirectory(caption=caption, directory=startPath,
                        options=QtWidgets.QFileDialog.ShowDirsOnly)
        else:
            path = QtWidgets.QFileDialog.getOpenFileName(caption=caption, directory=startPath, filter=filter_)[0]
    except Exception as e:
        print(e)
        return

    if path:
        lineEdit.setText(path)

def getPath2(listWid,caption, open_directory=False,startPath='',filter_=''):  # LineEdit -> GUI ()
    '''get database files from explorer for use when adding to line widget'''
    try:
        paths = QtWidgets.QFileDialog.getOpenFileNames(caption=caption, directory=startPath, filter=filter_)[0]
        # print(paths)
    except Exception as e:
        print(e)
        return
    
    return paths


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