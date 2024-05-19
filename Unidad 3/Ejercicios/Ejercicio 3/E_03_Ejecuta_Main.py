import sys
import E_03_MainWindow
import E_03_Ejecuta_Dialog
from PyQt5 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow, E_03_MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        E_03_MainWindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_ok.clicked.connect(self.ok)

    # Área de los Slots
    def ok(self):
        self.dialogo = E_03_Ejecuta_Dialog.MyDialog()
        self.dialogo.setModal(True)

        # Calcular los pagos mensuales y el total
        pagoMensual = 10
        pagoTotal = 0
        for i in range(1, 13):
            nombreLineEdit = f"txt_montomes{i}"
            line_edit = getattr(self.dialogo, nombreLineEdit)
            line_edit.setText(str(pagoMensual))
            pagoTotal += pagoMensual
            pagoMensual *= 2

        self.dialogo.txt_montototal.setText(str(pagoTotal))

        self.dialogo.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())