import E_05_StockDialog
from PyQt5 import QtWidgets


class MyDialog(QtWidgets.QDialog, E_05_StockDialog.Ui_Dialog):
    def __init__(self, mainAccess):
        QtWidgets.QDialog.__init__(self)
        E_05_StockDialog.Ui_Dialog.__init__(self)
        self.setupUi(self)

        self.access = mainAccess
        self.btn_buy.clicked.connect(self.comprar)

    def comprar(self):
        i = self.access.index
        self.access.b[i] += int(self.txt_cantidad.text())
        if self.access.a[i] == self.access.b[i]:
            self.access.a[i] = 0
            self.access.c[i] = int(self.txt_cantidad.text())
        elif self.access.b[i] > self.access.a[i]:
            self.access.c[i] = self.access.a[i] + (self.access.b[i] - self.access.a[i]) * 2
            self.access.a[i] = 0
        elif self.access.a[i] > self.access.b[i]:
            self.access.a[i] = self.access.a[i] - self.access.b[i]
            self.access.c[i] += int(self.txt_cantidad.text())

        self.close()
        self.access.update()
