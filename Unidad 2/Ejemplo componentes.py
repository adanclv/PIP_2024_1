from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Slider Example")

        slider = QSlider(self)
        slider.setOrientation(1)  # Orientación horizontal
        slider.valueChanged.connect(self.slider_changed)

    def slider_changed(self, value):
        print("Valor del Slider:", value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setGeometry(100, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())