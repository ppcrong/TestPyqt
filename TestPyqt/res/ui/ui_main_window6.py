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
"                    background:#2094D6;\n"
"                    border-top:1px solid darkGray;\n"
"                    border-bottom:1px solid darkGray;\n"
"                    border-right:1px solid darkGray;\n"
"                    border-top-right-radius:6px;\n"
"                    border-bottom-right-radius:6px;\n"
"                    }\n"
"                ")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(410, 30, 381, 501))
        self.tabWidget.setStyleSheet("/* The tab widget frame */\n"
"                                            QTabWidget:pane {\n"
"                                            border: none;\n"
"                                            background-color: rgba(16,21,102,100);\n"
"                                            border-top-left-radius: 8px;\n"
"                                            border-bottom-left-radius: 8px;\n"
"                                            }\n"
"\n"
"                                            QTabWidget:tab-bar {\n"
"                                            alignment: left;\n"
"                                            }\n"
"\n"
"                                            /* Style the tab using the tab sub-control. Note that\n"
"                                            it reads QTabBar _not_ QTabWidget */\n"
"                                            QTabBar:tab {\n"
"                                            background: rgba(255,255,255,40);\n"
"                                            min-width: 8ex;\n"
"                                            min-height: 30ex;\n"
"                                            color:#BFBFBF;\n"
"                                            font-size:14px;\n"
"                                            font-weight:200;\n"
"                                            font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"                                            border-top-right-radius: 8px;\n"
"                                            border-bottom-right-radius: 8px;\n"
"                                            }\n"
"\n"
"                                            QTabBar:tab:selected {\n"
"                                            background: rgba(16,21,102,100);\n"
"                                            color:white;\n"
"                                            }\n"
"\n"
"                                            QTabBar:tab:hover {\n"
"                                            background: rgba(16,21,102,30);\n"
"                                            }\n"
"                                        ")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("                                QPushButton{\n"
"                                border:none;\n"
"                                color:white;\n"
"                                font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"                                text-align:left;\n"
"                                padding: 5px;\n"
"                                }\n"
"\n"
"                                QPushButton:disabled{color:#BFBFBF;}\n"
"                                QPushButton#btn_1:hover{border-left:4px solid red;font-weight:700;}\n"
"                                QPushButton#btn_2:hover{border-left:4px solid red;font-weight:700;}\n"
"                                QPushButton#btn_3:hover{border-left:4px solid red;font-weight:700;}\n"
"                                QPushButton#btn_4:hover{border-left:4px solid red;font-weight:700;}\n"
"\n"
"")
        self.tab.setObjectName("tab")
        self.layout_tab = QtWidgets.QGridLayout(self.tab)
        self.layout_tab.setObjectName("layout_tab")
        self.btn_1 = QtWidgets.QPushButton(self.tab)
        self.btn_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ic_raw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_1.setIcon(icon)
        self.btn_1.setObjectName("btn_1")
        self.layout_tab.addWidget(self.btn_1, 0, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.tab)
        self.btn_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ic_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_2.setIcon(icon1)
        self.btn_2.setObjectName("btn_2")
        self.layout_tab.addWidget(self.btn_2, 1, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.tab)
        self.btn_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ic_image_folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_3.setIcon(icon2)
        self.btn_3.setObjectName("btn_3")
        self.layout_tab.addWidget(self.btn_3, 2, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.tab)
        self.btn_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ic_json.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_4.setIcon(icon3)
        self.btn_4.setObjectName("btn_4")
        self.layout_tab.addWidget(self.btn_4, 3, 0, 1, 1)
        self.label_empty_inf = QtWidgets.QLabel(self.tab)
        self.label_empty_inf.setObjectName("label_empty_inf")
        self.layout_tab.addWidget(self.label_empty_inf, 4, 0, 1, 1)
        self.layout_tab.setRowStretch(0, 1)
        self.layout_tab.setRowStretch(1, 1)
        self.layout_tab.setRowStretch(2, 1)
        self.layout_tab.setRowStretch(3, 1)
        self.layout_tab.setRowStretch(4, 1)
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
        self.btn_1.setText(_translate("MainWindow", "btn_1"))
        self.btn_2.setText(_translate("MainWindow", "btn_2"))
        self.btn_3.setText(_translate("MainWindow", "btn_3"))
        self.btn_4.setText(_translate("MainWindow", "btn_4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "INFERENCE"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "GOLDEN"))
