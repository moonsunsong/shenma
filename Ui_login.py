# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\prioject\dictionary\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 30, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # 用户名输入框
        self.lineUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineUsername.setObjectName("lineUsername")
        self.verticalLayout.addWidget(self.lineUsername)
        # 密码输入框
        self.linePassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.linePassword.setObjectName("linePassword")
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)# 修改
        self.verticalLayout.addWidget(self.linePassword)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 30, 51, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.laUsername = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.laUsername.setObjectName("laUsername")
        self.verticalLayout_2.addWidget(self.laUsername)
        self.laPassword = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.laPassword.setObjectName("laPassword")
        self.verticalLayout_2.addWidget(self.laPassword)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 120, 151, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnRegister = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnRegister.setObjectName("btnRegister")
        self.horizontalLayout.addWidget(self.btnRegister)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "神马网盘"))
        self.laUsername.setText(_translate("MainWindow", "用户名："))
        self.laPassword.setText(_translate("MainWindow", "  密码："))
        self.btnLogin.setText(_translate("MainWindow", "登录"))
        self.btnRegister.setText(_translate("MainWindow", "注册"))

