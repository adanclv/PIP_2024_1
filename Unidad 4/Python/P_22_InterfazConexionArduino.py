import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
import serial
# hola que hace
# ta buenardo esto la vdd
qtCreatorFile = "P_22_InterfazConexionArduino.ui"  # Nombre del archivo aquí.
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

    # Área de los Slots
    def accion(self):
        txt_btn = self.btn_Accion.text()
        com = self.txt_COM.text()
        if txt_btn == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundo.start(1000)
            self.lbl_estado.setText("CONECTADO")
            self.btn_Accion.setText("DESCONECTAR")
        elif txt_btn == "DESCONECTAR" and self.arduino.isOpen():
            self.segundo.stop()
            self.arduino.close()
            self.lbl_estado.setText("DESCONECTADO")
            self.btn_Accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.segundo.start(1000)
            self.lbl_estado.setText("CONECTADO")
            self.btn_Accion.setText("DESCONECTAR")

    def lecturaArduino(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.arduino.inWaiting():
                cadena = self.arduino.readline()
                cadena = cadena.decode()
                cadena = cadena.strip()
                print(cadena)
                if cadena != "":
                    self.dato.addItem(cadena)
                    self.dato.setCurrentRow(self.dato.count() - 1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


