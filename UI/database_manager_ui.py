# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database_manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 498)
        self.dbAPath = QtWidgets.QLineEdit(Dialog)
        self.dbAPath.setGeometry(QtCore.QRect(40, 40, 113, 20))
        self.dbAPath.setObjectName("dbAPath")
        self.dbBPath = QtWidgets.QLineEdit(Dialog)
        self.dbBPath.setGeometry(QtCore.QRect(40, 70, 113, 20))
        self.dbBPath.setObjectName("dbBPath")
        self.AFileButton = QtWidgets.QToolButton(Dialog)
        self.AFileButton.setGeometry(QtCore.QRect(10, 40, 25, 19))
        self.AFileButton.setObjectName("AFileButton")
        self.BFileButton = QtWidgets.QToolButton(Dialog)
        self.BFileButton.setGeometry(QtCore.QRect(10, 70, 25, 19))
        self.BFileButton.setObjectName("BFileButton")
        self.showA = QtWidgets.QPushButton(Dialog)
        self.showA.setGeometry(QtCore.QRect(11, 126, 31, 23))
        self.showA.setObjectName("showA")
        self.showB = QtWidgets.QPushButton(Dialog)
        self.showB.setEnabled(True)
        self.showB.setGeometry(QtCore.QRect(50, 130, 31, 23))
        self.showB.setObjectName("showB")
        self.ADiffB = QtWidgets.QPushButton(Dialog)
        self.ADiffB.setGeometry(QtCore.QRect(11, 160, 75, 23))
        self.ADiffB.setObjectName("ADiffB")
        self.BDiffA = QtWidgets.QPushButton(Dialog)
        self.BDiffA.setGeometry(QtCore.QRect(11, 194, 75, 23))
        self.BDiffA.setObjectName("BDiffA")
        self.symmetricDiff = QtWidgets.QPushButton(Dialog)
        self.symmetricDiff.setGeometry(QtCore.QRect(11, 228, 77, 23))
        self.symmetricDiff.setObjectName("symmetricDiff")
        self.ABUnion = QtWidgets.QPushButton(Dialog)
        self.ABUnion.setGeometry(QtCore.QRect(11, 262, 75, 23))
        self.ABUnion.setObjectName("ABUnion")
        self.ABIntersection = QtWidgets.QPushButton(Dialog)
        self.ABIntersection.setGeometry(QtCore.QRect(11, 296, 75, 23))
        self.ABIntersection.setObjectName("ABIntersection")
        self.morphemizerBox = QtWidgets.QComboBox(Dialog)
        self.morphemizerBox.setGeometry(QtCore.QRect(10, 340, 69, 22))
        self.morphemizerBox.setObjectName("morphemizerBox")
        self.extractMorphemes = QtWidgets.QPushButton(Dialog)
        self.extractMorphemes.setGeometry(QtCore.QRect(10, 380, 151, 23))
        self.extractMorphemes.setObjectName("extractMorphemes")
        self.saveResults = QtWidgets.QPushButton(Dialog)
        self.saveResults.setGeometry(QtCore.QRect(10, 410, 141, 23))
        self.saveResults.setObjectName("saveResults")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(190, 30, 241, 401))
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(490, 10, 47, 13))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(440, 30, 161, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 71, 16))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(0)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dbAPath.setPlaceholderText(_translate("Dialog", "database A path"))
        self.dbBPath.setPlaceholderText(_translate("Dialog", "database B path"))
        self.AFileButton.setText(_translate("Dialog", "..."))
        self.BFileButton.setText(_translate("Dialog", "..."))
        self.showA.setText(_translate("Dialog", "A"))
        self.showB.setText(_translate("Dialog", "B"))
        self.ADiffB.setText(_translate("Dialog", "A Diff B"))
        self.BDiffA.setText(_translate("Dialog", "B Diff A"))
        self.symmetricDiff.setText(_translate("Dialog", "Symmetric Diff"))
        self.ABUnion.setText(_translate("Dialog", "Union"))
        self.ABIntersection.setText(_translate("Dialog", "Intersection"))
        self.extractMorphemes.setText(_translate("Dialog", "Extract morphemes from file"))
        self.saveResults.setText(_translate("Dialog", "Save results to db"))
        self.label.setText(_translate("Dialog", "Summary"))
        self.label_2.setText(_translate("Dialog", "Database Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
