import sys
import Graficacion
from PyQt5 import QtWidgets, QtCore


class MyApp(QtWidgets.QMainWindow, Graficacion.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Graficacion.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

    # Área de los Slots


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


