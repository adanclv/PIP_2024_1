
from PyQt5 import uic, QtWidgets
import costo_viajes

class MyDialog(QtWidgets.QDialog, costo_viajes.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        costo_viajes.Ui_Dialog.__init__(self)
        self.setupUi(self)