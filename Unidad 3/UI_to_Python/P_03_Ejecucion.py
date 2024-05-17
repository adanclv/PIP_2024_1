import P_03_Ejemplo
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore


class MyApp(QtWidgets.QMainWindow, P_03_Ejemplo.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        P_03_Ejemplo.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_saludo.clicked.connect(self.saludar)

        self.btn_new = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new.setGeometry(QtCore.QRect(440, 210, 93, 28))
        self.btn_new.setObjectName('btn_new')

        self.btn_new.setText('Button 2')
        self.btn_new.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        pass
        try:
            self.btn_new.setText("hola mundo")
            self.btn_new.hide()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


