import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P_11_SliderWithTimers.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.carrusel)
        self.imagenes = [':/logo/Imagenes/poncho.jpg', ':/logo/Imagenes/adan.jpg',
                         ':/logo/Imagenes/cristobal.jpg', ':/logo/Imagenes/pavel.jpg']

    # Área de los Slots
    def iniciar(self):
        t = self.btn_iniciar.text()
        self.cont = 0
        if t == 'Iniciar':
            self.btn_iniciar.setText('Detener')
            self.segundoPlano.start(700)
        else:
            self.btn_iniciar.setText('Iniciar')
            self.segundoPlano.stop()

    def carrusel(self):
        self.lbl_1.setPixmap(QtGui.QPixmap(self.imagenes[self.cont]))
        self.cont = (self.cont + 1) % len(self.imagenes)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


