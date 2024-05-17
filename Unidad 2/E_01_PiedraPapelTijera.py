import sys
import random as rand
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "E_01_PiedraPapelTijera.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.piedra.clicked.connect(self.match)
        self.papel.clicked.connect(self.match)
        self.tijera.clicked.connect(self.match)
        self.btn_comenzar.clicked.connect(self.comenzar)
        self.segundoPlano = QtCore.QTimer()

        self.inicio()
        self.moves = {
            0: ['piedra', ':/variable/Imagenes/rock.png'],
            1: ['papel', ':/variable/Imagenes/paper.png'],
            2: ['tijera', ':/variable/Imagenes/scissors.png']
        }
        self.won = ['piedra-tijera', 'papel-piedra', 'tijera-papel'] # combinaciones
        self.lost = ['piedra-papel', 'papel-tijera', 'tijera-piedra']

    # Área de los Slots
    def inicio(self):
        self.piedra.setEnabled(False)
        self.papel.setEnabled(False)
        self.tijera.setEnabled(False)
        self.btn_comenzar.setEnabled(True)

    def comenzar(self):
        self.piedra.setEnabled(True)
        self.papel.setEnabled(True)
        self.tijera.setEnabled(True)
        self.lbl_player.setText('0')
        self.lbl_pc.setText('0')
        self.lbl_resultado.setText('')
        self.btn_comenzar.setEnabled(False)

    def match(self):
        player = self.sender().objectName() # nombre del btn presionado
        r = rand.randint(0,2) # num random
        self.jugada = f'{player}-{self.moves[r][0]}' # jugada
        if player == 'piedra': # desaparcen los demas
            self.piedra.clicked.disconnect()
            self.papel.setVisible(False)
            self.tijera.setVisible(False)
        elif player == 'papel':
            self.papel.clicked.disconnect()
            self.piedra.setVisible(False)
            self.tijera.setVisible(False)
        else:
            self.tijera.clicked.disconnect()
            self.piedra.setVisible(False)
            self.papel.setVisible(False)

        self.img_pc.setPixmap(QtGui.QPixmap(self.moves[r][-1]))
        self.segundoPlano.singleShot(1000, self.reset)
        self.win() # quien gano

    def win(self):
        puntosPlayer = int(self.lbl_player.text())
        puntosPc = int(self.lbl_pc.text())
        if self.jugada in self.won:
            puntosPlayer += 1
        elif self.jugada in self.lost:
            puntosPc += 1

        self.lbl_player.setText(str(puntosPlayer))
        self.lbl_pc.setText(str(puntosPc))

        if puntosPlayer == 3 or puntosPc == 3:
            self.winner()

    def winner(self):
        puntosPlayer = int(self.lbl_player.text())
        puntosPc = int(self.lbl_pc.text())
        if puntosPlayer == 3:
            self.lbl_resultado.setText('Ganaste')
        elif puntosPc == 3:
            self.lbl_resultado.setText('Perdiste')
        self.inicio()

    def reset(self):
        self.piedra.setVisible(True)
        self.papel.setVisible(True)
        self.tijera.setVisible(True)
        self.piedra.clicked.connect(self.match)
        self.papel.clicked.connect(self.match)
        self.tijera.clicked.connect(self.match)
        self.img_pc.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


