import sys
from PyQt5 import QtWidgets
from _radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        # başlangıçta bir tanesi seçili gelsin diye atama yapıyoruz
        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioLise.setChecked(True)
# radio butonların işaretlendiğini kontrol etmek için toggled fonk kullanılır
        self.ui.radioTurkiye.toggled.connect(self.onclickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onclickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onclickedUlke)
        self.ui.radioYunannistan.toggled.connect(self.onclickedUlke)
        self.ui.radioLise.toggled.connect(self.onclickedEgitim)
        self.ui.radioIlkokul.toggled.connect(self.onclickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onclickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onclickedEgitim)
        self.ui.btn_ulke.clicked.connect(self.getSelectedUlke)
        self.ui.btn_egitim.clicked.connect(self.getSelectedEgitim)
    def onclickedUlke(self):
        ##  seçilen radiobutonu bulmak için self.sender() yeterli biz console ekranında kontrol için kontrol yapıyoruz
        rb=self.sender()  
        if rb.isChecked():
            print("seçilen radio:"+rb.text())
    def onclickedEgitim(self):
        ##  seçilen radiobutonu bulmak için self.sender() yeterli biz console ekranında kontrol için kontrol yapıyoruz
        rb=self.sender()
        if rb.isChecked():
            print("seçilen radio:"+rb.text())
    
    def getSelectedUlke(self):
        items=self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for item in items:
            if item.isChecked():
                self.ui.lbl_Ulke.setText("seçilen ülke: " +item.text())
    def getSelectedEgitim(self):
        items=self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for item in items:
            if item.isChecked():
                self.ui.lbl_Egitim.setText("seçilen eğitim: " +item.text())
                  
            

app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())