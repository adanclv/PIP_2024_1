import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial

qtCreatorFile = "P_23_InterfazConexionArduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundo = QtCore.QTimer()
        self.segundo.timeout.connect(self.lecturaArduino)

        self.btn_Accion2.clicked.connect(self.controlLED)
        self.estadoLED = 1;

    # Área de los Slots
    def accion(self):
        txt_btn = self.btn_Accion.text()
        com = self.txt_COM.text()
        if txt_btn == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundo.start(100)
            self.btn_Accion.setText("DESCONECTAR")
        elif txt_btn == "DESCONECTAR" and self.arduino.isOpen():
            self.segundo.stop()
            self.arduino.close()
            self.btn_Accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.segundo.start(100)
            self.btn_Accion.setText("DESCONECTAR")

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

    def controlLED(self):
        if not self.arduino is None and self.arduino.isOpen():
            if not self.estadoLED:
                self.btn_Accion2.setText("PRENDER")
            else:
                self.btn_Accion2.setText("APAGAR")
            val = '1' if self.estadoLED == 1 else '0' + '\n'
            print(val)
            self.arduino.write(val.encode())
            self.estadoLED = self.estadoLED * -1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


