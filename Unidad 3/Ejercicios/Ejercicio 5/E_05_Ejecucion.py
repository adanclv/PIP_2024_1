import sys
import E_05_Stock
import E_05_EjecucionDialog as e05
import random as rand
from PyQt5 import QtWidgets


class MyApp(QtWidgets.QMainWindow, E_05_Stock.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        E_05_Stock.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_buy1.clicked.connect(self.comprar)
        self.btn_buy2.clicked.connect(self.comprar)
        self.btn_buy3.clicked.connect(self.comprar)
        self.btn_buy4.clicked.connect(self.comprar)
        self.btn_buy5.clicked.connect(self.comprar)
        self.btn_buy6.clicked.connect(self.comprar)
        self.btn_buy7.clicked.connect(self.comprar)
        self.btn_buy8.clicked.connect(self.comprar)
        self.btn_buy9.clicked.connect(self.comprar)
        self.btn_buy10.clicked.connect(self.comprar)

        self.lbl_stock1.setText(str(rand.randint(10, 30)))
        self.lbl_stock2.setText(str(rand.randint(10, 30)))
        self.lbl_stock3.setText(str(rand.randint(10, 30)))
        self.lbl_stock4.setText(str(rand.randint(10, 30)))
        self.lbl_stock5.setText(str(rand.randint(10, 30)))
        self.lbl_stock6.setText(str(rand.randint(10, 30)))
        self.lbl_stock7.setText(str(rand.randint(10, 30)))
        self.lbl_stock8.setText(str(rand.randint(10, 30)))
        self.lbl_stock9.setText(str(rand.randint(10, 30)))
        self.lbl_stock10.setText(str(rand.randint(10, 30)))

        self.a = [int(self.lbl_stock1.text()), int(self.lbl_stock2.text()),
                  int(self.lbl_stock3.text()), int(self.lbl_stock4.text()),
                  int(self.lbl_stock5.text()), int(self.lbl_stock6.text()),
                  int(self.lbl_stock7.text()), int(self.lbl_stock8.text()),
                  int(self.lbl_stock9.text()), int(self.lbl_stock10.text())]
        self.b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.index = -1

    # Área de los Slots
    def comprar(self):
        boton = self.sender().objectName()
        if boton == 'btn_buy1':
            aux = self.label_7.text()
            self.index = 0
        elif boton == 'btn_buy2':
            aux = self.label_11.text()
            self.index = 1
        elif boton == 'btn_buy3':
            aux = self.label_12.text()
            self.index = 2
        elif boton == 'btn_buy4':
            aux = self.label_16.text()
            self.index = 3
        elif boton == 'btn_buy5':
            aux = self.label_17.text()
            self.index = 4
        elif boton == 'btn_buy6':
            aux = self.label_18.text()
            self.index = 5
        elif boton == 'btn_buy7':
            aux = self.label_19.text()
            self.index = 6
        elif boton == 'btn_buy8':
            aux = self.label_20.text()
            self.index = 7
        elif boton == 'btn_buy9':
            aux = self.label_22.text()
            self.index = 8
        else:
            aux = self.label_21.text()
            self.index = 9

        self.dialogo = e05.MyDialog(self)
        self.dialogo.setModal(True)
        self.dialogo.lbl_producto.setText(aux)
        self.dialogo.show()

    def update(self):
        self.lbl_stock1.setText(str(self.a[0]))
        self.lbl_sold1.setText(str(self.b[0]))
        self.lbl_restock1.setText(str(self.c[0]))

        self.lbl_stock2.setText(str(self.a[1]))
        self.lbl_sold2.setText(str(self.b[1]))
        self.lbl_restock2.setText(str(self.c[1]))

        self.lbl_stock3.setText(str(self.a[2]))
        self.lbl_sold3.setText(str(self.b[2]))
        self.lbl_restock3.setText(str(self.c[2]))

        self.lbl_stock4.setText(str(self.a[3]))
        self.lbl_sold4.setText(str(self.b[3]))
        self.lbl_restock4.setText(str(self.c[3]))

        self.lbl_stock5.setText(str(self.a[4]))
        self.lbl_sold5.setText(str(self.b[4]))
        self.lbl_restock5.setText(str(self.c[4]))

        self.lbl_stock6.setText(str(self.a[5]))
        self.lbl_sold6.setText(str(self.b[5]))
        self.lbl_restock6.setText(str(self.c[5]))

        self.lbl_stock7.setText(str(self.a[6]))
        self.lbl_sold7.setText(str(self.b[6]))
        self.lbl_restock7.setText(str(self.c[6]))

        self.lbl_stock8.setText(str(self.a[7]))
        self.lbl_sold8.setText(str(self.b[7]))
        self.lbl_restock8.setText(str(self.c[7]))

        self.lbl_stock9.setText(str(self.a[8]))
        self.lbl_sold9.setText(str(self.b[8]))
        self.lbl_restock9.setText(str(self.c[8]))

        self.lbl_stock10.setText(str(self.a[9]))
        self.lbl_sold10.setText(str(self.b[9]))
        self.lbl_restock10.setText(str(self.c[9]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


