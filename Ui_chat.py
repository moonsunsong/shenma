# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\project\chat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 180))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 3, 1)
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralWidget)
        self.fontComboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout.addWidget(self.fontComboBox, 3, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralWidget)
        self.treeWidget.setMinimumSize(QtCore.QSize(1, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 1, 6, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 160))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "用户名"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "主机名"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "用户IP"))
        self.pushButton.setText(_translate("MainWindow", "发送"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_CMainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

