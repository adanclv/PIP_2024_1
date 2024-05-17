import Main_Enviando
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import Ej2_EjecucionDialog as ej2


class MyApp(QtWidgets.QMainWindow, Main_Enviando.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Main_Enviando.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        self.dialogo = ej2.MyDialog(self)
        self.dialogo.setModal(True)
        self.dialogo.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

