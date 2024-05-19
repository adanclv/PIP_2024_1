import sys
from PyQt5 import uic, QtWidgets

import main_viajes
import ejecuta_minimoPersonas_viajes
import ejecuta_costo_viajes
#qtCreatorFile = "P1_ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, main_viajes.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        main_viajes.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_continuar.clicked.connect(self.continuar)
        self.combo_bus.addItem("Selecciona...", 0)
        self.combo_bus.addItem("A", 2)
        self.combo_bus.addItem("B", 2.5)
        self.combo_bus.addItem("C", 3.0)



    # Área de los Slots
    def continuar(self):
        try:
            personas = int(self.line_personas.text())
            km_recorridos = int(self.line_km.text())
            costo_autobus = self.combo_bus.currentData()
            if personas >= 20:
                costo = costo_autobus * personas * km_recorridos
                self.dialogo = ejecuta_costo_viajes.MyDialog()
                self.dialogo.setModal(True)
                self.dialogo.txt_resultado.setText(str(costo))
                self.dialogo.txt_resultado_2.setText(str(costo_autobus))
                self.dialogo.show()

            else:
                self.eleccion()
        except Exception as e:
            print("Error", e)
    def eleccion(self):
        self.dialogo = ejecuta_minimoPersonas_viajes.MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.btn_continuar.clicked.connect(self.continuar_viaje)
        self.dialogo.btn_cancelar.clicked.connect(self.cancelar)
        self.dialogo.show()

    def cancelar(self):
        self.dialogo.close()
    def continuar_viaje(self):
        km_recorridos = int(self.line_km.text())
        costo_autobus = self.combo_bus.currentData()
        costo = costo_autobus * 20 * km_recorridos
        self.dialogo = ejecuta_costo_viajes.MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.txt_resultado.setText(str(costo))
        self.dialogo.txt_resultado_2.setText(str(costo_autobus))
        self.dialogo.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

