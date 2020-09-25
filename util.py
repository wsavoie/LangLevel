
from preferences import p
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import platform

import hashlib, binascii

class CopySelectedCellsAction(QtWidgets.QAction):
    def __init__(self, table_widget):
        if not isinstance(table_widget, QtWidgets.QTableWidget):
            raise ValueError(str('CopySelectedCellsAction must be initialised with a QTableWidget. A %s was given.' % type(table_widget)))
        super(CopySelectedCellsAction, self).__init__("Copy", table_widget)
        self.setShortcut('Ctrl+C')
        self.triggered.connect(self.copy_cells_to_clipboard)
        self.table_widget = table_widget

    def copy_cells_to_clipboard(self):
        if len(self.table_widget.selectionModel().selectedIndexes()) > 0:
            # sort select indexes into rows and columns
            RC=self.table_widget.selectedRanges()[0].rowCount()
            CC=self.table_widget.selectedRanges()[0].columnCount()
            items=self.table_widget.selectedItems()
            
            #if selection leads to a ragged array, only copy first value
            if(len(items) is not RC*CC): 
                sys_clip = QtWidgets.QApplication.clipboard()
                sys_clip.setText(items[0].text())
            
            outList=[[items[i].text() for i in range(j*CC,(j+1)*CC)] for j in range(RC)]
            outCommand= '\n'.join([x for x in map('\t'.join,outList)])
            sys_clip = QtWidgets.QApplication.clipboard()
            sys_clip.setText(outCommand)


def errorMsg(text):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("error")

    msg.setText(text)
    msg.exec_()

def isWin():
    if platform.system()=='Windows':
        return True
    return False

def isMac():
    if platform.system()=='Darwin':
        return True
    return False

def isLinux():
    if platform.system()=='Linux ':
        return True
    return False

def getPathLE(lineEdit, caption, open_directory=False,startPath='',filter_=''):  # LineEdit -> GUI ()
    '''get database files from explorer add them to lineEdit'''
    try:
        if open_directory:
            path =  QtWidgets.QFileDialog.getExistingDirectory(caption=caption, directory=startPath,
                        options=QtWidgets.QFileDialog.ShowDirsOnly)
        else:
            path = QtWidgets.QFileDialog.getOpenFileName(caption=caption, directory=startPath, filter=filter_)[0]
    except Exception as e:
        errorMsg(e)
        return

    if path:
        lineEdit.setText(path)

def getPathLW(listWid,caption, open_directory=False,startPath='',filter_=''):  # LineEdit -> GUI ()
    '''get database files from explorer for use when adding to line widget'''
    try:
        paths = QtWidgets.QFileDialog.getOpenFileNames(caption=caption, directory=startPath, filter=filter_)[0]
        # print(paths)
    except Exception as e:
        print(e)
        return
    
    return paths

def setCheck(obj,prefName):
    obj.setChecked(p['DEFAULT'].getboolean(prefName))
    obj.clicked['bool'].connect(lambda: on_check(prefName))
    
def on_check(prop):
    p['DEFAULT'][prop]= str(not p['DEFAULT'].getboolean(prop))

def retrive_pass(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    # pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return binascii.hexlify(pwdhash).decode('ascii')

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')