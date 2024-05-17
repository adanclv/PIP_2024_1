import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P_12_CompareImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_atras.clicked.connect(self.atras)
        self.btn_siguiente.clicked.connect(self.siguiente)
        self.btn_validar.clicked.connect(self.validar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.carrusel)
        self.imagenes = [':/logo/Imagenes/poncho.jpg',
                         ':/logo/Imagenes/adan.jpg',
                         ':/logo/Imagenes/cristobal.jpg',
                         ':/logo/Imagenes/pavel.jpg']

        self.btn_atras.setEnabled(False)
        self.index_control = 0
        self.cont = 0

    # Área de los Slots
    def iniciar(self):
        t = self.btn_iniciar.text()
        if t == 'Iniciar':
            self.btn_iniciar.setText('Detener')
            self.cont = 0
            self.segundoPlano.start(80)
        else:
            self.btn_iniciar.setText('Iniciar')
            self.segundoPlano.stop()
            print(self.cont)

    def carrusel(self):
        self.cont = (self.cont + 1) % len(self.imagenes)
        self.lbl_1.setPixmap(QtGui.QPixmap(self.imagenes[self.cont]))

    def atras(self):
        if self.index_control > 0:
            self.index_control -= 1
            self.btn_siguiente.setEnabled(True)
            self.lbl_2.setPixmap(QtGui.QPixmap(self.imagenes[self.index_control]))

        if self.index_control == 0:
            self.btn_atras.setEnabled(False)

    def siguiente(self):
        if self.index_control < len(self.imagenes) - 1:
            self.index_control += 1
            self.btn_atras.setEnabled(True)
            self.lbl_2.setPixmap(QtGui.QPixmap(self.imagenes[self.index_control]))

        if self.index_control == len(self.imagenes) - 1:
            self.btn_siguiente.setEnabled(False)

    def validar(self):
        res = self.index_control == self.cont
        msj = QtWidgets.QMessageBox()
        msj.setText(str(res))
        msj.exec_()
        print(self.cont, self.index_control)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


