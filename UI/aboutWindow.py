# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QDialog
import platform
import sys

#TODO fix this
sys.path.append("..") # Adds higher directory to python modules path.
from manabi import MainWindowUI
# from .manabi import main
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


#be careful will overwrite file
#pyuic5 -x aboutWindow.ui -o aboutWindow_test.ui

ver = 1.0
# assert isinstance(MainWindowUI)
class aboutDialog(QDialog):
    def __init__(self,parent=None):
        self.parent=parent
        super(aboutDialog,self).__init__(self.parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(562, 466)
        # self.buttonBox = QtWidgets.QDialogButtonBox(self)
        # self.buttonBox.setGeometry(QtCore.QRect(130, 390, 341, 32))
        # self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        # self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        # self.buttonBox.setCenterButtons(True)
        # self.buttonBox.setObjectName("buttonBox")
        # self.buttonBox.clicked.connect(self.on_okay)
        self.authorinfo = QtWidgets.QLabel(self)
        self.authorinfo.setGeometry(QtCore.QRect(60, 320, 271, 111))
        self.authorinfo.setScaledContents(True)
        self.authorinfo.setWordWrap(False)
        self.authorinfo.setObjectName("authorinfo")
        self.manabi_pic = QtWidgets.QLabel(self)
        self.manabi_pic.setGeometry(QtCore.QRect(170, 30, 231, 111))
        self.manabi_pic.setPixmap(QtGui.QPixmap("..//icons//manabi.png"))
        self.manabi_pic.setScaledContents(True)
        self.manabi_pic.setObjectName("manabi_pic")
        self.programInfo = QtWidgets.QLabel(self)
        self.programInfo.setGeometry(QtCore.QRect(60, 150, 471, 71))
        self.programInfo.setWordWrap(True)
        self.programInfo.setObjectName("programInfo")
        self.versioningInfo = QtWidgets.QLabel(self)
        self.versioningInfo.setGeometry(QtCore.QRect(60, 260, 431, 16))
        self.versioningInfo.setScaledContents(True)
        self.versioningInfo.setObjectName("versioningInfo")

        self.okbutton = QtWidgets.QPushButton(self)
        self.okbutton.setGeometry(QtCore.QRect(240, 410, 75, 23))
        self.okbutton.setAutoDefault(True)
        self.okbutton.setObjectName("okbutton")
        self.okbutton.clicked.connect(self.on_okay)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    def on_okay(self):
        self.close()
    def setParent(self, parent):
        self.parent= parent
    def retranslateUi(self):
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.authorinfo.setText(_translate("Dialog", "<html><head/><body><p>Written by: Will Savoie</p><p><a href=\"https://github.com/wsavoie/Manabi\"><span style=\" text-decoration: underline; color:#0000ff;\">Visit Website</span></a></p></body></html>"))
        self.programInfo.setText(_translate("Dialog", "<html><head/><body><p>Manabi is a language independent, document readability analyzer. It\'s free and open source. This program was heavily influenced by the Anki <a href=\"https://ankiweb.net/shared/info/900801631\"><span style=\" text-decoration: underline; color:#0000ff;\">MorphMan</span></a> addon </p><p>Not currently licensed, so don\'t steal it. I\'ll have to figure that out later</p></body></html>"))
        self.versioningInfo.setText(_translate("Dialog", f"version info {ver} \n Python: {platform.python_version()} PyQt: {vars(Qt)['PYQT_VERSION_STR']}"))
        self.okbutton.setText(_translate("Dialog", "OK"))
        self.okbutton.setShortcut(_translate("Dialog", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = aboutDialog()
    ui.show()
    sys.exit(app.exec_())

def lol():
    print('im here')
def main(mainwindow):
    about = aboutDialog(mainwindow)
    about.show()