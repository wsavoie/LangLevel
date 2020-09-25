from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys

import os
# from propertiesWindow_ui import Ui_Form
from .database_manager_ui import Ui_Dialog
from preferences import p



#TODO fix this
sys.path.append("..") # Adds higher directory to python modules path.
from morphemes import MorphDb
from morphemizer import getAllMorphemizers
from util import errorMsg, getPathLE,CopySelectedCellsAction
from UI import morphemizerComboBox 
#TODO make sure language is set somewhere, add a combobox class 


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
        # AFileButton     
        # BFileButton
        # dbAPath
        # dbBPath
        # showA
        # showB
        # ADiffB
        # BDiffA
        # symmetricDiff
        # ABUnion
        # ABIntersection
        # morphemizer
        # extractMorphemes
        # saveResults
        
        # onlyWords
        # fullInfo

        # dbTable
        # dbInfo

        self.AFileButton.clicked.connect(lambda: [None, getPathLE(self.dbAPath,'location of database file',False,
            startPath=os.path.normpath(p['DEFAULT']['dbdir']),filter_='database dir (*.db)')][0])
        self.BFileButton.clicked.connect(lambda: [None, getPathLE(self.dbBPath,'location of database file',False,
            startPath=os.path.normpath(p['DEFAULT']['dbdir']),filter_='database dir (*.db)')][0])


        self.showA.clicked.connect(self.onShowA)
        self.showB.clicked.connect(self.onShowB)

        #comparisons
        self.ADiffB.clicked.connect(lambda: self.DbInteractions('A-B'))
        self.BDiffA.clicked.connect(lambda: self.DbInteractions('B-A'))
        self.symmetricDiff.clicked.connect(lambda: self.DbInteractions('sym'))
        self.ABUnion.clicked.connect(lambda: self.DbInteractions('union'))
        self.ABIntersection.clicked.connect(lambda: self.DbInteractions('inter'))

        self.extractMorphemes.clicked.connect(self.onExtractTxtFile)
        self.saveResults.clicked.connect(self.onSaveResults)


        self.db = None

        self.morphemizerComboBox = morphemizerComboBox.MorphemizerComboBox()
        self.morphemizerComboBox.setMorphemizers(getAllMorphemizers())
        
        self.fullInfo.clicked.connect(self.colModeButtonListener)
        self.onlyMorphs.clicked.connect(self.colModeButtonListener)
        '''
            set actions 
        '''
        self.dbTable.addAction(CopySelectedCellsAction(self.dbTable))
        # util.CopySelectedCellsAction()
    def onSaveResults(self):
        pass
        #TODO add method

    #     dir_path = cfg('path_dbs') + os.sep + 'results.db'
    #     destPath = QFileDialog.getSaveFileName(caption='Save results to?', directory=dir_path)[0]
    #     if not destPath:
    #         return
    #     if not hasattr(self, 'db'):
    #         return errorMsg('No results to save')
    #     self.db.save(str(destPath))
    #     infoMsg('Saved successfully')
    def onExtractTxtFile(self):
        pass
        #TODO add method
        #TODO add open on drag
    
        # srcPath = QFileDialog.getOpenFileName(caption='Text file to extract from?', directory=cfg('path_dbs'))[0]
        # if not srcPath:
        #     return

        # destPath = QFileDialog.getSaveFileName(
        #            caption='Save morpheme db to?', directory=cfg('path_dbs') + os.sep + 'textFile.db')[0]
        # if not destPath:
        #     return

        # mat = cfg('text file import maturity')
        # db = MorphDb.mkFromFile(str(srcPath), self.morphemizerComboBox.getCurrent(), mat)
        # if db:
        #     db.save(str(destPath))
        #     infoMsg('Extracted successfully')
    def DbInteractions(self, kind):
        try:
            self.loadAB()
        except Exception as e:
            return errorMsg('Can\'t load dbs:\n%s' % e)

        a_set = set(self.aDb.db.keys())
        b_set = set(self.bDb.db.keys())
        if kind == 'sym':
            ms = a_set.symmetric_difference(b_set)
        elif kind == 'A-B':
            ms = a_set.difference(b_set)
        elif kind == 'B-A':
            ms = b_set.difference(a_set)
        elif kind == 'inter':
            ms = a_set.intersection(b_set)
        elif kind == 'union':
            ms = a_set.union(b_set)
        else:
            raise ValueError("'kind' must be one of [sym, A-B, B-A, inter, union], it was actually '%s'" % kind)

        self.db.clear()
        for m in ms:
            locs = set()
            if m in self.aDb.db:
                locs.update(self.aDb.db[m])
            if m in self.bDb.db:
                locs.update(self.bDb.db[m])
            self.db.addMLs1(m, locs)

        self.updateDisplay()

    def loadA(self):
        self.aPath = self.dbAPath.text()
        self.aDb = MorphDb(path=self.aPath)
        if not self.db:
            self.db = self.aDb

    def loadB(self):
        self.bPath = self.dbBPath.text()
        self.bDb = MorphDb(path=self.bPath)

    def loadAB(self):
        self.loadA()
        self.loadB()

    def onShowA(self):
        try:
            self.loadA()
        except Exception as e:
            return errorMsg(f"Cannot load db:\n {e}")
        self.db = self.aDb
        self.updateDisplay()

    def onShowB(self):
        try:
            self.loadB()
        except Exception as e:
            return errorMsg(f"Cannot load db:\n {e}")
        self.db = self.bDb
        self.updateDisplay()

    def colModeButtonListener(self):
        # colModeButton = self.sender()
        # if colModeButton.isChecked():
        try:
            self.updateDisplay()
        except AttributeError:
            return  # User has not selected a db view yet

    def updateDisplay(self):
        # # num_cols = get from a morpehme component
        # num_cols = 6
        # cols=['']
        # if num_cols == 6: #mecab
        #     #name columns
        #     cols=['norm base', 'base', 'inflected', 'reading', 'POS','subPOS', 'freq']
        # else:
        #     cols=[f"{i}" for i in range(7)]
        self.dbTable.clear()
        self.posTable.clear()
        self.dbTable.setRowCount(len(self.db.db.items()))
        if self.fullInfo.isChecked():

            # self.dbTable.setText(self.db.showMs())
            #  return sorted(self.db.items(), key=lambda it: it[0].show()))
            self.dbTable.setColumnCount(7)
            self.dbTable.setHorizontalHeaderLabels(['norm base', 'base', 'inflected', 'reading', 'POS','subPOS', 'freq'])
            # errorMsg('yo')
            for i,m in enumerate(self.db.showMsList()):
                # freq= len(m[1])
                self.addRow(self.dbTable,i,[m[0].norm, m[0].base, m[0].inflected, m[0].read, m[0].pos, m[0].subPos,str(len(m[1]))])            
    
        else:
            self.dbTable.setColumnCount(1)
            self.dbTable.setHorizontalHeaderLabels(['morphs'])
            for i,m in enumerate(self.db.showMsList()):
                self.addRow(self.dbTable,i,[m[0].norm]) 
            # self.dbTable.setText('\n'.join(sorted(list(set([m.norm for m in self.db.db])))))
        self.db.analyze()

        
        self.summaryLabel.setText(f'Total normalized morphemes: {self.db.kCount}\nTotal variations: {self.db.vCount}\nBy part of speech:')
 
        self.posTable.setColumnCount(3)
        self.posTable.setHorizontalHeaderLabels(['Total',r'% of Total','POS'])
        self.posTable.setRowCount(len(self.db.posBreakdown.items()))  
        for i,k in enumerate(self.db.posBreakdown.items()):
            self.addRow(self.posTable,i,[str(k[1]), str(int(100. * k[1] / self.db.vCount)),k[0]]) 
    def addRow(self,table_,rowInd,vals):
        for i in range(len(vals)):
            table_.setItem(rowInd,i,QtWidgets.QTableWidgetItem(vals[i]))
def getProgressWidget():
    progressWidget = QtWidgets.QWidget()
    progressWidget.setFixedSize(400, 70)
    progressWidget.setWindowModality(Qt.WindowModal)
    bar = QtWidgets.QProgressBar(progressWidget)

    #TODO add utils function to determine OS
    isMac = False
    #
    if isMac:
        bar.setFixedSize(380, 50)
    else:
        bar.setFixedSize(390, 50)
    bar.move(10, 10)
    per = QtWidgets.QLabel(bar)
    per.setAlignment(Qt.AlignCenter)
    progressWidget.show()
    return progressWidget, bar



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