import sys
from PyQt5 import uic, QtWidgets
import serial

qtCreatorFile = "P_21_InterfazConexionArduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Accion.clicked.connect(self.accion)
        self.arduino = None

    # Área de los Slots
    def accion(self):
        txt_btn = self.btn_Accion.text()
        com = self.txt_COM.text()
        if txt_btn == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.lbl_estado.setText("CONECTADO")
            self.btn_Accion.setText("DESCONECTAR")
        elif txt_btn == "DESCONECTAR" and self.arduino.isOpen():
            self.arduino.close()
            self.lbl_estado.setText("DESCONECTADO")
            self.btn_Accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.btn_Accion.setText("DESCONECTAR")
            self.lbl_estado.setText("CONECTADO")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


