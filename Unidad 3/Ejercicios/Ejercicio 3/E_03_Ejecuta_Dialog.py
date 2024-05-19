import E_03_Dialog
from PyQt5 import QtWidgets


class MyDialog(QtWidgets.QDialog, E_03_Dialog.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        E_03_Dialog.Ui_Dialog.__init__(self)
        self.setupUi(self)