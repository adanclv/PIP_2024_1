import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_Aritmetica.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.restar)
        self.btn_multiplicacion.clicked.connect(self.multiplicar)
        self.btn_division.clicked.connect(self.dividir)
        self.txt_resultado.setEnabled(False)

    # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        suma = a + b
        self.txt_resultado.setText(str(suma))

    def restar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        resta = a - b
        self.txt_resultado.setText(str(resta))

    def multiplicar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        multiplicacion= a * b
        self.txt_resultado.setText(str(multiplicacion))

    def dividir(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        division = a / b
        self.txt_resultado.setText(str(division))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


