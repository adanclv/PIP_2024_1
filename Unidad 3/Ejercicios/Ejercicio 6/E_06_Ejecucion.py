import sys
import E_06_Transporte
import E_06_EjecucionDialog as e06
from PyQt5 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow, E_06_Transporte.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        E_06_Transporte.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_generar.clicked.connect(self.generar)

        self.diasFabian = list()
        self.diasHector = list()
        self.diasEmi = list()

    # Área de los Slots
    def generar(self):
        self.diasFabian.append(int(self.txt_f1.text()))
        self.diasFabian.append(int(self.txt_f2.text()))
        self.diasFabian.append(int(self.txt_f3.text()))
        self.diasFabian.append(int(self.txt_f4.text()))
        self.diasFabian.append(int(self.txt_f5.text()))

        self.diasHector.append(int(self.txt_h1.text()))
        self.diasHector.append(int(self.txt_h2.text()))
        self.diasHector.append(int(self.txt_h3.text()))
        self.diasHector.append(int(self.txt_h4.text()))
        self.diasHector.append(int(self.txt_h5.text()))

        self.diasEmi.append(int(self.txt_e1.text()))
        self.diasEmi.append(int(self.txt_e2.text()))
        self.diasEmi.append(int(self.txt_e3.text()))
        self.diasEmi.append(int(self.txt_e4.text()))
        self.diasEmi.append(int(self.txt_e5.text()))

        self.cargarDialog()

    def cargarDialog(self):
        self.dialogo = e06.MyDialog()
        self.dialogo.setModal(True)

        self.dialogo.lbl_Fabian1.setText(f'{self.diasFabian[0]}')
        self.dialogo.lbl_Fabian2.setText(f'{self.diasFabian[1]}')
        self.dialogo.lbl_Fabian3.setText(f'{self.diasFabian[2]}')
        self.dialogo.lbl_Fabian4.setText(f'{self.diasFabian[3]}')
        self.dialogo.lbl_Fabian5.setText(f'{self.diasFabian[4]}')
        self.dialogo.lbl_Fabian6.setText(f'{sum(self.diasFabian)}')

        self.dialogo.lbl_Hector1.setText(f'{self.diasHector[0]}')
        self.dialogo.lbl_Hector2.setText(f'{self.diasHector[1]}')
        self.dialogo.lbl_Hector3.setText(f'{self.diasHector[2]}')
        self.dialogo.lbl_Hector4.setText(f'{self.diasHector[3]}')
        self.dialogo.lbl_Hector5.setText(f'{self.diasHector[4]}')
        self.dialogo.lbl_Hector6.setText(f'{sum(self.diasHector)}')

        self.dialogo.lbl_Emi1.setText(f'{self.diasEmi[0]}')
        self.dialogo.lbl_Emi2.setText(f'{self.diasEmi[1]}')
        self.dialogo.lbl_Emi3.setText(f'{self.diasEmi[2]}')
        self.dialogo.lbl_Emi4.setText(f'{self.diasEmi[3]}')
        self.dialogo.lbl_Emi5.setText(f'{self.diasEmi[4]}')
        self.dialogo.lbl_Emi6.setText(f'{sum(self.diasEmi)}')

        self.dialogo.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


