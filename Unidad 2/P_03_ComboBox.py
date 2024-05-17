import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P_03_ComboBox.ui"  # Nombre del archivo aquí.
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
        self.combo_persona.addItem('Selecciona...', 0)
        self.combo_persona.addItem('Poncho', 1)
        self.combo_persona.addItem('Adan', 2)
        self.combo_persona.addItem('Cristobal', 3)
        self.combo_persona.addItem('Pavel', 4)

        self.combo_persona.currentIndexChanged.connect(self.cambio)
    # Área de los Slots
    def cambio(self):
        print('Text:', self.combo_persona.currentText())
        print('Index:', self.combo_persona.currentIndex())
        print('Data:', self.combo_persona.currentData())

        dataClave = self.combo_persona.currentData()
        imagen = self.datos_mascotas[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


