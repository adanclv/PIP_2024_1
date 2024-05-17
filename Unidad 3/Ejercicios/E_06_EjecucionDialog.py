import E_06_TransporteDialog
from PyQt5 import QtWidgets


class MyDialog(QtWidgets.QDialog, E_06_TransporteDialog.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        E_06_TransporteDialog.Ui_Dialog.__init__(self)
        self.setupUi(self)