import E_04_TrabajoXHoraDialog
from PyQt5 import QtWidgets


class MyDialog(QtWidgets.QDialog, E_04_TrabajoXHoraDialog.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        E_04_TrabajoXHoraDialog.Ui_Dialog.__init__(self)
        self.setupUi(self)