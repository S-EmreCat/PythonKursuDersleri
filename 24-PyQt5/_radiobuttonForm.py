# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_radiobuttonForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_Ulke = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Ulke.setGeometry(QtCore.QRect(40, 200, 131, 31))
        self.lbl_Ulke.setText("")
        self.lbl_Ulke.setObjectName("lbl_Ulke")
        self.lbl_Egitim = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Egitim.setGeometry(QtCore.QRect(400, 200, 121, 31))
        self.lbl_Egitim.setText("")
        self.lbl_Egitim.setObjectName("lbl_Egitim")
        self.btn_ulke = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ulke.setGeometry(QtCore.QRect(80, 250, 241, 61))
        self.btn_ulke.setObjectName("btn_ulke")
        self.btn_egitim = QtWidgets.QPushButton(self.centralwidget)
        self.btn_egitim.setGeometry(QtCore.QRect(430, 250, 241, 61))
        self.btn_egitim.setObjectName("btn_egitim")
        self.groupBoxUlke = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUlke.setGeometry(QtCore.QRect(19, 10, 281, 181))
        self.groupBoxUlke.setObjectName("groupBoxUlke")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxUlke)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 231, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridUlkeler = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridUlkeler.setContentsMargins(0, 0, 0, 0)
        self.gridUlkeler.setObjectName("gridUlkeler")
        self.radioYunannistan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioYunannistan.setObjectName("radioYunannistan")
        self.gridUlkeler.addWidget(self.radioYunannistan, 6, 0, 1, 1)
        self.radioTurkiye = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioTurkiye.setObjectName("radioTurkiye")
        self.gridUlkeler.addWidget(self.radioTurkiye, 4, 0, 1, 1)
        self.radioAzerbaycan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAzerbaycan.setObjectName("radioAzerbaycan")
        self.gridUlkeler.addWidget(self.radioAzerbaycan, 5, 0, 1, 1)
        self.radioAlmanya = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAlmanya.setObjectName("radioAlmanya")
        self.gridUlkeler.addWidget(self.radioAlmanya, 7, 0, 1, 1)
        self.groupBoxEgitim = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEgitim.setGeometry(QtCore.QRect(350, 20, 271, 171))
        self.groupBoxEgitim.setObjectName("groupBoxEgitim")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxEgitim)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 221, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridEgitim = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridEgitim.setContentsMargins(0, 0, 0, 0)
        self.gridEgitim.setObjectName("gridEgitim")
        self.radioIlkokul = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioIlkokul.setObjectName("radioIlkokul")
        self.gridEgitim.addWidget(self.radioIlkokul, 0, 0, 1, 1)
        self.radioYuksekLisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioYuksekLisans.setObjectName("radioYuksekLisans")
        self.gridEgitim.addWidget(self.radioYuksekLisans, 4, 0, 1, 1)
        self.radioUniversite = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioUniversite.setObjectName("radioUniversite")
        self.gridEgitim.addWidget(self.radioUniversite, 1, 0, 1, 1)
        self.radioLise = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioLise.setObjectName("radioLise")
        self.gridEgitim.addWidget(self.radioLise, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 21))
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
        self.btn_ulke.setText(_translate("MainWindow", "Ülke Seçimi"))
        self.btn_egitim.setText(_translate("MainWindow", "Egitim Seçimi"))
        self.groupBoxUlke.setTitle(_translate("MainWindow", "Ulkeler"))
        self.radioYunannistan.setText(_translate("MainWindow", "Yunanistan"))
        self.radioTurkiye.setText(_translate("MainWindow", "Türkiye"))
        self.radioAzerbaycan.setText(_translate("MainWindow", "Azerbaycan"))
        self.radioAlmanya.setText(_translate("MainWindow", "Almanya"))
        self.groupBoxEgitim.setTitle(_translate("MainWindow", "Eğitim"))
        self.radioIlkokul.setText(_translate("MainWindow", "İlkokul"))
        self.radioYuksekLisans.setText(_translate("MainWindow", "Yüksek Lisans"))
        self.radioUniversite.setText(_translate("MainWindow", "Üniversite"))
        self.radioLise.setText(_translate("MainWindow", "Lise"))