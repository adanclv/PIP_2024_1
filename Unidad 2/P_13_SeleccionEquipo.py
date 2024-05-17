import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_13_SeleccionEquipoui.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_1.toggled.connect(self.seleccionar_poncho)
        self.rb_2.toggled.connect(self.seleccionar_adan)
        self.rb_3.toggled.connect(self.seleccionar_cristobal)
        self.rb_4.toggled.connect(self.seleccionar_pavel)

    # Área de los Slots
    def seleccionar_poncho(self):
        estado = self.rb_1.isChecked()
        print('El rb_1 cambio de estado. Nuevo estado:', estado)
        self.txt_seleccionado.setText("Poncho")

    def seleccionar_adan(self):
        self.txt_seleccionado.setText("Adan")

    def seleccionar_cristobal(self):
        self.txt_seleccionado.setText("Cristobal")

    def seleccionar_pavel(self):
        self.txt_seleccionado.setText("Pavel")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


