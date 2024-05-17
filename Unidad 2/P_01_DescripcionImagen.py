import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P_01_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_equipo ={
            1:['Alfonso Aldama', 'Comer', 20, 'O+', ':/logo/Imagenes/poncho.jpg'],
            2: ['Adan Clemente', 'Comer', 20, 'O+', ':/logo/Imagenes/adan.jpg'],
            3: ['Jesus Cristobal', 'Comer', 20, 'O+', ':/logo/Imagenes/cristobal.jpg'],
            4: ['Pavel Dominguez', 'Comer', 20, 'O+', ':/logo/Imagenes/pavel.jpg'],
        }

        self.btn_atras.clicked.connect(self.atras)
        self.btn_siguiente.clicked.connect(self.siguiente)
        self.img_persona.setPixmap(QtGui.QPixmap(':/logo/Imagenes/poncho.jpg'))
        self.txt_nombre.setText('Alfonso Aldama')
        self.txt_pasatiempo.setText('Comer')
        self.txt_edad.setText('20')
        self.txt_sangre.setText('O+')

        self.index_control = 1
        self.btn_atras.setEnabled(False)

    # Área de los Slots
    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            self.btn_siguiente.setEnabled(True)
            datos = self.datos_equipo[self.index_control]
            # changes
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
            self.txt_nombre.setText(datos[0])
            self.txt_pasatiempo.setText(datos[1])
            self.txt_edad.setText(str(datos[2]))
            self.txt_sangre.setText(datos[3])
        if self.index_control == 1:
            self.btn_atras.setEnabled(False)


    def siguiente(self):
        if self.index_control < 4:
            self.index_control += 1
            self.btn_atras.setEnabled(True)
            datos = self.datos_equipo[self.index_control]
            # changes
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
            self.txt_nombre.setText(datos[0])
            self.txt_pasatiempo.setText(datos[1])
            self.txt_edad.setText(str(datos[2]))
            self.txt_sangre.setText(datos[3])
        if self.index_control == 4:
            self.btn_siguiente.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


