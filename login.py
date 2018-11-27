'''
登录界面的控制代码
'''
from Ui_login import *
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QMessageBox
import sys

class Login_UI(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()   
    def initUI(self):
        self.show()
        pass
    def toRegister(self):
        self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Login_UI()
    sys.exit(app.exec_())




