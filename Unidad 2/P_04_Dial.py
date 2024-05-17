import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P_04_Dial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_mascotas = {
            1: ['Poncho', 'Comer', 20, 'a+', ':/logo/Imagenes/poncho.jpg'],
            2: ['Adan', 'Comer', 20, 'a+', ':/logo/Imagenes/adan.jpg'],
            3: ['Cristobal', 'Comer', 20, 'a+', ':/logo/Imagenes/cristobal.jpg'],
            4: ['Pavel', 'Comer', 20, 'a+', ':/logo/Imagenes/pavel.jpg'],
        }

        self.dial_persona.setMinimum(1)
        self.dial_persona.setMaximum(4)
        self.dial_persona.setSingleStep(1)
        self.dial_persona.setValue(1)
        self.dial_persona.valueChanged.connect(self.cambio)
        self.img_persona.setPixmap(QtGui.QPixmap(':/logo/Imagenes/poncho.jpg'))

    # Área de los Slots
    def cambio(self):
        dataClave = self.dial_persona.value()
        imagen = self.datos_mascotas[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


