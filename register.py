from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QMessageBox
from Ui_register import *
from PyQt5.QtCore import Qt
import sys
import pymysql
import tools.mysqltool as mysqltool
from socket import *


class Register_UI(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
    def initUI(self):
        self.pushButton.clicked.connect(self.get_u_p)
        self.checkBox.stateChanged.connect(self.promise)
        self.show()
    
    def promise(self):
        if self.checkBox.checkState() == Qt.Checked:
            self.pushButton.setEnabled(True)
        elif self.checkBox.checkState() == Qt.Unchecked:
            self.pushButton.setEnabled(False)

    def get_u_p(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        password2 = self.lineEdit_3.text()
        if not username or not password or not password2:
            QMessageBox.about(self,'警告','请填写完整信息!')
            return
        if  password != password2:
            QMessageBox.about(self,'警告','两次密码不一致')
            return
        
        # 发送信息给服务器


        # 进入数据库查询
        self.linkDB(username,password)

    def linkDB(self,username,password):
        msql = mysqltool.Mysqltool('tt')
        msql.open()
        try:
            l = msql.all("select username from userinfo")
        except:
            print("数据库出错!")
        for i in l:
            if i[0] == username:
                QMessageBox.about(self,'警告','该用户已存在!')
                return
        # 将数据存入数据库
        try:
            msql.insert_update_delete("insert into userinfo(username,password) values('%s','%s')"%(username,password))
        except:
            print("插入数据库失败")
            return
        QMessageBox.about(self,'完成','注册成功!')
        self.hide()

        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Register_UI()
    sys.exit(app.exec_())


