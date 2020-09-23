# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 466)
        self.authorinfo = QtWidgets.QLabel(Dialog)
        self.authorinfo.setGeometry(QtCore.QRect(60, 320, 271, 111))
        self.authorinfo.setScaledContents(True)
        self.authorinfo.setWordWrap(False)
        self.authorinfo.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.authorinfo.setObjectName("authorinfo")
        self.manabi_pic = QtWidgets.QLabel(Dialog)
        self.manabi_pic.setGeometry(QtCore.QRect(170, 30, 231, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manabi_pic.sizePolicy().hasHeightForWidth())
        self.manabi_pic.setSizePolicy(sizePolicy)
        self.manabi_pic.setText("")
        self.manabi_pic.setPixmap(QtGui.QPixmap("../icons/manabi.png"))
        self.manabi_pic.setScaledContents(True)
        self.manabi_pic.setObjectName("manabi_pic")
        self.programInfo = QtWidgets.QLabel(Dialog)
        self.programInfo.setGeometry(QtCore.QRect(60, 150, 471, 71))
        self.programInfo.setWordWrap(True)
        self.programInfo.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.programInfo.setObjectName("programInfo")
        self.okbutton = QtWidgets.QPushButton(Dialog)
        self.okbutton.setGeometry(QtCore.QRect(240, 410, 75, 23))
        self.okbutton.setAutoDefault(True)
        self.okbutton.setObjectName("okbutton")
        self.versioningInfo = QtWidgets.QLabel(Dialog)
        self.versioningInfo.setGeometry(QtCore.QRect(60, 255, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versioningInfo.sizePolicy().hasHeightForWidth())
        self.versioningInfo.setSizePolicy(sizePolicy)
        self.versioningInfo.setLineWidth(1)
        self.versioningInfo.setScaledContents(True)
        self.versioningInfo.setIndent(-4)
        self.versioningInfo.setObjectName("versioningInfo")

        self.retranslateUi(Dialog)
        self.okbutton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.authorinfo.setText(_translate("Dialog", "<html><head/><body><p>Written by: Will Savoie</p><p><a href=\"https://github.com/wsavoie/Manabi\"><span style=\" text-decoration: underline; color:#0000ff;\">Visit Website</span></a></p></body></html>"))
        self.programInfo.setText(_translate("Dialog", "<html><head/><body><p>Manabi is a language independent, document readability analyzer. It\'s free and open source. This program was heavily influenced by the Anki <a href=\"https://ankiweb.net/shared/info/900801631\"><span style=\" text-decoration: underline; color:#0000ff;\">MorphMan</span></a> addon </p><p>Not currently licensed, so don\'t steal it. I\'ll have to figure that out later</p></body></html>"))
        self.okbutton.setText(_translate("Dialog", "OK"))
        self.okbutton.setShortcut(_translate("Dialog", "Return"))
        self.versioningInfo.setText(_translate("Dialog", "Version blah"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
