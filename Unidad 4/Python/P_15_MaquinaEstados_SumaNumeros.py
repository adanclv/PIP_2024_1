import sys
from PyQt5 import uic, QtWidgets
import serial

qtCreatorFile = "P_15_MaquinaEstados_SumaNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_enviar.clicked.connect(self.enviar)
        self.arduino = None
        self.resultado_pendiente = False

    # Área de los Slots
    def conectar(self):
        txt_btn = self.btn_conectar.text()
        com = self.txt_COM.text()
        if txt_btn == "Conectar" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.lbl_estado.setText("Arduino conectado")
            self.btn_conectar.setText("Desconectar")
        elif txt_btn == "Desconectar" and self.arduino.isOpen():
            self.arduino.close()
            self.lbl_estado.setText("Arduino desconectado")
            self.btn_conectar.setText("Conectar")
        else:
            self.arduino.open()
            self.lbl_estado.setText("Arduino conectado")
            self.btn_conectar.setText("Desconectar")

    def enviar(self):
        if self.arduino is not None and self.arduino.isOpen():
            datos = self.txt_ingreso.text().split(',')  # Dividir los datos por comas
            for dato in datos:
                dato = dato.strip()  # Eliminar espacios en blanco alrededor del dato
                if dato:  # Verificar que el dato no esté vacío
                    self.arduino.write((dato + '\n').encode())
                    instruccion = self.arduino.readline().decode().strip()
                    self.lbl_instruccion.setText(instruccion)

            # Leer y mostrar el resultado
            resultado = self.arduino.readline().decode().strip()
        self.txt_ingreso.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
