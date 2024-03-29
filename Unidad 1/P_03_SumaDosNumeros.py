import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_SumaDosNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.sumar)
        self.txt_suma.setEnabled(False)
    # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        suma = a + b
        self.txt_suma.setText(str(suma))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


