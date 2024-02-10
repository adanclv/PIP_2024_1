import math
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_08_Nota.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        calif = int(self.txt_calif.text())
        if calif == 10:
            nota = 'A'
        elif calif == 9:
            nota = 'B'
        elif calif == 8:
            nota = 'C'
        elif calif == 7:
            nota = 'D'
        elif calif == 6:
            nota = 'E'
        elif 0 <= calif < 6:
            nota = 'F'
        else:
            nota = 'No aplica'

        self.label_nota.setText(str(nota))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



