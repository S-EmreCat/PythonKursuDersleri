from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        # herhangi bir text label butona ulaşmak istediğimizde artık self.ui ile ulaşacağız (self.ui.txt_sayi2) gibi
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self) # app projemize designerdaki elemanlar aktarılsın

        # click atamalarını burada yapıyoruz
        self.ui.btn_topla.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
    def hesapla(self):
        sender=self.sender().text()
        print(sender)
        result=0
        if sender=="Toplam":
            result=int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        elif sender=='Çıkarma':
            result=int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        elif sender=="Çarpma":
            result=int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        elif sender=="Bölme":
            result=int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())
        self.ui.lbl_sonuc.setText("Sonuc: "+str(result)) 


application=QtWidgets.QApplication(sys.argv)
win=MyApp()
win.show()
sys.exit(application.exec_())

