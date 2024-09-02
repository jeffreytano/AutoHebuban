# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIprototype.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(199, 217)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Target = QComboBox(self.tab)
        self.Target.addItem("")
        self.Target.addItem("")
        self.Target.setObjectName(u"Target")

        self.horizontalLayout.addWidget(self.Target)

        self.Color = QComboBox(self.tab)
        self.Color.addItem("")
        self.Color.addItem("")
        self.Color.addItem("")
        self.Color.addItem("")
        self.Color.addItem("")
        self.Color.setObjectName(u"Color")

        self.horizontalLayout.addWidget(self.Color)

        self.Level = QComboBox(self.tab)
        self.Level.addItem("")
        self.Level.addItem("")
        self.Level.addItem("")
        self.Level.addItem("")
        self.Level.addItem("")
        self.Level.setObjectName(u"Level")

        self.horizontalLayout.addWidget(self.Level)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LaunchAppCheckBox = QCheckBox(self.tab)
        self.LaunchAppCheckBox.setObjectName(u"LaunchAppCheckBox")

        self.verticalLayout.addWidget(self.LaunchAppCheckBox)

        self.AutoTrainCheckBox = QCheckBox(self.tab)
        self.AutoTrainCheckBox.setObjectName(u"AutoTrainCheckBox")

        self.verticalLayout.addWidget(self.AutoTrainCheckBox)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")

        self.verticalLayout_2.addWidget(self.StartButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 199, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Target.setItemText(0, QCoreApplication.translate("MainWindow", u"Orb", None))
        self.Target.setItemText(1, QCoreApplication.translate("MainWindow", u"Jewel", None))

        self.Color.setItemText(0, QCoreApplication.translate("MainWindow", u"R", None))
        self.Color.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.Color.setItemText(2, QCoreApplication.translate("MainWindow", u"Y", None))
        self.Color.setItemText(3, QCoreApplication.translate("MainWindow", u"W", None))
        self.Color.setItemText(4, QCoreApplication.translate("MainWindow", u"P", None))

        self.Level.setItemText(0, QCoreApplication.translate("MainWindow", u"12", None))
        self.Level.setItemText(1, QCoreApplication.translate("MainWindow", u"13", None))
        self.Level.setItemText(2, QCoreApplication.translate("MainWindow", u"14", None))
        self.Level.setItemText(3, QCoreApplication.translate("MainWindow", u"15", None))
        self.Level.setItemText(4, QCoreApplication.translate("MainWindow", u"16", None))

        self.LaunchAppCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30d7\u30ea\u8d77\u52d5", None))
        self.AutoTrainCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u6642\u306e\u4fee\u7df4\u5834", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

