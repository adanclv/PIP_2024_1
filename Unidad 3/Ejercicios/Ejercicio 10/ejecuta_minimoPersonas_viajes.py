
from PyQt5 import uic, QtWidgets
import minimoPersonas_viajes

class MyDialog(QtWidgets.QDialog, minimoPersonas_viajes.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        minimoPersonas_viajes.Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.textEdit.setReadOnly(True)