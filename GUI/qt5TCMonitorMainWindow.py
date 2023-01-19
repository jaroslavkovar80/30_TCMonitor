# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt5TCMonitorMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1264, 908)
        MainWindow.setMinimumSize(QtCore.QSize(600, 486))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vlayout1Main = QtWidgets.QVBoxLayout()
        self.vlayout1Main.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout1Main.setContentsMargins(5, 5, 5, 5)
        self.vlayout1Main.setSpacing(5)
        self.vlayout1Main.setObjectName("vlayout1Main")
        self.hlayout2Top = QtWidgets.QHBoxLayout()
        self.hlayout2Top.setContentsMargins(5, 5, 5, 5)
        self.hlayout2Top.setSpacing(10)
        self.hlayout2Top.setObjectName("hlayout2Top")
        self.lbTargetHostAddress = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setKerning(True)
        self.lbTargetHostAddress.setFont(font)
        self.lbTargetHostAddress.setObjectName("lbTargetHostAddress")
        self.hlayout2Top.addWidget(self.lbTargetHostAddress)
        self.edTargetHost = QtWidgets.QLineEdit(self.centralwidget)
        self.edTargetHost.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setKerning(True)
        self.edTargetHost.setFont(font)
        self.edTargetHost.setAutoFillBackground(False)
        self.edTargetHost.setMaxLength(15)
        self.edTargetHost.setAlignment(QtCore.Qt.AlignCenter)
        self.edTargetHost.setObjectName("edTargetHost")
        self.hlayout2Top.addWidget(self.edTargetHost)
        self.btnCheckConnection = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setKerning(True)
        self.btnCheckConnection.setFont(font)
        self.btnCheckConnection.setCheckable(False)
        self.btnCheckConnection.setObjectName("btnCheckConnection")
        self.hlayout2Top.addWidget(self.btnCheckConnection)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlayout2Top.addItem(spacerItem)
        self.hlayout2Top.setStretch(1, 1)
        self.vlayout1Main.addLayout(self.hlayout2Top)
        self.hlayout2Bottom = QtWidgets.QHBoxLayout()
        self.hlayout2Bottom.setContentsMargins(0, 0, -1, -1)
        self.hlayout2Bottom.setSpacing(5)
        self.hlayout2Bottom.setObjectName("hlayout2Bottom")
        self.vlayout3Left = QtWidgets.QVBoxLayout()
        self.vlayout3Left.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout3Left.setObjectName("vlayout3Left")
        self.btnTab1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnTab1.setFont(font)
        self.btnTab1.setObjectName("btnTab1")
        self.vlayout3Left.addWidget(self.btnTab1)
        self.btnTab2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnTab2.setFont(font)
        self.btnTab2.setObjectName("btnTab2")
        self.vlayout3Left.addWidget(self.btnTab2)
        self.btnTab3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnTab3.setFont(font)
        self.btnTab3.setObjectName("btnTab3")
        self.vlayout3Left.addWidget(self.btnTab3)
        self.btnTab4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnTab4.setFont(font)
        self.btnTab4.setObjectName("btnTab4")
        self.vlayout3Left.addWidget(self.btnTab4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlayout3Left.addItem(spacerItem1)
        self.hlayout2Bottom.addLayout(self.vlayout3Left)
        self.vlayout3Right = QtWidgets.QVBoxLayout()
        self.vlayout3Right.setObjectName("vlayout3Right")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabMemory = QtWidgets.QWidget()
        self.tabMemory.setObjectName("tabMemory")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabMemory)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnAddRecordToMemoryTable = QtWidgets.QPushButton(self.tabMemory)
        self.btnAddRecordToMemoryTable.setObjectName("btnAddRecordToMemoryTable")
        self.horizontalLayout_3.addWidget(self.btnAddRecordToMemoryTable)
        self.btnDelRecordFromMemoryTable = QtWidgets.QPushButton(self.tabMemory)
        self.btnDelRecordFromMemoryTable.setObjectName("btnDelRecordFromMemoryTable")
        self.horizontalLayout_3.addWidget(self.btnDelRecordFromMemoryTable)
        self.btnClearMemoryTable = QtWidgets.QPushButton(self.tabMemory)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btnClearMemoryTable.setFont(font)
        self.btnClearMemoryTable.setObjectName("btnClearMemoryTable")
        self.horizontalLayout_3.addWidget(self.btnClearMemoryTable)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lbAutomaticlogging = QtWidgets.QLabel(self.tabMemory)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setKerning(True)
        self.lbAutomaticlogging.setFont(font)
        self.lbAutomaticlogging.setObjectName("lbAutomaticlogging")
        self.horizontalLayout_3.addWidget(self.lbAutomaticlogging)
        self.spinBoxLoggingTime = QtWidgets.QSpinBox(self.tabMemory)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxLoggingTime.sizePolicy().hasHeightForWidth())
        self.spinBoxLoggingTime.setSizePolicy(sizePolicy)
        self.spinBoxLoggingTime.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxLoggingTime.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxLoggingTime.setMinimum(1)
        self.spinBoxLoggingTime.setMaximum(120)
        self.spinBoxLoggingTime.setProperty("value", 10)
        self.spinBoxLoggingTime.setObjectName("spinBoxLoggingTime")
        self.horizontalLayout_3.addWidget(self.spinBoxLoggingTime)
        self.btnStartMemoryLogging = QtWidgets.QPushButton(self.tabMemory)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.btnStartMemoryLogging.setFont(font)
        self.btnStartMemoryLogging.setObjectName("btnStartMemoryLogging")
        self.horizontalLayout_3.addWidget(self.btnStartMemoryLogging)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tablewMemoryOverview = QtWidgets.QTableWidget(self.tabMemory)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.tablewMemoryOverview.setFont(font)
        self.tablewMemoryOverview.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tablewMemoryOverview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewMemoryOverview.setAlternatingRowColors(True)
        self.tablewMemoryOverview.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tablewMemoryOverview.setObjectName("tablewMemoryOverview")
        self.tablewMemoryOverview.setColumnCount(10)
        self.tablewMemoryOverview.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tablewMemoryOverview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tablewMemoryOverview.setHorizontalHeaderItem(9, item)
        self.tablewMemoryOverview.horizontalHeader().setVisible(False)
        self.tablewMemoryOverview.horizontalHeader().setDefaultSectionSize(95)
        self.tablewMemoryOverview.horizontalHeader().setHighlightSections(True)
        self.tablewMemoryOverview.horizontalHeader().setMinimumSectionSize(50)
        self.tablewMemoryOverview.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_2.addWidget(self.tablewMemoryOverview)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tabMemory, "")
        self.tabProcesses = QtWidgets.QWidget()
        self.tabProcesses.setObjectName("tabProcesses")
        self.label_2 = QtWidgets.QLabel(self.tabProcesses)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.btnCallCmd = QtWidgets.QPushButton(self.tabProcesses)
        self.btnCallCmd.setGeometry(QtCore.QRect(40, 20, 75, 23))
        self.btnCallCmd.setObjectName("btnCallCmd")
        self.lineEdit = QtWidgets.QLineEdit(self.tabProcesses)
        self.lineEdit.setGeometry(QtCore.QRect(40, 120, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tabProcesses, "")
        self.tabLogger = QtWidgets.QWidget()
        self.tabLogger.setObjectName("tabLogger")
        self.label_3 = QtWidgets.QLabel(self.tabLogger)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tabLogger, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(250, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.vlayout3Right.addWidget(self.tabWidget)
        self.hlayout2Bottom.addLayout(self.vlayout3Right)
        self.hlayout2Bottom.setStretch(0, 1)
        self.hlayout2Bottom.setStretch(1, 10)
        self.vlayout1Main.addLayout(self.hlayout2Bottom)
        self.gridLayout.addLayout(self.vlayout1Main, 0, 0, 1, 1)
        self.lbStatus = QtWidgets.QLabel(self.centralwidget)
        self.lbStatus.setObjectName("lbStatus")
        self.gridLayout.addWidget(self.lbStatus, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1264, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TC - SSH Client"))
        self.lbTargetHostAddress.setText(_translate("MainWindow", "Target IP adress:"))
        self.edTargetHost.setText(_translate("MainWindow", "10.0.0.73"))
        self.btnCheckConnection.setText(_translate("MainWindow", "Check connection"))
        self.btnTab1.setText(_translate("MainWindow", "PushButton"))
        self.btnTab2.setText(_translate("MainWindow", "PushButton"))
        self.btnTab3.setText(_translate("MainWindow", "PushButton"))
        self.btnTab4.setText(_translate("MainWindow", "PushButton"))
        self.btnAddRecordToMemoryTable.setText(_translate("MainWindow", "get"))
        self.btnDelRecordFromMemoryTable.setText(_translate("MainWindow", "remove"))
        self.btnClearMemoryTable.setText(_translate("MainWindow", "clear all"))
        self.lbAutomaticlogging.setText(_translate("MainWindow", "Time [min]"))
        self.btnStartMemoryLogging.setText(_translate("MainWindow", "start logging"))
        self.tablewMemoryOverview.setSortingEnabled(True)
        item = self.tablewMemoryOverview.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "time"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "total"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "used"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "free"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "shared"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "buff/cache"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "availabe"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "swap total"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "swap used"))
        item = self.tablewMemoryOverview.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "swap free"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMemory), _translate("MainWindow", "Tab 1"))
        self.label_2.setText(_translate("MainWindow", "tab2"))
        self.btnCallCmd.setText(_translate("MainWindow", "PushButton"))
        self.lineEdit.setText(_translate("MainWindow", "journalctl"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProcesses), _translate("MainWindow", "Tab 2"))
        self.label_3.setText(_translate("MainWindow", "tab3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLogger), _translate("MainWindow", "Strana"))
        self.label_4.setText(_translate("MainWindow", "tab4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Strana"))
        self.lbStatus.setText(_translate("MainWindow", "status"))
