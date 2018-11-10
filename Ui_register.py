# -*- coding: utf-8 -*-
'''
注册界面UI
'''


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 30, 160, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # 用户名文本框
        self.lineUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineUsername.setObjectName("lineUsername")
        self.verticalLayout.addWidget(self.lineUsername)
        # 密码文本框
        self.linePass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.linePass.setObjectName("linePass")
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)# 修改
        self.verticalLayout.addWidget(self.linePass)
        # 第二次输入的密码文本框
        self.linePass2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.linePass2.setObjectName("linePass2")
        self.linePass2.setEchoMode(QtWidgets.QLineEdit.Password)# 修改
        self.verticalLayout.addWidget(self.linePass2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 40, 71, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.laUsername = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.laUsername.setFont(font)
        self.laUsername.setObjectName("laUsername")
        self.verticalLayout_2.addWidget(self.laUsername)
        self.laPass1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.laPass1.setFont(font)
        self.laPass1.setObjectName("laPass1")
        self.verticalLayout_2.addWidget(self.laPass1)
        self.laPass2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.laPass2.setFont(font)
        self.laPass2.setObjectName("laPass2")
        self.verticalLayout_2.addWidget(self.laPass2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 250, 131, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRegist = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnRegist.setObjectName("btnRegist")
        self.btnRegist.setEnabled(False)# 将注册按钮变灰
        self.horizontalLayout.addWidget(self.btnRegist)
        self.laWarning = QtWidgets.QLabel(self.centralwidget)
        self.laWarning.setGeometry(QtCore.QRect(60, 190, 54, 12))
        self.laWarning.setObjectName("laWarning")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 210, 301, 16))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # 添加 返回登录 的按钮
        self.btnReturnLogin = QtWidgets.QPushButton(self)
        self.btnReturnLogin.setObjectName("btnReturnLogin")
        self.btnReturnLogin.setGeometry(QtCore.QRect(312, 290, 68, 30))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "神马网盘"))
        self.laUsername.setText(_translate("MainWindow", " 用户名："))
        self.laPass1.setText(_translate("MainWindow", "   密码："))
        self.laPass2.setText(_translate("MainWindow", "确认密码："))
        self.btnRegist.setText(_translate("MainWindow", "注册"))
        self.laWarning.setText(_translate("MainWindow", "警告："))
        self.checkBox.setText(_translate("MainWindow", "请勿使用本网盘上传非法文件，否则后果自负！"))
        self.btnReturnLogin.setText(_translate("MainWindow", "返回登录"))

