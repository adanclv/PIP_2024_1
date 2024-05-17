import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P_05_VerticalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_mascotas = {
            1: ['Poncho', ':/logo/Imagenes/poncho.jpg'],
            2: ['Adan', ':/logo/Imagenes/adan.jpg'],
            3: ['Cristobal', ':/logo/Imagenes/cristobal.jpg'],
            4: ['Pavel', ':/logo/Imagenes/pavel.jpg'],
        }

        self.vs_persona.setMinimum(1)
        self.vs_persona.setMaximum(4)
        self.vs_persona.setSingleStep(1)
        self.vs_persona.setValue(1)
        self.vs_persona.valueChanged.connect(self.cambio)


    # Área de los Slots
    def cambio(self):
        dataClave = self.vs_persona.value()
        imagen = self.datos_mascotas[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


