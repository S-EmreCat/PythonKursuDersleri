# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_cbheckbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnSecilenleriAl.setGeometry(QtCore.QRect(90, 300, 151, 41))
        self.btnSecilenleriAl.setObjectName("btnSecilenleriAl")
        self.llbl_result = QtWidgets.QLabel(self.centralwidget)
        self.llbl_result.setGeometry(QtCore.QRect(290, 140, 121, 71))
        self.llbl_result.setText("")
        self.llbl_result.setObjectName("llbl_result")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 130, 151, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbsinema = QtWidgets.QCheckBox(self.widget)
        self.cbsinema.setObjectName("cbsinema")
        self.verticalLayout.addWidget(self.cbsinema)
        self.cbKitapOkumak = QtWidgets.QCheckBox(self.widget)
        self.cbKitapOkumak.setObjectName("cbKitapOkumak")
        self.verticalLayout.addWidget(self.cbKitapOkumak)
        self.cbspor = QtWidgets.QCheckBox(self.widget)
        self.cbspor.setObjectName("cbspor")
        self.verticalLayout.addWidget(self.cbspor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 21))
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
        self.btnSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
        self.cbsinema.setText(_translate("MainWindow", "Sinema"))
        self.cbKitapOkumak.setText(_translate("MainWindow", "Kitap Okumak"))
        self.cbspor.setText(_translate("MainWindow", "Spor"))
