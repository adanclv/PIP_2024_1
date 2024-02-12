import math
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_05_PuntoMedio.ui"  # Nombre del archivo aquí.
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
        x1 = float(self.txt_x1.text())
        x2 = float(self.txt_x2.text())
        y1 = float(self.txt_y1.text())
        y2 = float(self.txt_y2.text())
        x_medio = (x1 + x2) / 2
        y_medio = (y1 + y2) / 2
        self.txt_resultado.setText(f'{x_medio, y_medio}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



