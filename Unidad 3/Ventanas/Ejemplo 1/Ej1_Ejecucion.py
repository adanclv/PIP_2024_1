import Main_Enviando
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import Ej1_EjecucionDialog


class MyApp(QtWidgets.QMainWindow, Main_Enviando.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Main_Enviando.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        r = a + b

        self.dialogo = Ej1_EjecucionDialog.MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.lbl_resultado.setText(str(r))
        self.dialogo.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

