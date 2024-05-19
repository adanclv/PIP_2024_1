import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial

qtCreatorFile = "P_09_ControlLeds_ArrayV1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Accion.clicked.connect(self.accion)
        self.arduino = None

        self.btn_enviar.clicked.connect(self.enviar_Datos)

        self.comboBox.addItem("Selecciona...")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")
        self.comboBox.addItem("5")
        self.comboBox.addItem("6")
        self.comboBox.addItem("7")
        self.comboBox.addItem("8")
        self.comboBox.addItem("9")
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

    def enviar_Datos(self):
        if not self.arduino is None and self.arduino.isOpen():
            led = self.comboBox.currentText()
            if led != "Selecciona...":
                valor = led + '\n'
                self.arduino.write(valor.encode())
               # if self.btn_enviar.text() == "Encender":
                #    self.btn_enviar.setText("Apagar")
                #else:
                 #   self.btn_enviar.setText("Encender")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())