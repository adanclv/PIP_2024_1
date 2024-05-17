import sys
import P_02_LeerArchivos as p02
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_ListaAlumnos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        a = p02.cargarArchivo()
        for e in a:
            self.listWidget.addItem(e[0])

    # Área de los Slots


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


