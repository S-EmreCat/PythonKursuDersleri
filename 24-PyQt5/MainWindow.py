# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 61, 31))
        self.label_2.setObjectName("label_2")
        self.txt_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(100, 30, 200, 32))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(100, 80, 200, 32))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_topla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_topla.setGeometry(QtCore.QRect(100, 130, 61, 41))
        self.btn_topla.setObjectName("btn_topla")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(240, 130, 61, 41))
        self.btn_bolme.setObjectName("btn_bolme")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(170, 130, 61, 41))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(310, 130, 61, 41))
        self.btn_carpma.setObjectName("btn_carpma")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(100, 190, 181, 51))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 21))
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
        self.label.setText(_translate("MainWindow", "Sayı 1:"))
        self.label_2.setText(_translate("MainWindow", "Sayı 2:"))
        self.btn_topla.setText(_translate("MainWindow", "Toplam"))
        self.btn_bolme.setText(_translate("MainWindow", "Bölme"))
        self.btn_cikarma.setText(_translate("MainWindow", "Çıkarma"))
        self.btn_carpma.setText(_translate("MainWindow", "Çarpma"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonuç:"))
