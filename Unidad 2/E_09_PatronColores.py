import math
import sys
import random as rand
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "E_09_PatronColores.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rojo.clicked.connect(self.match)
        self.amarillo.clicked.connect(self.match)
        self.verde.clicked.connect(self.match)
        self.azul.clicked.connect(self.match)
        self.btn_comenzar.clicked.connect(self.inicio)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.carrusel)

        self.color = 0
        self.cont = 0
        self.rondas = 0
        self.colores = ['rojo', 'amarillo', 'verde', 'azul']
        self.pc = list()
        self.noEnables()

    # Área de los Slots
    def inicio(self):
        self.lbl_lost.setText('')
        self.color = 0
        self.btn_comenzar.setEnabled(False)
        self.pc = [self.colores[rand.randint(0, 3)]]
        self.rondas = len(self.pc)
        self.segundoPlano.start(1000)

    def carrusel(self):
        self.noEnables()
        self.lbl_lost.setText('')
        if self.cont == self.rondas:
            self.cont = 0
            self.segundoPlano.stop()
            self.enables()
            return

        self.habilitarColor()
        self.cont += 1
        self.lbl_lost.setText(str(self.cont))

    def habilitarColor(self):
        if self.pc[self.cont] == 'rojo':
            self.rojo.setEnabled(True)
        elif self.pc[self.cont] == 'amarillo':
            self.amarillo.setEnabled(True)
        elif self.pc[self.cont] == 'verde':
            self.verde.setEnabled(True)
        else:
            self.azul.setEnabled(True)

    def match(self):
        nombre = self.sender().objectName()
        if nombre == self.pc[self.color]: # si acertaste
            self.color += 1
            self.lbl_lost.setText(str(self.color))
        else:
            self.lbl_lost.setText('Perdiste')
            self.noEnables()
            self.btn_comenzar.setEnabled(True)
            self.pc.clear()
            return

        if self.color == len(self.pc): # si acertaste todos
            self.color = 0
            self.noEnables()
            self.pc.append(self.colores[rand.randint(0, 3)])
            self.rondas = len(self.pc)
            self.segundoPlano.start(500)

    def noEnables(self):
        self.rojo.setEnabled(False)
        self.amarillo.setEnabled(False)
        self.verde.setEnabled(False)
        self.azul.setEnabled(False)

    def enables(self):
        self.rojo.setEnabled(True)
        self.amarillo.setEnabled(True)
        self.verde.setEnabled(True)
        self.azul.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



