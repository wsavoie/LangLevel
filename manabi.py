import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QMessageBox
from PyQt5.QtCore import QSize

import manabi_ui
import importlib



#pyuic5 -x manabi.ui -o manabi_ui.py


class MainWindowUI(manabi_ui.Ui_MainWindow):
    def __init__( self ):
        '''Initialize the super class
        '''
        super().__init__()

        # QMainWindow.__init__(self)
        

    def errorMsg(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("error")
        msg.setText(text)
        msg.exec_()
        

    def setupUi(self,MainWindow):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(MainWindow)
        # Init QSystemTrayIcon
        manabi_icon = QtGui.QIcon()
        manabi_icon.addFile('test.png', QtCore.QSize(20,20))
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(manabi_icon)
        # self.
        # self.actionExit = self.findChild(QtWidgets.QAction, "actionExit")


        '''
            Define and add steps to work with the system tray icon
            show - show window
            hide - hide window
            exit - exit from application
        '''
        show_action = QAction("Show",MainWindow)
        quit_action = QAction("Exit",MainWindow)
        hide_action = QAction("Hide",MainWindow)
        show_action.triggered.connect(MainWindow.show)
        hide_action.triggered.connect(MainWindow.hide)
        # quit_action.triggered.connect(qApp.quit)
        # quit_action.triggered.connect(self.closeEvent)
        quit_action.triggered.connect(MainWindow.close)
       
        # show_action = QAction("Show",self)
        # quit_action = QAction("Exit",self)
        # hide_action = QAction("Hide",self)
        # show_action.triggered.connect(self.show)
        # hide_action.triggered.connect(self.hide)
        # quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
 
    def closeEvent(self,event):
        
        print('closeEvent')
        
        if self.minimize_to_tray.isChecked():
            
            event.ignore()
            MainWindow.hide()
            MainWindow.tray_icon.showMessage(
                "Manabi",
                "Application was minimized to Tray",
                QSystemTrayIcon.Information,
                2000
            )     

    # def closeEvent(self):
    #     print('hello from other close')

    

def main():
    # mw.mm = Morphman(mw)
    # mw.mm.show()
    print('hi')
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUI()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.errorMsg('err')
    
    sys.exit(app.exec_())

    # # MainWindow = QtWidgets.QMainWindow()
    # app = QtWidgets.QApplication(sys.argv)
    # ui = MainWindowUI()
    # ui.setupUi()
    # ui.show()
    # sys.exit(app.exec_())
    

main()


# class Ui_MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         QtWidgets.QMainWindow.__init__(self)
        
#     def setupUi(self):
#         MainWindow=self