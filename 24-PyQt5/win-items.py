import sys
from PyQt5 import QtWidgets


# basit şekilde kendimiz bir kaç elemanı win üzerine ekleyip kaydet işlemi yaptık
# move ile konum belirlerken resize ile boyutlandırma yapıyoruz

class MyWinDow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWinDow,self).__init__()
        self.setWindowTitle("First Application")
        self.setGeometry(200,200,500,500)
        self.setToolTip("my tooltip")
        self.initUI()

    def initUI(self):    
        self.lbl_name=QtWidgets.QLabel(self) 
        self.lbl_name.setText("adınız: ")
        self.lbl_name.move(50,30) 
        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText("soyadınız: ")
        self.lbl_surname.move(50,70) 
        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,150)
        self.txt_name=QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_surname=QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)

        self.btn_save=QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked)
        
    
    def clicked(self):
        self.lbl_result.setText("ad: "+self.txt_name.text()+" soyad: "+self.txt_surname.text())


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWinDow()
    win.show()
    sys.exit(app.exec_())
window()



