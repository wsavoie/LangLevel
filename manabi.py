import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets, QtGui, QtCore, uic, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon,\
     QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QMessageBox
from PyQt5.QtCore import QSize

from preferences import p
import importlib
from UI import manabi_ui, morphemizerComboBox, aboutWindow, propertiesWindow, database_manager
import util
import platform

#pyuic5 -x manabi.ui -o manabi_ui.py



class MainWindowUI(manabi_ui.Ui_MainWindow):
    def __init__( self,mainwindow):
        '''Initialize the super class
        '''
        super().__init__()
        self.mw = mainwindow

        # QMainWindow.__init__(self)

    def setupUi(self):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(self.mw)
        # Init QSystemTrayIcon
        manabi_icon = QtGui.QIcon()
        manabi_icon.addFile('icons//test.png', QtCore.QSize(20,20))
        self.tray_icon = QSystemTrayIcon(self.mw)
        self.tray_icon.setIcon(manabi_icon)
        
        # self.tray_icon.setIcon(self.mw.style().standardIcon(QStyle.SP_ComputerIcon))
        # self.
        # self.actionExit = self.findChild(QtWidgets.QAction, "actionExit")
        # app.setQuitLockEnabled(False)
        #TODO maybe use qApp to find a closeEven thing
        app.aboutToQuit.connect(self.closeEvent)
        # self.mw.isminimized.connect(self.)
        # self.mw.showMinimized()
        '''
            Define and add steps to work with the system tray icon
            show - show window
            hide - hide window
            exit - exit from application
        '''    
        show_action = QAction("Show",self.mw)
        hide_action = QAction("Minimize to tray",self.mw)
        quit_action = QAction("Exit",self.mw)
        show_action.triggered.connect(self.mw.show)
        hide_action.triggered.connect(self.mw.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu(self.mw)
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addSeparator()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        '''
            initialize all values to values in property file

        '''
        
        self.minimize_to_tray.setChecked(p['DEFAULT'].getboolean('minimizetotray'))

        ##TODO create database from csv, load csv file open up a small editor window to highlight columns to traverse
        ##TODO readability for a subtitle fi
        '''
            set actions 
        '''
        self.minimize_to_tray.clicked['bool'].connect(lambda: util.on_check('minimizetotray'))

        '''set actions'''
        self.loaddb.clicked.connect(lambda: self.buttonz())
   
######################

        '''
            setup menus items
        '''
        self.actionProperties_2.triggered.connect(self.onProperties)
        self.actionAbout.triggered.connect(self.onAbout)
        self.actionDatabase_Manager.triggered.connect(self.onDatabase_Manager)
    
    def buttonz(self):
        import morphemes
        import morphemizer
        mdb=morphemes.MorphDb()
        mecab=morphemizer.MecabMorphemizer()
        mdb.load(r'C:\Users\WS\AppData\Roaming\Anki2\main\dbs\known.db')
    def onDatabase_Manager(self):
        database_manager.main(self.mw)
    def onProperties(self):
        propertiesWindow.main(self.mw)

    def onAbout(self):
        dialog = QtWidgets.QDialog(self.mw)
        about = aboutWindow.Ui_Dialog()
        about.setupUi(dialog)
        ver= 1.0
        about.versioningInfo.setText(f"Manabi version: {str(ver)} \nPython: {platform.python_version()}\nPyQt: {vars(Qt)['PYQT_VERSION_STR']}")
        about.manabi_pic.setPixmap(QtGui.QPixmap('icons//manabi.png'))
        dialog.show()
        
        # self.

        # c= aboutWindow.aboutDialog(self.mw)
        # cmain(self.mw)
       
        # c.exec_() 
    
    def closeEvent(self):
        p.write_prefs()
        #TODO add save all preferences to pref file
        
    # def closeEvent(self):
    #     print('hello from other close')
    def show_minimized_msg(self):
        self.tray_icon.showMessage(
            "Manabi",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            1500)
    def on_minimize(self):
        print(self.mw.isMinimized())

        if(self.mw.isMinimized()):
            if p['DEFAULT'].getboolean('minimize_to_tray'):
                self.mw.hide()


def main():
    # mw.mm = Morphman(mw)
    # mw.mm.show()
    # app = QtWidgets.QApplication(sys.argv)
    

    MainWindow = QtWidgets.QMainWindow()

    ui = MainWindowUI(MainWindow)
    ui.setupUi()

    if p['DEFAULT'].getboolean('open_minimized'):
        ui.mw.hide()
        ui.show_minimized_msg()
    else:
        ui.mw.show()
    
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main()
#     MainWindow = QtWidgets.QMainWindow()
#     ui = MainWindowUI(MainWindow)
#     ui.setupUi()
#     MainWindow.show()

    
    

    # # MainWindow = QtWidgets.QMainWindow()
    # app = QtWidgets.QApplication(sys.argv)
    # ui = MainWindowUI()
    # ui.setupUi()
    # ui.show()
    # sys.exit(app.exec_())
    




# class Ui_MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         QtWidgets.QMainWindow.__init__(self)
        
#     def setupUi(self):
#         MainWindow=self