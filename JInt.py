from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app= QApplication(sys.argv)
    win = QMainWindow()
    xpos,ypos,width,height= [200,200,300,300]
    win.setGeometry(xpos,ypos,width,height)
    win.setWindowTitle("hello world")

    label= QtWidgets.QLabel(win)
    label.setText("my first label")
    

    win.show()
    sys.exit(app.exec_())

window()