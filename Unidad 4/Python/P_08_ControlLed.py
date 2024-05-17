import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial

qtCreatorFile = "P_08_ControlLed.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Accion.clicked.connect(self.accion)
        self.arduino = None

        self.btn_enviar.clicked.connect(self.controlLED)

    # Área de los Slots
    def accion(self):
        txt_btn = self.btn_Accion.text()
        com = self.txt_COM.text()
        if txt_btn == "Conectar" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.lbl_estado.setText("Conectado")
            self.btn_Accion.setText("Desconectar")
        elif txt_btn == "Desconectar" and self.arduino.isOpen():
            self.arduino.close()
            self.lbl_estado.setText("Desconectado")
            self.btn_Accion.setText("Reconectear")
        else:
            self.arduino.open()
            self.lbl_estado.setText("Conectado")
            self.btn_Accion.setText("Desconectar")

    def controlLED(self):
        if not self.arduino is None and self.arduino.isOpen():
            valor = self.txt_valor.text()
            self.arduino.write(valor.encode())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


