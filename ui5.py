# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIprototype5.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pynput import keyboard
from multiprocessing import Process, Event
import threading

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

import autohvbnImporter 
# import autoHvbn, battleOnly, enterBattleHandler

class Ui_MainWindow(object):

    process = Process()
    process_finished = Event()
    terminated = False

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(561, 505)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabGroup = QTabWidget(self.centralwidget)
        self.tabGroup.setObjectName(u"tabGroup")
        self.tabGroup.setEnabled(True)
        self.tabGroup.setGeometry(QRect(9, 9, 543, 381))
        font = QFont()
        font.setFamilies([u"\u6e38\u30b4\u30b7\u30c3\u30af"])
        self.tabGroup.setFont(font)
        self.Task = QWidget()
        self.Task.setObjectName(u"Task")
        self.verticalLayout_3 = QVBoxLayout(self.Task)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.taskGroup = QGroupBox(self.Task)
        self.taskGroup.setObjectName(u"taskGroup")
        self.taskGroup.setMinimumSize(QSize(519, 270))
        self.taskGroup.setFont(font)
        self.RadioButtons = QGroupBox(self.taskGroup)
        self.RadioButtons.setObjectName(u"RadioButtons")
        self.RadioButtons.setGeometry(QRect(310, 70, 181, 161))
        self.RadioButtons.setFont(font)
        self.layoutWidget = QWidget(self.RadioButtons)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 21, 145, 126))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tokiAuto = QRadioButton(self.layoutWidget)
        self.tokiAuto.setObjectName(u"tokiAuto")
        self.tokiAuto.setFont(font)
        self.tokiAuto.setChecked(True)

        self.verticalLayout.addWidget(self.tokiAuto)

        self.arenaAuto = QRadioButton(self.layoutWidget)
        self.arenaAuto.setObjectName(u"arenaAuto")
        self.arenaAuto.setFont(font)

        self.verticalLayout.addWidget(self.arenaAuto)

        self.doNoAuto = QRadioButton(self.layoutWidget)
        self.doNoAuto.setObjectName(u"doNoAuto")
        self.doNoAuto.setFont(font)

        self.verticalLayout.addWidget(self.doNoAuto)

        self.Weekly = QCheckBox(self.layoutWidget)
        self.Weekly.setObjectName(u"Weekly")
        self.Weekly.setFont(font)
        self.Weekly.setChecked(True)

        self.verticalLayout.addWidget(self.Weekly)

        self.Daily = QCheckBox(self.layoutWidget)
        self.Daily.setObjectName(u"Daily")
        self.Daily.setFont(font)
        self.Daily.setChecked(True)

        self.verticalLayout.addWidget(self.Daily)

        self.Sweep = QCheckBox(self.taskGroup)
        self.Sweep.setObjectName(u"Sweep")
        self.Sweep.setGeometry(QRect(20, 80, 47, 20))
        self.Sweep.setFont(font)
        self.Sweep.setChecked(True)
        self.layoutWidget1 = QWidget(self.taskGroup)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 110, 271, 206))
        self.layoutWidget1.setFont(font)
        self.SweepOptionLayout = QVBoxLayout(self.layoutWidget1)
        self.SweepOptionLayout.setObjectName(u"SweepOptionLayout")
        self.SweepOptionLayout.setContentsMargins(0, 0, 0, 0)
        self.targetLayout = QHBoxLayout()
        self.targetLayout.setObjectName(u"targetLayout")
        self.target = QLabel(self.layoutWidget1)
        self.target.setObjectName(u"target")
        self.target.setMinimumSize(QSize(60, 0))
        self.target.setFont(font)

        self.targetLayout.addWidget(self.target)

        self.targetComboBox = QComboBox(self.layoutWidget1)
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.addItem("")
        self.targetComboBox.setObjectName(u"targetComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetComboBox.sizePolicy().hasHeightForWidth())
        self.targetComboBox.setSizePolicy(sizePolicy)
        self.targetComboBox.setMinimumSize(QSize(205, 0))
        self.targetComboBox.setFont(font)

        self.targetLayout.addWidget(self.targetComboBox)


        self.SweepOptionLayout.addLayout(self.targetLayout)

        self.levelLayout = QHBoxLayout()
        self.levelLayout.setObjectName(u"levelLayout")
        self.levelLabel = QLabel(self.layoutWidget1)
        self.levelLabel.setObjectName(u"levelLabel")
        self.levelLabel.setMinimumSize(QSize(60, 0))
        self.levelLabel.setFont(font)

        self.levelLayout.addWidget(self.levelLabel)

        self.levelComboBox = QComboBox(self.layoutWidget1)
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.setObjectName(u"levelComboBox")
        sizePolicy.setHeightForWidth(self.levelComboBox.sizePolicy().hasHeightForWidth())
        self.levelComboBox.setSizePolicy(sizePolicy)
        self.levelComboBox.setMinimumSize(QSize(205, 0))
        self.levelComboBox.setFont(font)

        self.levelLayout.addWidget(self.levelComboBox)


        self.SweepOptionLayout.addLayout(self.levelLayout)

        self.sweepTimeLayout = QHBoxLayout()
        self.sweepTimeLayout.setObjectName(u"sweepTimeLayout")
        self.sweepTime = QLabel(self.layoutWidget1)
        self.sweepTime.setObjectName(u"sweepTime")
        self.sweepTime.setFont(font)

        self.sweepTimeLayout.addWidget(self.sweepTime)

        self.sweepTimeComboBox = QComboBox(self.layoutWidget1)
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.addItem("")
        self.sweepTimeComboBox.setObjectName(u"sweepTimeComboBox")
        sizePolicy.setHeightForWidth(self.sweepTimeComboBox.sizePolicy().hasHeightForWidth())
        self.sweepTimeComboBox.setSizePolicy(sizePolicy)
        self.sweepTimeComboBox.setMinimumSize(QSize(205, 0))
        self.sweepTimeComboBox.setFont(font)

        self.sweepTimeLayout.addWidget(self.sweepTimeComboBox)


        self.SweepOptionLayout.addLayout(self.sweepTimeLayout)

        self.teamLayout = QHBoxLayout()
        self.teamLayout.setObjectName(u"teamLayout")
        self.teamLabel = QLabel(self.layoutWidget1)
        self.teamLabel.setObjectName(u"teamLabel")
        self.teamLabel.setFont(font)

        self.teamLayout.addWidget(self.teamLabel)

        self.teamSelect = QComboBox(self.layoutWidget1)
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.addItem("")
        self.teamSelect.setObjectName(u"teamSelect")
        sizePolicy.setHeightForWidth(self.teamSelect.sizePolicy().hasHeightForWidth())
        self.teamSelect.setSizePolicy(sizePolicy)
        self.teamSelect.setMinimumSize(QSize(92, 0))
        self.teamSelect.setFont(font)

        self.teamLayout.addWidget(self.teamSelect)

        self.formerTeam = QCheckBox(self.layoutWidget1)
        self.formerTeam.setObjectName(u"formerTeam")
        self.formerTeam.setMinimumSize(QSize(0, 0))
        self.formerTeam.setFont(font)

        self.teamLayout.addWidget(self.formerTeam)


        self.SweepOptionLayout.addLayout(self.teamLayout)

        self.battleLayout = QHBoxLayout()
        self.battleLayout.setObjectName(u"battleLayout")
        self.battleScript = QLabel(self.layoutWidget1)
        self.battleScript.setObjectName(u"battleScript")
        self.battleScript.setFont(font)

        self.battleLayout.addWidget(self.battleScript)

        self.battleInstruction = QComboBox(self.layoutWidget1)
        self.battleInstruction.addItem("")
        self.battleInstruction.setObjectName(u"battleInstruction")
        sizePolicy.setHeightForWidth(self.battleInstruction.sizePolicy().hasHeightForWidth())
        self.battleInstruction.setSizePolicy(sizePolicy)
        self.battleInstruction.setMinimumSize(QSize(205, 0))
        self.battleInstruction.setFont(font)

        self.battleLayout.addWidget(self.battleInstruction)


        self.SweepOptionLayout.addLayout(self.battleLayout)

        self.resourceLayout = QHBoxLayout()
        self.resourceLayout.setObjectName(u"resourceLayout")
        self.resourceLabel = QLabel(self.layoutWidget1)
        self.resourceLabel.setObjectName(u"resourceLabel")
        self.resourceLabel.setFont(font)

        self.resourceLayout.addWidget(self.resourceLabel)

        self.resourceComboBox = QComboBox(self.layoutWidget1)
        self.resourceComboBox.addItem("")
        self.resourceComboBox.addItem("")
        self.resourceComboBox.setObjectName(u"resourceComboBox")
        sizePolicy.setHeightForWidth(self.resourceComboBox.sizePolicy().hasHeightForWidth())
        self.resourceComboBox.setSizePolicy(sizePolicy)
        self.resourceComboBox.setMinimumSize(QSize(205, 0))
        self.resourceComboBox.setFont(font)

        self.resourceLayout.addWidget(self.resourceComboBox)


        self.SweepOptionLayout.addLayout(self.resourceLayout)

        self.refillLayout = QHBoxLayout()
        self.refillLayout.setObjectName(u"refillLayout")
        self.refillLabel = QLabel(self.layoutWidget1)
        self.refillLabel.setObjectName(u"refillLabel")
        self.refillLabel.setFont(font)

        self.refillLayout.addWidget(self.refillLabel)

        self.refillComboBox = QComboBox(self.layoutWidget1)
        self.refillComboBox.addItem("")
        self.refillComboBox.addItem("")
        self.refillComboBox.addItem("")
        self.refillComboBox.setObjectName(u"refillComboBox")
        sizePolicy.setHeightForWidth(self.refillComboBox.sizePolicy().hasHeightForWidth())
        self.refillComboBox.setSizePolicy(sizePolicy)
        self.refillComboBox.setMinimumSize(QSize(205, 0))
        self.refillComboBox.setFont(font)

        self.refillLayout.addWidget(self.refillComboBox)


        self.SweepOptionLayout.addLayout(self.refillLayout)

        self.widget = QWidget(self.taskGroup)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 448, 22))
        self.startCheckBoxLayout = QHBoxLayout(self.widget)
        self.startCheckBoxLayout.setObjectName(u"startCheckBoxLayout")
        self.startCheckBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.Login = QCheckBox(self.widget)
        self.Login.setObjectName(u"Login")
        self.Login.setFont(font)

        self.startCheckBoxLayout.addWidget(self.Login)

        # self.LaunchApp = QCheckBox(self.widget)
        # self.LaunchApp.setObjectName(u"LaunchApp")
        # self.LaunchApp.setEnabled(True)
        # self.LaunchApp.setFont(font)
        # self.LaunchApp.setChecked(True)

        # self.startCheckBoxLayout.addWidget(self.LaunchApp)

        self.SkipTrailer = QCheckBox(self.widget)
        self.SkipTrailer.setObjectName(u"SkipTrailer")
        self.SkipTrailer.setFont(font)
        self.SkipTrailer.setChecked(False)

        self.startCheckBoxLayout.addWidget(self.SkipTrailer)

        self.notSkipGacha = QCheckBox(self.widget)
        self.notSkipGacha.setObjectName(u"notSkipGacha")
        self.notSkipGacha.setFont(font)

        self.startCheckBoxLayout.addWidget(self.notSkipGacha)

        self.layoutWidget2 = QWidget(self.taskGroup)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 50, 113, 24))
        self.loginAccountLayout = QHBoxLayout(self.layoutWidget2)
        self.loginAccountLayout.setObjectName(u"loginAccountLayout")
        self.loginAccountLayout.setContentsMargins(0, 0, 0, 0)
        self.loginLabel = QLabel(self.layoutWidget2)
        self.loginLabel.setObjectName(u"loginLabel")

        self.loginAccountLayout.addWidget(self.loginLabel)

        self.loginComboBox = QComboBox(self.layoutWidget2)
        self.loginComboBox.setObjectName(u"loginComboBox")

        self.loginAccountLayout.addWidget(self.loginComboBox)

        self.verticalLayout_3.addWidget(self.taskGroup)

        self.tabGroup.addTab(self.Task, "")
        self.Battle = QWidget()
        self.Battle.setObjectName(u"Battle")
        self.instructionEdit = QPlainTextEdit(self.Battle)
        self.instructionEdit.setObjectName(u"instructionEdit")
        self.instructionEdit.setGeometry(QRect(20, 50, 471, 211))
        self.layoutWidget3 = QWidget(self.Battle)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 310, 258, 26))
        self.bunchanLayout = QHBoxLayout(self.layoutWidget3)
        self.bunchanLayout.setObjectName(u"bunchanLayout")
        self.bunchanLayout.setContentsMargins(0, 0, 0, 0)
        self.bunchanLabel = QLabel(self.layoutWidget3)
        self.bunchanLabel.setObjectName(u"bunchanLabel")

        self.bunchanLayout.addWidget(self.bunchanLabel)

        self.bunchanInput = QSpinBox(self.layoutWidget3)
        self.bunchanInput.setObjectName(u"bunchanInput")
        self.bunchanInput.setMaximum(1000)
        self.bunchanInput.setValue(121)

        self.bunchanLayout.addWidget(self.bunchanInput)

        self.bunchanButton = QPushButton(self.layoutWidget3)
        self.bunchanButton.setObjectName(u"bunchanButton")

        self.bunchanLayout.addWidget(self.bunchanButton)

        self.layoutWidget4 = QWidget(self.Battle)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 20, 471, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setSpacing(148)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fileName = QLineEdit(self.layoutWidget4)
        self.fileName.setObjectName(u"fileName")

        self.horizontalLayout.addWidget(self.fileName)

        self.fileComboBox = QComboBox(self.layoutWidget4)
        self.fileComboBox.setObjectName(u"fileComboBox")
        self.fileComboBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.fileComboBox)

        self.layoutWidget5 = QWidget(self.Battle)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 270, 471, 26))
        self.saveInfoLayout = QHBoxLayout(self.layoutWidget5)
        self.saveInfoLayout.setSpacing(250)
        self.saveInfoLayout.setObjectName(u"saveInfoLayout")
        self.saveInfoLayout.setContentsMargins(0, 0, 0, 0)
        self.saveButton = QPushButton(self.layoutWidget5)
        self.saveButton.setObjectName(u"saveButton")

        self.saveInfoLayout.addWidget(self.saveButton)

        self.infoButton = QPushButton(self.layoutWidget5)
        self.infoButton.setObjectName(u"infoButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.infoButton.sizePolicy().hasHeightForWidth())
        self.infoButton.setSizePolicy(sizePolicy1)
        self.infoButton.setMinimumSize(QSize(3, 0))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.infoButton.setIcon(icon)

        self.saveInfoLayout.addWidget(self.infoButton)

        self.tabGroup.addTab(self.Battle, "")
        self.layoutWidget6 = QWidget(self.centralwidget)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(20, 400, 400, 60))
        self.GreatButtonGroup = QVBoxLayout(self.layoutWidget6)
        self.GreatButtonGroup.setObjectName(u"GreatButtonGroup")
        self.GreatButtonGroup.setContentsMargins(0, 0, 0, 0)
        self.ButtonGroup1 = QHBoxLayout()
        self.ButtonGroup1.setObjectName(u"ButtonGroup1")
        self.AllButton = QPushButton(self.layoutWidget6)
        self.AllButton.setObjectName(u"AllButton")
        self.AllButton.setMinimumSize(QSize(128, 0))
        self.AllButton.setFont(font)

        self.ButtonGroup1.addWidget(self.AllButton)

        self.SweepCloseButton = QPushButton(self.layoutWidget6)
        self.SweepCloseButton.setObjectName(u"SweepCloseButton")
        self.SweepCloseButton.setMinimumSize(QSize(128, 0))
        self.SweepCloseButton.setFont(font)

        self.ButtonGroup1.addWidget(self.SweepCloseButton)

        self.onlyCloseButton = QPushButton(self.layoutWidget6)
        self.onlyCloseButton.setObjectName(u"onlyCloseButton")
        self.onlyCloseButton.setMinimumSize(QSize(128, 0))
        self.onlyCloseButton.setFont(font)
        self.onlyCloseButton.clicked.connect(self.onlyClose)

        self.ButtonGroup1.addWidget(self.onlyCloseButton)

        self.GreatButtonGroup.addLayout(self.ButtonGroup1)

        self.ButtonGroup2 = QHBoxLayout()
        self.ButtonGroup2.setObjectName(u"ButtonGroup2")
        self.StartButton = QPushButton(self.layoutWidget6)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setMinimumSize(QSize(128, 0))
        self.StartButton.setFont(font)

        self.ButtonGroup2.addWidget(self.StartButton)

        self.onlyBattleButton = QPushButton(self.layoutWidget6)
        self.onlyBattleButton.setObjectName(u"onlyBattleButton")
        self.onlyBattleButton.setMinimumSize(QSize(128, 0))
        self.onlyBattleButton.setFont(font)
        self.onlyBattleButton.clicked.connect(self.onlyBattleWithMonitor)

        self.ButtonGroup2.addWidget(self.onlyBattleButton)

        self.SweepButton = QPushButton(self.layoutWidget6)
        self.SweepButton.setObjectName(u"SweepButton")
        self.SweepButton.setFont(font)

        self.ButtonGroup2.addWidget(self.SweepButton)

        self.GreatButtonGroup.addLayout(self.ButtonGroup2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 561, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabGroup.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.levelComboBox.setMaxVisibleItems(6)
        self.StartButton.clicked.connect(self.startSequence)
        self.SweepButton.clicked.connect(self.onlySweep) # manually added
        self.targetComboBox.currentIndexChanged.connect(self.onTargetChange)
        self.AllButton.clicked.connect(self.fullSequence)
        self.SweepCloseButton.clicked.connect(self.sweepClose)

        self.loginComboBox.setEnabled(False)
        self.Login.setEnabled(False) # added manually
        self.SkipTrailer.setEnabled(False) # added manually
        self.notSkipGacha.setEnabled(False) # added manually

        self.tokiAuto.setChecked(True)  # added manually
        # self.LaunchApp.setChecked(True) # added manually
        self.formerTeam.setChecked(True)
        self.Daily.setChecked(True) # added manually
        self.Weekly.setChecked(True) # added manually
        self.Sweep.setChecked(True) # added manually
        self.targetComboBox.setCurrentIndex(9)
        self.levelComboBox.setCurrentIndex(3)
        self.loadBattleInstruction()

        self.loadPreset()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.taskGroup.setTitle(QCoreApplication.translate("MainWindow", u"\u30db\u30fc\u30e0\u753b\u9762", None))
        self.RadioButtons.setTitle(QCoreApplication.translate("MainWindow", u"\u9589\u3058\u308b\u524d", None))
        self.tokiAuto.setText(QCoreApplication.translate("MainWindow", u"\u6642\u306e\u4fee\u7df4\u5834", None))
        self.arenaAuto.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30ea\u30fc\u30ca", None))
        self.doNoAuto.setText(QCoreApplication.translate("MainWindow", u"\u4f55\u3082\u3057\u306a\u3044", None))
        self.Weekly.setText(QCoreApplication.translate("MainWindow", u"\u30a6\u30a3\u30fc\u30af\u30ea\u30fc\u53d7\u3051\u53d6\u308a", None))
        self.Daily.setText(QCoreApplication.translate("MainWindow", u"\u30c7\u30a4\u30ea\u30fc\u53d7\u3051\u53d6\u308a", None))
        self.Sweep.setText(QCoreApplication.translate("MainWindow", u"\u5468\u56de", None))
        self.target.setText(QCoreApplication.translate("MainWindow", u"\u5468\u56de\u76f8\u624b", None))
        self.targetComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u30d9\u30eb\u30af\u30ce\u30c3\u30ab\u30fc", None))
        self.targetComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u30d8\u30a4\u30eb\u30db\u30fc\u30b9", None))
        self.targetComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u30d1\u30a4\u30eb\u30b4\u30fc\u30ec\u30e0T", None))
        self.targetComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u30b7\u30a7\u30eb\u30d7\u30ed\u30c6\u30af\u30b7\u30aa\u30f3", None))
        self.targetComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u30f4\u30a7\u30a4\u30eb\u30c9\u30c7\u30b9O", None))
        self.targetComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u30a2\u30e9\u30af\u30cd\u30e9\u30a4\u30f3A", None))
        self.targetComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u30a8\u30b0\u30be\u30f4\u30a9\u30c3\u30c1\u30e3\u30fcR", None))
        self.targetComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u30a8\u30b0\u30be\u30f4\u30a9\u30c3\u30c1\u30e3\u30fcB", None))
        self.targetComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u30a8\u30b0\u30be\u30f4\u30a9\u30c3\u30c1\u30e3\u30fcY", None))
        self.targetComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\u30a8\u30b0\u30be\u30f4\u30a9\u30c3\u30c1\u30e3\u30fcW", None))
        self.targetComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"\u30a8\u30b0\u30be\u30f4\u30a9\u30c3\u30c1\u30e3\u30fcP", None))
        self.targetComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"\u30b7\u30cb\u30b9\u30bf\u30fc\uff06\u30ec\u30af\u30bf\u30b9\u30fb\u30cb\u30fc\u30ebR", None))
        self.targetComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"\u30b7\u30cb\u30b9\u30bf\u30fc\uff06\u30ec\u30af\u30bf\u30b9\u30fb\u30cb\u30fc\u30ebB", None))
        self.targetComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"\u30b7\u30cb\u30b9\u30bf\u30fc\uff06\u30ec\u30af\u30bf\u30b9\u30fb\u30cb\u30fc\u30ebY", None))
        self.targetComboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"\u30b7\u30cb\u30b9\u30bf\u30fc\uff06\u30ec\u30af\u30bf\u30b9\u30fb\u30cb\u30fc\u30ebW", None))
        self.targetComboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"\u30b7\u30cb\u30b9\u30bf\u30fc\uff06\u30ec\u30af\u30bf\u30b9\u30fb\u30cb\u30fc\u30ebP", None))
        self.targetComboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"\u30a2\u30e2\u30f3Y", None))
        self.targetComboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"\u30a2\u30e2\u30f3B", None))
        self.targetComboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"\u30a2\u30e2\u30f3W", None))
        self.targetComboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"\u30a2\u30e2\u30f3P", None))
        self.targetComboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"\u30a2\u30e2\u30f3R", None))

        self.levelLabel.setText(QCoreApplication.translate("MainWindow", u"\u30ec\u30d9\u30eb", None))
        self.levelComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Lv8", None))
        self.levelComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Lv9", None))
        self.levelComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Lv10", None))
        self.levelComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Lv11", None))
        self.levelComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Lv12", None))
        self.levelComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Lv13", None))

        self.sweepTime.setText(QCoreApplication.translate("MainWindow", u"\u56de\u6570", None))
        # self.sweepTimeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u3042\u308b\u3060\u3051", None))
        self.sweepTimeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.sweepTimeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.sweepTimeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.sweepTimeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.sweepTimeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.sweepTimeComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.sweepTimeComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"10", None))
        self.sweepTimeComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"15", None))
        self.sweepTimeComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"20", None))
        self.sweepTimeComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"25", None))
        self.sweepTimeComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"30", None))
        self.sweepTimeComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"35", None))
        self.sweepTimeComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"40", None))
        self.sweepTimeComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"45", None))
        self.sweepTimeComboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"50", None))
        self.sweepTimeComboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"55", None))
        self.sweepTimeComboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"60", None))

        self.teamLabel.setText(QCoreApplication.translate("MainWindow", u"\u30c1\u30fc\u30e0\u6307\u5b9a", None))
        self.teamSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.teamSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.teamSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.teamSelect.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.teamSelect.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.teamSelect.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.teamSelect.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.teamSelect.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.teamSelect.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.teamSelect.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.teamSelect.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.teamSelect.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.teamSelect.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.teamSelect.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.teamSelect.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.teamSelect.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.teamSelect.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.teamSelect.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.teamSelect.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.teamSelect.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.formerTeam.setText(QCoreApplication.translate("MainWindow", u"\u524d\u56de\u30af\u30ea\u30a2\u90e8\u968a", None))
        self.battleScript.setText(QCoreApplication.translate("MainWindow", u"\u6226\u95d8\u6307\u793a", None))
        self.battleInstruction.setItemText(0, QCoreApplication.translate("MainWindow", u"Auto", None))

        self.resourceLabel.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u3046\u8cc7\u6e90", None))
        self.resourceComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u30e9\u30a4\u30d5", None))
        self.resourceComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u30c1\u30b1\u30c3\u30c8", None))

        self.refillLabel.setText(QCoreApplication.translate("MainWindow", u"\u30e9\u30a4\u30d5\u88dc\u586b", None))
        self.refillComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u30e9\u30a4\u30d5\u30b9\u30c8\u30f3", None))
        self.refillComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e88\u5099\u30e9\u30a4\u30d5", None))
        self.refillComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u30af\u30a9\u30fc\u30c4", None))

        self.Login.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30ab\u30a6\u30f3\u30c8\u7d99\u627f", None))
        # self.LaunchApp.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30d7\u30ea\u8d77\u52d5", None))
        self.SkipTrailer.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u30b9\u30bf\u30a4\u30eb\u30b9\u30ad\u30c3\u30d7", None))
        self.notSkipGacha.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u65e5\u4e00\u56de\u30ac\u30c1\u30e3", None))
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"\u7d99\u627f\u5148", None))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.Task), QCoreApplication.translate("MainWindow", u"\u4f5c\u696d", None))
        self.instructionEdit.setPlainText(QCoreApplication.translate("MainWindow", u"T1 C1S1 TE\n"
"T2 C1C4 C1S4 TE\n"
"BE", None))
        self.bunchanLabel.setText(QCoreApplication.translate("MainWindow", u"\u8c4a\u5f8c\u5c02\u7528\u30a2\u30ea\u30fc\u30ca\u5468\u56de", None))
        self.bunchanButton.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
        self.fileName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb\u540d", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8aac\u660e\u66f8", None))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.Battle), QCoreApplication.translate("MainWindow", u"\u6226\u95d8\u6307\u793a", None))
        self.AllButton.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u52d5\uff0b\u5468\u56de\uff0b\u9589\u3058\u308b", None))
        self.SweepCloseButton.setText(QCoreApplication.translate("MainWindow", u"\u5468\u56de\uff0b\u9589\u3058\u308b", None))
        self.onlyCloseButton.setText(QCoreApplication.translate("MainWindow", u"\u9589\u3058\u308b\u3060\u3051", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u52d5\u3060\u3051", None))
        self.onlyBattleButton.setText(QCoreApplication.translate("MainWindow", u"\u6226\u95d8\u3060\u3051", None))
        self.SweepButton.setText(QCoreApplication.translate("MainWindow", u"\u5468\u56de\u3060\u3051", None))
    # retranslateUi

# manually added

    def loadPreset(self):
        try:
            file = open('Preset.txt','r+')

            # self.Login.setChecked(True)
            # self.tokiAuto.setChecked(True)
            # self.SkipTrailer.setChecked(True)
            # self.notSkipGacha.setChecked(True)
            # self.Sweep.setChecked(True)
            # self.targetComboBox.setCurrentIndex(1)
            # self.levelComboBox.setCurrentIndex(1)
            # self.sweepTimeComboBox.setCurrentIndex(1)
            # self.battleInstruction.setCurrentIndex(1)
            # self.Daily.setChecked(True)
            # self.Weekly.setChecked(True)
            # self.tokiAuto.setChecked(True)

        except FileNotFoundError:
            print("Preset not found.")

    def loadBattleInstruction(self):
        preset = []
        file = open('index.txt','r')
        for line in file.readlines():
            preset.append(line)
            self.battleInstruction.addItem(line)
        file.close()

    def onTargetChange(self,index):
        match index:
            case index if 0<= index < 5:
                self.levelComboBox.setMaxCount(6)
                self.levelComboBox.setMaxVisibleItems(6)
                self.levelComboBox.setItemText(0,'Lv8')
                self.levelComboBox.setItemText(1,'Lv9')
                self.levelComboBox.setItemText(2,'Lv10')
                self.levelComboBox.setItemText(3,'Lv11')
                self.levelComboBox.addItem('Lv12')
                self.levelComboBox.addItem('Lv13')
            case 5:
                self.levelComboBox.setMaxCount(4)
                self.levelComboBox.setItemText(0,'Lv13')
                self.levelComboBox.setItemText(1,'Lv14')
                self.levelComboBox.setItemText(2,'Lv15')
                self.levelComboBox.setItemText(3,'Lv16')
                if self.levelComboBox.currentIndex()>3:
                    self.levelComboBox.setCurrentIndex(3)
                # self.levelComboBox.removeItem(4)
                # self.levelComboBox.removeItem(5)
            case index if 6<= index < 21:
                self.levelComboBox.setMaxCount(4)
                self.levelComboBox.setMaxVisibleItems(4)
                self.levelComboBox.setItemText(0,'Lv1')
                self.levelComboBox.setItemText(1,'Lv2')
                self.levelComboBox.setItemText(2,'Lv3')
                self.levelComboBox.setItemText(3,'Lv4')
                if self.levelComboBox.currentIndex()>3:
                    self.levelComboBox.setCurrentIndex(3)
                # self.levelComboBox.removeItem(4)
                # self.levelComboBox.removeItem(5)

    # def fullSequence(self):
    #     self.process = Process(target=self.fullSequence)
    #     self.process.start()
    #     self.monitor_key_press()
    #     self.process.join()
    
    def fullSequence(self):
        print('full sequence')
        self.startSequence()
        self.process_finished.wait()
        if not self.terminated:
            self.onlySweep()
        self.process_finished.wait()
        if not self.terminated:
            self.onlyClose()

    # def sweepClose(self):
    #     self.process = Process(target=self.sweepClose)
    #     self.process.start()
    #     self.monitor_key_press()
    #     self.process.join()

    def sweepClose(self):
        print('sweepClose')
        # self.callFunctionWithMonitor(self.onlySweep,[])
        # self.callFunctionWithMonitor(self.onlyClose,[])
        self.onlySweep()
        self.process_finished.wait()
        if not self.terminated:
            self.onlyClose()
    
    def startSequence(self):
        # autoHvbn.launchApplication(self.notSkipGacha.isChecked())
        # self.process = Process(target=self.startSequence)
        self.callFunctionWithMonitor(autohvbnImporter.launchApplication,[self.notSkipGacha.isChecked()])
        # self.process = Process(target=autohvbnImporter.launchApplication,args=(self.notSkipGacha.isChecked(),))
        # self.process.start()
        # self.monitor_key_press()
        # self.process.join()

    def onlyBattleWithMonitor(self):
        # autoHvbn.battleOnly(self,self.battleInstruction.currentText())
        self.process = Process(target=autohvbnImporter.battleOnly,args=(self.battleInstruction.currentText(),))
        self.process.start()
        self.monitor_key_press()
        self.process.join()

    def onlyClose(self):
        params = [self.Daily.isChecked(),self.Weekly.isChecked(),self.tokiAuto.isChecked()]
        self.callFunctionWithMonitor(autohvbnImporter.closeProcess,params)

    def onlySweep(self):
        battleParam = [ self.targetComboBox.currentIndex(),
                        self.levelComboBox.currentIndex(),
                        self.sweepTimeComboBox.currentText(),
                        self.teamSelect.currentIndex(),
                        self.formerTeam.isChecked(),
                        self.resourceComboBox.currentIndex(),
                        self.battleInstruction.currentText(),
                        self.refillComboBox.currentIndex()
                        ]
        self.callFunctionWithMonitor(autohvbnImporter.enterBattleHandler,battleParam)
        # self.process = Process(target=autohvbnImporter.enterBattleHandler,args=(*battleParam,))
        # self.process.start()
        # self.monitor_key_press()
        # self.process.join()
        

    def on_press(self,key):
        try:
            if key == keyboard.Key.esc:
                print('terminated')
                if listener:
                    listener.stop()
                self.process.terminate()
                self.terminated=True
                return False
        except AttributeError:
            pass

    def monitor_key_press(self):
        global listener
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()

    def callFunctionWithMonitor(self,function,params):
        self.terminated = False
        self.process_finished = Event()
        self.process = Process(target=function,args=(*params,))
        self.process.start()
        threading.Thread(target=self.monitor_key_press, daemon=True).start()
        threading.Thread(target=lambda: self.monitorProcess(self.process), daemon=True).start()

    def monitorProcess(self,process):
        process.join()
        print('process end')
        if listener:
            listener.stop()
            self.process_finished.set()
