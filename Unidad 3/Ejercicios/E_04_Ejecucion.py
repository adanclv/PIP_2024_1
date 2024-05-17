import sys
import E_04_TrabajoXHora
import E_04_EjecucionDialog as e04
from PyQt5 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow, E_04_TrabajoXHora.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        E_04_TrabajoXHora.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        salario = float(self.txt_salario.text())
        empleado1 = int(self.txt_1.text()) * salario
        empleado2 = int(self.txt_2.text()) * salario
        empleado3 = int(self.txt_3.text()) * salario
        empleado4 = int(self.txt_4.text()) * salario
        empleado5 = int(self.txt_5.text()) * salario
        total = empleado1 + empleado2 + empleado3 + empleado4 + empleado5

        self.dialogo = e04.MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.txt_1.setText(f'${str(empleado1)}')
        self.dialogo.txt_2.setText(f'${str(empleado2)}')
        self.dialogo.txt_3.setText(f'${str(empleado3)}')
        self.dialogo.txt_4.setText(f'${str(empleado4)}')
        self.dialogo.txt_5.setText(f'${str(empleado5)}')
        self.dialogo.txt_total.setText(f'${str(total)}')
        self.dialogo.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


