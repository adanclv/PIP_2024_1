# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Enviando.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_logoUAT = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logoUAT.setGeometry(QtCore.QRect(30, 10, 181, 71))
        self.lbl_logoUAT.setText("")
        self.lbl_logoUAT.setPixmap(QtGui.QPixmap(":/logo/Imagenes/UAT-Escudo-2024.png"))
        self.lbl_logoUAT.setScaledContents(True)
        self.lbl_logoUAT.setObjectName("lbl_logoUAT")
        self.lbl_logoFIT = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logoFIT.setGeometry(QtCore.QRect(410, 20, 211, 61))
        self.lbl_logoFIT.setText("")
        self.lbl_logoFIT.setPixmap(QtGui.QPixmap(":/logo/Imagenes/LogoFIT.png"))
        self.lbl_logoFIT.setScaledContents(True)
        self.lbl_logoFIT.setObjectName("lbl_logoFIT")
        self.lbl_logoCT = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logoCT.setGeometry(QtCore.QRect(570, 320, 71, 51))
        self.lbl_logoCT.setText("")
        self.lbl_logoCT.setPixmap(QtGui.QPixmap(":/logo/Imagenes/logoCT.png"))
        self.lbl_logoCT.setScaledContents(True)
        self.lbl_logoCT.setObjectName("lbl_logoCT")
        self.lbl_resultado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_resultado.setGeometry(QtCore.QRect(190, 250, 261, 31))
        self.lbl_resultado.setStyleSheet("font: 9pt \"Yu Gothic UI\";\n"
"")
        self.lbl_resultado.setText("")
        self.lbl_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 200, 151, 31))
        self.label_3.setStyleSheet("font: 10pt \"Yu Gothic UI\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.btn_sumar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sumar.setGeometry(QtCore.QRect(270, 140, 93, 28))
        self.btn_sumar.setObjectName("btn_sumar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Resultado:"))
        self.btn_sumar.setText(_translate("MainWindow", "Sumar"))
import recursos_rc