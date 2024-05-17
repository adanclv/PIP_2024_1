import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_02_SeleccionEquipoui.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cb_1.toggled.connect(self.seleccionar_poncho)
        self.cb_2.toggled.connect(self.seleccionar_adan)
        self.cb_3.toggled.connect(self.seleccionar_cristobal)
        self.cb_4.toggled.connect(self.seleccionar_pavel)

        self.poncho = ''
        self.adan = ''
        self.cristobal = ''
        self.pavel = ''

    # Área de los Slots
    def seleccionar_poncho(self):
        if self.cb_1.isChecked():
            self.poncho = 'ALFONSO\n'
        else:
            self.poncho = ''
        self.txt_equipo.setPlainText(self.poncho + self.adan + self.cristobal + self.pavel)

    def seleccionar_adan(self):
        if self.cb_2.isChecked():
            self.adan = 'ADAN\n'
        else:
            self.adan = ''
        self.txt_equipo.setPlainText(self.poncho + self.adan + self.cristobal + self.pavel)

    def seleccionar_cristobal(self):
        if self.cb_3.isChecked():
            self.cristobal = 'CRISTOBAL\n'
        else:
            self.cristobal = ''
        self.txt_equipo.setPlainText(self.poncho + self.adan + self.cristobal + self.pavel)

    def seleccionar_pavel(self):
        if self.cb_4.isChecked():
            self.pavel = 'PAVEL\n'
        else:
            self.pavel = ''
        self.txt_equipo.setPlainText(self.poncho + self.adan + self.cristobal + self.pavel)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


