# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\prioject\projectPan\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.laUsericon = QtWidgets.QLabel(self.centralwidget)
        self.laUsericon.setGeometry(QtCore.QRect(10, 10, 54, 51))
        self.laUsericon.setText("")
        self.laUsericon.setPixmap(QtGui.QPixmap("C:/Users/tarena/Desktop/favicon.png"))
        self.laUsericon.setObjectName("laUsericon")
        self.laUsername = QtWidgets.QLabel(self.centralwidget)
        self.laUsername.setGeometry(QtCore.QRect(70, 22, 81, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.laUsername.setFont(font)
        self.laUsername.setObjectName("laUsername")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(290, 50, 221, 341))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 54, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:/Users/tarena/Desktop/favicon.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(80, 11, 54, 51))
        self.label_10.setObjectName("label_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btnUpload = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpload.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.btnUpload.setObjectName("btnUpload")
        self.btndoownload = QtWidgets.QPushButton(self.centralwidget)
        self.btndoownload.setGeometry(QtCore.QRect(390, 20, 75, 23))
        self.btndoownload.setObjectName("btndoownload")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 350, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upload = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.upload.setObjectName("upload")
        self.horizontalLayout.addWidget(self.upload)
        self.uploadS = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.uploadS.setObjectName("uploadS")
        self.horizontalLayout.addWidget(self.uploadS)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.download = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.download.setObjectName("download")
        self.horizontalLayout.addWidget(self.download)
        self.downloadS = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.downloadS.setObjectName("downloadS")
        self.horizontalLayout.addWidget(self.downloadS)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 251, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.d_tab = QtWidgets.QWidget()
        self.d_tab.setObjectName("d_tab")
        self.d_filename = QtWidgets.QLabel(self.d_tab)
        self.d_filename.setGeometry(QtCore.QRect(70, 10, 54, 51))
        self.d_filename.setObjectName("d_filename")
        self.d_fileicon = QtWidgets.QLabel(self.d_tab)
        self.d_fileicon.setGeometry(QtCore.QRect(0, 9, 54, 51))
        self.d_fileicon.setText("")
        self.d_fileicon.setPixmap(QtGui.QPixmap("C:/Users/tarena/Desktop/favicon.png"))
        self.d_fileicon.setObjectName("d_fileicon")
        self.progressBar = QtWidgets.QProgressBar(self.d_tab)
        self.progressBar.setGeometry(QtCore.QRect(0, 60, 231, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.d_tab, "")
        self.u_tab = QtWidgets.QWidget()
        self.u_tab.setObjectName("u_tab")
        self.tabWidget.addTab(self.u_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.laUsername.setText(_translate("MainWindow", "myname"))
        self.label_10.setText(_translate("MainWindow", "文件名"))
        self.btnUpload.setText(_translate("MainWindow", "上传"))
        self.btndoownload.setText(_translate("MainWindow", "下载"))
        self.upload.setText(_translate("MainWindow", "上传速度:"))
        self.uploadS.setText(_translate("MainWindow", "0 KB/s"))
        self.download.setText(_translate("MainWindow", "下载速度:"))
        self.downloadS.setText(_translate("MainWindow", "0 KB/s"))
        self.d_filename.setText(_translate("MainWindow", "文件名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.d_tab), _translate("MainWindow", "下载列表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.u_tab), _translate("MainWindow", "上传列表"))

