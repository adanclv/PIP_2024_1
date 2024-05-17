import sys
import Second_Enviando
from PyQt5 import uic, QtWidgets, QtGui, QtCore

class MyDialog(QtWidgets.QDialog, Second_Enviando.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Second_Enviando.Ui_Dialog.__init__(self)
        self.setupUi(self)