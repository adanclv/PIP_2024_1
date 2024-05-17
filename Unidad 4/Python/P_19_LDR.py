import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial

qtCreatorFile = "P_19_LDR.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Accion.clicked.connect(self.conectar)
        self.arduino = None

        self.segundo = QtCore.QTimer()
        self.segundo.timeout.connect(self.lecturaArduino)

    # Área de los Slots
    def conectar(self):
        txt_btn = self.btn_Accion.text()
        com = self.txt_COM.text()
        if txt_btn == "Conectar" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundo.start(100)
            self.lbl_estado.setText("Conectado")
            self.btn_Accion.setText("Desconectar")
        elif txt_btn == "Desconectar" and self.arduino.isOpen():
            self.arduino.close()
            self.segundo.stop()
            self.lbl_estado.setText("Desconectado")
            self.btn_Accion.setText("Reconectear")
        else:
            self.arduino.open()
            self.segundo.start(100)
            self.lbl_estado.setText("Conectado")
            self.btn_Accion.setText("Desconectar")

    def lecturaArduino(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.arduino.inWaiting():
                cadena = self.arduino.readline()
                cadena = cadena.decode()
                cadena = cadena.strip()
                print(cadena)
                if cadena != '':
                    self.datos.addItem(cadena)
                    self.datos.setCurrentRow(self.datos.count() - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


