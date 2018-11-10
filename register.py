'''
这是界面的控制代码
'''
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QMessageBox,QLabel
# from Ui_register import *
import Ui_register
import Ui_login
from PyQt5.QtCore import Qt,QRect
import sys
# import pymysql
import tools.mysqltool as mysqltool
from socket import *

HOST = '176.209.102.47'
PORT = 7777
ADDR = (HOST,PORT)

def varify_info(sockfd,username,password,mod):
    msg = mod+" %s %s"%(username,password)
    sockfd.send(msg.encode())
    r = sockfd.recv(128).decode()
    return r

class Login_UI(Ui_login.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.btnRegister.clicked.connect(self.toRegister)
        self.btnLogin.clicked.connect(self.doLogin)
    def doLogin(self):
        # 获取用户名和密码
        username = self.lineUsername.text()
        password = self.linePassword.text()
        if not username or not password:
            QMessageBox.about(self,'警告','请填写完整信息!')
            return
        try:
            sockfd = socket()
            sockfd.connect(ADDR)
        except:
            QMessageBox.about(self,'信息','无法连接服务器!')
            return
        r = varify_info(sockfd,username,password,"L")#L代表登录
        if r == 'SUCCESS':
            # 登录成功,进入网盘客户端界面
            print("登录成功")
        elif r == 'FAIL':
            # 登录失败
            QMessageBox.about(self,'信息','用户名或密码错误!')
        elif r == 'ServerError':
            QMessageBox.about(self,'信息','服务器出错!')
        sockfd.close()
    def toRegister(self):
        self.hide()
        self.register_ui = Register_UI_Control()
        self.register_ui.show()



class Register_UI_Control(Ui_register.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.sockfd = socket()
        self.setupUi(self)
        self.initUI()
    def initUI(self):
        self.btnRegist.clicked.connect(self.doRegister)
        self.checkBox.stateChanged.connect(self.promise)
        self.btnReturnLogin.clicked.connect(self.toLogin)
        # 初始化完成,显示界面
        self.show()
    def promise(self):
        if self.checkBox.checkState() == Qt.Checked:
            self.btnRegist.setEnabled(True)
        elif self.checkBox.checkState() == Qt.Unchecked:
            self.btnRegist.setEnabled(False)
    def toLogin(self):
        # 显示登录界面
        self.hide()
        # 登录界面初始化
        self.login_ui = Login_UI()
        self.login_ui.show()
    # 处理注册的逻辑
    def doRegister(self):
        username = self.lineUsername.text()
        password = self.linePass.text()
        password2 = self.linePass2.text()
        # 验证用户名和密码是否合法
        if " " in username or " " in password:
            QMessageBox.about(self,'警告','请勿使用空格!')
            return
        if not username or not password or not password2:
            QMessageBox.about(self,'警告','请填写完整信息!')
            return
        if  password != password2:
            QMessageBox.about(self,'警告','两次密码不一致')
            return
        # 发送信息(用户名和密码)给服务器
        try:
            # sockfd = socket()
            self.sockfd.connect(ADDR)
        except:
            QMessageBox.about(self,'信息','无法连接服务器!')
            return
        r = varify_info(self.sockfd,username,password,"R")#R代表注册
        if r == 'OK':
            # 注册成功
            QMessageBox.about(self,'完成','注册成功!')
            self.toLogin()
            return
        elif r == "USED":
            # 用户名已存在
            QMessageBox.about(self,'警告','该用户已存在!')
            return
        else:
            # 服务器故障
            QMessageBox.about(self,'警告','服务器故障!')
            return

        # 进入数据库查询(测试)
        # self.linkDB(username,password)

    # def linkDB(self,username,password):
    #     msql = mysqltool.Mysqltool('tt')
    #     msql.open()
    #     try:
    #         l = msql.all("select username from userinfo")
    #     except:
    #         print("数据库出错!")
    #     for i in l:
    #         if i[0] == username:
    #             QMessageBox.about(self,'警告','该用户已存在!')
    #             return
    #     # 将数据存入数据库
    #     try:
    #         msql.insert_update_delete("insert into userinfo(username,password) values('%s','%s')"%(username,password))
    #     except:
    #         print("插入数据库失败")
    #         return
    #     QMessageBox.about(self,'完成','注册成功!')
    #     # 登录成功隐藏注册界面
    #     self.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 注册界面初始化
    register_ui = Register_UI_Control()
    sys.exit(app.exec_())


