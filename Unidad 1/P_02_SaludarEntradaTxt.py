import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_02_SaludarEntradaTxt.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Saludar.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        nombre = self.txt_Nombre.text()
        edad = int(self.txt_Edad.text())
        cadena = "Hola " + nombre + " de " + str(edad) + " años"

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


