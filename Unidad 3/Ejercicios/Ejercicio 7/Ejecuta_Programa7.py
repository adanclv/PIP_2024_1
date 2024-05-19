import sys
from PyQt5 import uic, QtWidgets, QtCore

import E_07_Langosta_main
import ejecuta_langosta_dialog
#qtCreatorFile = "P1_ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, E_07_Langosta_main.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        E_07_Langosta_main.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_cotizar.clicked.connect(self.personas)
        self.btn_lista.clicked.connect(self.lista)
        self.line_km.textChanged.connect(self.cambiar)
    # Área de los Slots
    def personas(self):
        num_personas = int(self.line_km.text())

        if num_personas > 0 and num_personas < 200:
            costo_total = num_personas * 95
            self.dialogo = ejecuta_langosta_dialog.MyDialog()
            self.dialogo.setModal(True)
            self.dialogo.txt_resultado.setText(str(costo_total))
            self.dialogo.show()
            self.line_km.clear()
            self.label.setText(" ")

        elif num_personas > 200 and num_personas < 300:
            costo_total = num_personas * 85
            self.dialogo = ejecuta_langosta_dialog.MyDialog()
            self.dialogo.setModal(True)
            self.dialogo.txt_resultado.setText(str(costo_total))
            self.dialogo.show()
            self.line_km.clear()
            self.label.setText(" ")
        else:
            costo_total = num_personas * 75
            self.dialogo = ejecuta_langosta_dialog.MyDialog()
            self.dialogo.setModal(True)
            self.dialogo.txt_resultado.setText(str(costo_total))
            self.dialogo.show()
            self.line_km.clear()
            self.label.setText(" ")

    def lista(self):
        msj = QtWidgets.QMessageBox()
        msj.setText("**La Langosta Ahumada**\n\n"
                    "Lista de precios\n"
                    "0-200 personas: $95\n"
                    "200-300 personas: $85\n"
                    "+300 personas: $75\n")

        msj.exec_()

    def cambiar(self):
      try:
        num_personas = int(self.line_km.text())
        if num_personas > 0 and num_personas < 200:
            self.label.setText("$95")
        elif num_personas > 200 and num_personas < 300:
            self.label.setText("$85")
        else:
            self.label.setText("$75")
      except Exception as e:
          print("ERRROR numero invalido", e)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

