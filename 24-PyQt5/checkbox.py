import sys
from PyQt5 import QtWidgets
from checkboxForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)  # Ui_MainWindow içerisindeki setupUi fonksiyonunu çağırdık
        self.ui.cbsinema.stateChanged.connect(self.show_state)
        self.ui.cbKitapOkumak.stateChanged.connect(self.show_state)
        self.ui.cbspor.stateChanged.connect(self.show_state)
        self.ui.btnSecilenleriAl.clicked.connect(self.getAllChecked)
        
    def getAllChecked(self):
        # biz centralwidget kısmındaki checkbox lar ile ilgilendiğimiz için ui.centralwidget şeklinde bir kısıtlama koyduk
        # findChildren(QtWidgets.QCheckBox)  metodu ile aradığımız elemanların checkbox olduğunu belirttik
        items=self.ui.centralwidget.findChildren(QtWidgets.QCheckBox) # seçilen elemanları dizi ile döndürür
        result=''
        for item in items:
            if item.isChecked()==True:
                result+=item.text()+'\n'
        self.ui.llbl_result.setText(result)
    def show_state(self,value):
        cb=self.sender() ## hangi checkbox üzerinde işlem yapıyorsak ona ulaşırız
        print(cb)
        # print(value)
        # print(cb.text())
        # print(cb.isChecked())

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())
         
app()