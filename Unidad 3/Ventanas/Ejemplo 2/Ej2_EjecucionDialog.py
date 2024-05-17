import Second_Enviando
from PyQt5 import uic, QtWidgets, QtGui, QtCore


class MyDialog(QtWidgets.QDialog, Second_Enviando.Ui_Dialog):
    def __init__(self, rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Second_Enviando.Ui_Dialog.__init__(self)
        self.setupUi(self)

        self.access = rPrincipal
        self.btn_sumar.clicked.connect(self.sumar)

    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        r = a + b

        print(r)
        self.access.lbl_resultado.setText(str(r))
        self.close()