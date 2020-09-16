from manabi import mw
from .preferences import *

def mkBtn(txt, f, parent):
    b = QPushButton(txt)
    b.clicked.connect(f)
    parent.addWidget(b)
    return b
