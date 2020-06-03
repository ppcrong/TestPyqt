# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"    background:#2094D6;\n"
"    border-top:1px solid darkGray;\n"
"    border-bottom:1px solid darkGray;\n"
"    border-right:1px solid darkGray;\n"
"    border-top-right-radius:6px;\n"
"    border-bottom-right-radius:6px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(410, 30, 381, 501))
        self.tabWidget.setStyleSheet("/* The tab widget frame */\n"
"QTabWidget:pane {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTabWidget:tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"it reads QTabBar _not_ QTabWidget */\n"
"QTabBar:tab {\n"
"    background: rgba(255,255,255,40);\n"
"    min-width: 8ex;\n"
"    min-height: 30ex;\n"
"    color:#BFBFBF;\n"
"    font-size:14px;\n"
"    font-weight:200;\n"
"    font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"QTabBar:tab:selected {\n"
"    background: rgba(16,21,102,100);\n"
"    color:white;\n"
"}\n"
"\n"
"QTabBar:tab:hover {\n"
"    background: rgba(16,21,102,30);\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(90, 120, 98, 19))
        self.radioButton.setObjectName("radioButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "INFERENCE"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "GOLDEN"))
