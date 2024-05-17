import sys
import os
import E_00_EjecutableGeneral
import E_04_Ejecucion, E_05_Ejecucion, E_06_Ejecucion
from PyQt5 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow, E_00_EjecutableGeneral.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        E_00_EjecutableGeneral.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_ej4.clicked.connect(self.ejercicio4)
        self.btn_ej5.clicked.connect(self.ejercicio5)
        self.btn_ej6.clicked.connect(self.ejercicio6)

    # Área de los Slots
    def ejercicio4(self):
        self.e4 = E_04_Ejecucion.MyApp()
        self.e4.show()

    def ejercicio5(self):
        self.e5 = E_05_Ejecucion.MyApp()
        self.e5.show()

    def ejercicio6(self):
        self.e6 = E_06_Ejecucion.MyApp()
        self.e6.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


