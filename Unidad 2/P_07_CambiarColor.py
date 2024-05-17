import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_07_CambiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.hs_r.setMinimum(0)
        self.hs_r.setMaximum(255)
        self.hs_r.setSingleStep(1)
        self.hs_r.setValue(0)
        self.hs_r.valueChanged.connect(self.cambioR)

        self.hs_g.setMinimum(0)
        self.hs_g.setMaximum(255)
        self.hs_g.setSingleStep(1)
        self.hs_g.setValue(0)
        self.hs_g.valueChanged.connect(self.cambioG)

        self.hs_b.setMinimum(0)
        self.hs_b.setMaximum(255)
        self.hs_b.setSingleStep(1)
        self.hs_b.setValue(0)
        self.hs_b.valueChanged.connect(self.cambioB)

        self.R = '0'
        self.G = '0'
        self.B = '0'

    # Área de los Slots
    def cambioR(self):
        self.R = self.hs_r.value()
        estilo = f'background-color: rgb({str(self.R)}, {str(self.G)}, {str(self.B)});'
        self.colores.setStyleSheet(estilo)
        self.printColor()

    def cambioG(self):
        self.G = self.hs_g.value()
        estilo = f'background-color: rgb({str(self.R)}, {str(self.G)}, {str(self.B)});'
        self.colores.setStyleSheet(estilo)
        self.printColor()

    def cambioB(self):
        self.B = self.hs_b.value()
        estilo = f'background-color: rgb({str(self.R)}, {str(self.G)}, {str(self.B)});'
        self.colores.setStyleSheet(estilo)
        self.printColor()

    def printColor(self):
        self.txt_r.setText(str(self.R))
        self.txt_g.setText(str(self.G))
        self.txt_b.setText(str(self.B))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


