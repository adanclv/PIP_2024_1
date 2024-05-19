
from PyQt5 import uic, QtWidgets
import E_07_Langosta_dialog

class MyDialog(QtWidgets.QDialog, E_07_Langosta_dialog.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        E_07_Langosta_dialog.Ui_Dialog.__init__(self)
        self.setupUi(self)