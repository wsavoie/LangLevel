# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertiesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 500)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 461, 431))
        self.tabWidget.setStatusTip("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.basicTab = QtWidgets.QWidget()
        self.basicTab.setObjectName("basicTab")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.basicTab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 241, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.runShortcut = QtWidgets.QKeySequenceEdit(self.horizontalLayoutWidget_2)
        self.runShortcut.setKeySequence("")
        self.runShortcut.setObjectName("runShortcut")
        self.horizontalLayout_2.addWidget(self.runShortcut)
        self.properNounsCheck = QtWidgets.QCheckBox(self.basicTab)
        self.properNounsCheck.setGeometry(QtCore.QRect(10, 140, 151, 17))
        self.properNounsCheck.setObjectName("properNounsCheck")
        self.ignoreGrammarCheck = QtWidgets.QCheckBox(self.basicTab)
        self.ignoreGrammarCheck.setGeometry(QtCore.QRect(10, 160, 151, 17))
        self.ignoreGrammarCheck.setStatusTip("")
        self.ignoreGrammarCheck.setWhatsThis("")
        self.ignoreGrammarCheck.setObjectName("ignoreGrammarCheck")
        self.label_11 = QtWidgets.QLabel(self.basicTab)
        self.label_11.setGeometry(QtCore.QRect(10, 190, 111, 16))
        self.label_11.setObjectName("label_11")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.basicTab)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 210, 160, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.morphemizerButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_10)
        self.morphemizerButton.setObjectName("morphemizerButton")
        self.horizontalLayout_10.addWidget(self.morphemizerButton)
        self.morphemizerPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.morphemizerPath.setInputMask("")
        self.morphemizerPath.setText("")
        self.morphemizerPath.setObjectName("morphemizerPath")
        self.horizontalLayout_10.addWidget(self.morphemizerPath)
        self.startMinimizedCheck = QtWidgets.QCheckBox(self.basicTab)
        self.startMinimizedCheck.setGeometry(QtCore.QRect(10, 270, 101, 17))
        self.startMinimizedCheck.setObjectName("startMinimizedCheck")
        self.label_6 = QtWidgets.QLabel(self.basicTab)
        self.label_6.setGeometry(QtCore.QRect(200, 302, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.basicTab, "")
        self.databaseTab = QtWidgets.QWidget()
        self.databaseTab.setObjectName("databaseTab")
        self.db_list = QtWidgets.QListView(self.databaseTab)
        self.db_list.setGeometry(QtCore.QRect(230, 20, 221, 121))
        self.db_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.db_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.db_list.setMidLineWidth(0)
        self.db_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.db_list.setDragEnabled(True)
        self.db_list.setMovement(QtWidgets.QListView.Static)
        self.db_list.setWordWrap(False)
        self.db_list.setSelectionRectVisible(True)
        self.db_list.setObjectName("db_list")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.databaseTab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(250, 150, 181, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.up_db = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.up_db.setObjectName("up_db")
        self.horizontalLayout_3.addWidget(self.up_db)
        self.down_db = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.down_db.setObjectName("down_db")
        self.horizontalLayout_3.addWidget(self.down_db)
        self.add_db = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.add_db.setObjectName("add_db")
        self.horizontalLayout_3.addWidget(self.add_db)
        self.del_db = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.del_db.setObjectName("del_db")
        self.horizontalLayout_3.addWidget(self.del_db)
        self.label_2 = QtWidgets.QLabel(self.databaseTab)
        self.label_2.setGeometry(QtCore.QRect(240, 0, 211, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.databaseTab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 70, 172, 22))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.dbFolderButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_4)
        self.dbFolderButton.setObjectName("dbFolderButton")
        self.horizontalLayout_4.addWidget(self.dbFolderButton)
        self.dbFolderPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.dbFolderPath.setText("")
        self.dbFolderPath.setObjectName("dbFolderPath")
        self.horizontalLayout_4.addWidget(self.dbFolderPath)
        self.label_4 = QtWidgets.QLabel(self.databaseTab)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.databaseTab)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 140, 160, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.frequencyButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_9)
        self.frequencyButton.setObjectName("frequencyButton")
        self.horizontalLayout_9.addWidget(self.frequencyButton)
        self.frequencyPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.frequencyPath.setText("")
        self.frequencyPath.setObjectName("frequencyPath")
        self.horizontalLayout_9.addWidget(self.frequencyPath)
        self.label_10 = QtWidgets.QLabel(self.databaseTab)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.databaseTab, "")
        self.ImportTab = QtWidgets.QWidget()
        self.ImportTab.setObjectName("ImportTab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.ImportTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 100, 391, 43))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wk_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.wk_check.setChecked(True)
        self.wk_check.setObjectName("wk_check")
        self.horizontalLayout.addWidget(self.wk_check)
        self.wk_api_token = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.wk_api_token.setInputMask("")
        self.wk_api_token.setReadOnly(False)
        self.wk_api_token.setClearButtonEnabled(False)
        self.wk_api_token.setObjectName("wk_api_token")
        self.horizontalLayout.addWidget(self.wk_api_token)
        self.wk_conn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.wk_conn.setObjectName("wk_conn")
        self.horizontalLayout.addWidget(self.wk_conn)
        self.gridLayoutWidget = QtWidgets.QWidget(self.ImportTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 170, 321, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.duo_username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.duo_username.setInputMask("")
        self.duo_username.setReadOnly(False)
        self.duo_username.setClearButtonEnabled(False)
        self.duo_username.setObjectName("duo_username")
        self.gridLayout.addWidget(self.duo_username, 0, 1, 1, 1)
        self.duo_check = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.duo_check.setChecked(True)
        self.duo_check.setObjectName("duo_check")
        self.gridLayout.addWidget(self.duo_check, 0, 0, 2, 1)
        self.duo_pass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.duo_pass.setInputMask("")
        self.duo_pass.setReadOnly(False)
        self.duo_pass.setClearButtonEnabled(False)
        self.duo_pass.setObjectName("duo_pass")
        self.gridLayout.addWidget(self.duo_pass, 1, 1, 1, 1)
        self.duo_conn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.duo_conn.setObjectName("duo_conn")
        self.gridLayout.addWidget(self.duo_conn, 0, 2, 2, 1)
        self.tabWidget.addTab(self.ImportTab, "")
        self.ankiTab = QtWidgets.QWidget()
        self.ankiTab.setObjectName("ankiTab")
        self.label_5 = QtWidgets.QLabel(self.ankiTab)
        self.label_5.setGeometry(QtCore.QRect(310, 20, 91, 16))
        self.label_5.setObjectName("label_5")
        self.connectToAnki = QtWidgets.QPushButton(self.ankiTab)
        self.connectToAnki.setGeometry(QtCore.QRect(20, 20, 111, 23))
        self.connectToAnki.setObjectName("connectToAnki")
        self.ankiNoteTable = QtWidgets.QTableWidget(self.ankiTab)
        self.ankiNoteTable.setGeometry(QtCore.QRect(20, 100, 256, 192))
        self.ankiNoteTable.setRowCount(0)
        self.ankiNoteTable.setColumnCount(2)
        self.ankiNoteTable.setObjectName("ankiNoteTable")
        item = QtWidgets.QTableWidgetItem()
        self.ankiNoteTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ankiNoteTable.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.ankiTab, "")
        self.applyCancelButton = QtWidgets.QDialogButtonBox(Dialog)
        self.applyCancelButton.setGeometry(QtCore.QRect(290, 450, 156, 23))
        self.applyCancelButton.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.applyCancelButton.setCenterButtons(False)
        self.applyCancelButton.setObjectName("applyCancelButton")
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(10, 450, 151, 31))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.languageCombo = QtWidgets.QComboBox(self.horizontalLayoutWidget_11)
        self.languageCombo.setObjectName("languageCombo")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.horizontalLayout_11.addWidget(self.languageCombo)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setToolTip(_translate("Dialog", "use this option to not pick up proper nouns (names) as new vocab"))
        self.label.setText(_translate("Dialog", "Analyze shortcut"))
        self.properNounsCheck.setStatusTip(_translate("Dialog", "Proper nouns are counted as already readable"))
        self.properNounsCheck.setText(_translate("Dialog", "Treat proper nouns known"))
        self.ignoreGrammarCheck.setToolTip(_translate("Dialog", "Use this option to ignore morpheme grammar type (noun, verb, etc.)"))
        self.ignoreGrammarCheck.setText(_translate("Dialog", "Ignore grammar position"))
        self.label_11.setText(_translate("Dialog", "Morphemizer Location"))
        self.morphemizerButton.setText(_translate("Dialog", "..."))
        self.morphemizerPath.setPlaceholderText(_translate("Dialog", "Morphemeizer Path"))
        self.startMinimizedCheck.setToolTip(_translate("Dialog", "start the program minimized"))
        self.startMinimizedCheck.setText(_translate("Dialog", "Start minimized"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Set default button</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basicTab), _translate("Dialog", "Basic"))
        self.up_db.setText(_translate("Dialog", "up"))
        self.down_db.setText(_translate("Dialog", "down"))
        self.add_db.setText(_translate("Dialog", "add"))
        self.del_db.setText(_translate("Dialog", "delete"))
        self.label_2.setText(_translate("Dialog", "Databases to union into external"))
        self.dbFolderButton.setText(_translate("Dialog", "..."))
        self.dbFolderPath.setPlaceholderText(_translate("Dialog", "Database path"))
        self.label_4.setText(_translate("Dialog", "Database folder"))
        self.frequencyButton.setText(_translate("Dialog", "..."))
        self.frequencyPath.setPlaceholderText(_translate("Dialog", "Master frequency path"))
        self.label_10.setText(_translate("Dialog", "Default frequency list"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.databaseTab), _translate("Dialog", "Databases"))
        self.wk_check.setText(_translate("Dialog", "Use Wanikani"))
        self.wk_api_token.setPlaceholderText(_translate("Dialog", "Wanikani API token"))
        self.wk_conn.setText(_translate("Dialog", "Check Conn"))
        self.duo_username.setPlaceholderText(_translate("Dialog", "Duolingo username"))
        self.duo_check.setText(_translate("Dialog", "Use Duolingo"))
        self.duo_pass.setPlaceholderText(_translate("Dialog", "Duolingo passowrd"))
        self.duo_conn.setText(_translate("Dialog", "Check Conn"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ImportTab), _translate("Dialog", "Import"))
        self.label_5.setText(_translate("Dialog", "Choose note type"))
        self.connectToAnki.setText(_translate("Dialog", "Connect to anki"))
        item = self.ankiNoteTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Note Field"))
        item = self.ankiNoteTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Inserted Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ankiTab), _translate("Dialog", "Anki"))
        self.label_12.setText(_translate("Dialog", "Language"))
        self.languageCombo.setItemText(0, _translate("Dialog", "Japanese"))
        self.languageCombo.setItemText(1, _translate("Dialog", "Chinese"))
        self.languageCombo.setItemText(2, _translate("Dialog", "German"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
