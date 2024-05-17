import sys
import Graficacion
from PyQt5 import QtWidgets, QtCore
import matplotlib.pyplot as plt


class MyApp(QtWidgets.QMainWindow, Graficacion.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Graficacion.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_graficar.clicked.connect(self.graficar)
        self.btn_establecer.clicked.connect(self.titulo)
        self.btn_off.clicked.connect(self.grilla)
        self.btn_limpiar.clicked.connect(self.limpiar)

        self.cb_estilo.addItem('Estilo: :', ':')
        self.cb_estilo.addItem('Estilo: -', '-')
        self.cb_estilo.addItem('Estilo: --', '--')
        self.cb_estilo.addItem('Estilo: -.', '-.')
        self.cb_estilo.currentIndexChanged.connect(self.estiloLinea)

        self.cb_color.addItem('Negro', 'black')
        self.cb_color.addItem('Rojo', 'red')
        self.cb_color.addItem('Azul', 'blue')
        self.cb_color.addItem('Verde', 'green')
        self.cb_color.currentIndexChanged.connect(self.colorLinea)

        self.ancho.setValue(1)
        self.ancho.setMaximum(10)
        self.ancho.setMinimum(1)
        self.ancho.setSingleStep(1)
        self.ancho.valueChanged.connect(self.anchoLinea)

        #Valor por default
        self.estiloLinea = ':'
        self.colorLinea = 'black'
        self.anchoLinea = 1

        self.xmin.setValue(0)
        self.xmin.setMaximum(10000)
        self.xmin.setMinimum(-10000)
        self.xmin.setSingleStep(1)
        self.xmin.valueChanged.connect(self.minX)

        self.xmax.setValue(10)
        self.xmax.setMaximum(10000)
        self.xmax.setMinimum(-10000)
        self.xmax.setSingleStep(1)
        self.xmax.valueChanged.connect(self.maxX)

        self.divisiones1.setValue(10)
        self.divisiones1.setMaximum(10)
        self.divisiones1.setMinimum(1)
        self.divisiones1.setSingleStep(1)
        self.divisiones1.valueChanged.connect(self.divisionesX)

        self.ymin.setValue(0)
        self.ymin.setMaximum(10000)
        self.ymin.setMinimum(-10000)
        self.ymin.setSingleStep(1)
        self.ymin.valueChanged.connect(self.minY)

        self.ymax.setValue(10)
        self.ymax.setMaximum(10000)
        self.ymax.setMinimum(-10000)
        self.ymax.setSingleStep(1)
        self.ymax.valueChanged.connect(self.maxY)

        self.divisiones2.setValue(10)
        self.divisiones2.setMaximum(10)
        self.divisiones2.setMinimum(1)
        self.divisiones2.setSingleStep(1)
        self.divisiones2.valueChanged.connect(self.divisionesY)

        self.xMax = 10
        self.xMin = 1
        self.xDivisiones = 10
        self.yMax = 10
        self.yMin = 1
        self.yDivisiones = 10

        self.btn_off.setText('Off')

    # Área de los Slots
    def graficar(self):
        polinomio = self.txt_polinomio.text()
        polinomio = polinomio.replace("^", "**")

        # x = [i for i in range(-5,6)] #[-5 5]
        x = [i for i in range(self.xMin, self.xMax + 1)]
        print("Valores de X: ")
        print(x)

        # y = polinomio.replace("x","*("+str(x[0])+")")
        y = [eval(polinomio.replace("x", "*(" + str(i) + ")")) for i in x]
        print("Valores de Y: ")
        print(y)

        # self.ax.plot(x,y)
        # self.ax.plot(x, y,"g*--")
        self.ax.plot(x, y,

                     linestyle=self.estiloLinea,  #: - -- -.
                     color=self.colorLinea,  # color de la linea
                     linewidth=self.anchoLinea,  # tamaño de la linea
                     marker="x",  # o . *  x   1
                     markersize=12,
                     markerfacecolor="yellow",  # color interno del marcador
                     markeredgewidth=2,  # tamaño del borde del marcador
                     markeredgecolor="red",  # color del borde del marcador
                     dash_capstyle="butt",  # dash or solid : "butt" "round" "projecting"
                     dash_joinstyle="miter"  # dash or solid : "miter" "round" "bevel"
                     )

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax + 1)
        self.ax.set_ylim(self.yMin, self.yMax + 1)

        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")

        # totalelementosenX/totaldivisionesDeseadas = 8
        # mediante un ciclo se obtiene:

        # si comienzo con xmin en 0 seria:
        # xtick = [0, 10, 20, 30, 40, 50, 60, 70, 80]

        # si comienzo con xmin en n seria:
        xtick = []
        for i in range(-30, 30 + 1, 10):
            xtick.append(i)
        print("Ticks para X: ")
        print(xtick)

        xtick = [2, 5, 15, 25, 35, 45, 55, 65, 75, 85]

        self.ax.set_xticks(xtick)

        self.ax.set_yticks(y)  # NOTA.. CHECK!

        # una posibilidad para establecer los ticks sería:
        # Tomar el conjunto y dividirlo entre el total de "divisiones" que el usuario desee

        self.canvas.draw()

    def titulo(self):
        t = self.txt_titulo.text()
        self.ax.set_title(t)  # establece el titulo

        self.canvas.draw()  # aplica los cambios

    def grilla(self):
        texto = self.btn_off.text()
        if texto == "OFF":
            self.btn_off.setText("ON")
            plt.grid(False)
        else:
            self.btn_off.setText("OFF")
            plt.grid(True)

        self.canvas.draw()

    def limpiar(self):
        plt.cla()  # borra_todo
        self.canvas.draw()

    def estiloLinea(self):
        estilo = self.cb_estilo.currentData()
        self.estiloLinea = estilo

        self.limpiar()
        self.graficar()

    def colorLinea(self):
        color = self.cb_color.currentData()
        self.colorLinea = color

        self.limpiar()
        self.graficar()

    def anchoLinea(self):
        ancho = self.ancho.value()
        self.anchoLinea = ancho

        self.limpiar()
        self.graficar()

    def minX(self):
        self.xMin = self.xmin.value()
        self.limpiar()
        self.graficar()
    def maxX(self):
        self.xMax = self.xmax.value()
        self.limpiar()
        self.graficar()
    def divisionesX(self):
        self.xDivisiones = self.divisiones1.value()
        self.limpiar()
        self.graficar()
    def minY(self):
        self.yMin = self.ymin.value()
        self.limpiar()
        self.graficar()
    def maxY(self):
        self.yMax = self.ymax.value()
        self.limpiar()
        self.graficar()
    def divisionesY(self):
        self.yDivisiones = self.divisiones2.value()
        self.limpiar()
        self.graficar()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


