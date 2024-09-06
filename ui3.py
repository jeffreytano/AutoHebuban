from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from autohvbnImporter import autoHvbn
autohvbn = autoHvbn()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(561, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.taskTab = QTabWidget(self.centralwidget)
        self.taskTab.setObjectName(u"taskTab")
        self.taskTab.setEnabled(True)
        self.Task = QWidget()
        self.Task.setObjectName(u"Task")
        self.verticalLayout_3 = QVBoxLayout(self.Task)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.startGroup = QGroupBox(self.Task)
        self.startGroup.setObjectName(u"startGroup")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startGroup.sizePolicy().hasHeightForWidth())
        self.startGroup.setSizePolicy(sizePolicy)
        self.startGroup.setMinimumSize(QSize(0, 94))
        self.widget = QWidget(self.startGroup)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 481, 48))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.StartLabelTitle = QLabel(self.widget)
        self.StartLabelTitle.setObjectName(u"StartLabelTitle")

        self.horizontalLayout_5.addWidget(self.StartLabelTitle)

        self.StartLabel = QLabel(self.widget)
        self.StartLabel.setObjectName(u"StartLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StartLabel.sizePolicy().hasHeightForWidth())
        self.StartLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.StartLabel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Login = QCheckBox(self.widget)
        self.Login.setObjectName(u"Login")

        self.Login.setEnabled(False) # added manually

        self.horizontalLayout.addWidget(self.Login)

        self.LaunchApp = QCheckBox(self.widget)
        self.LaunchApp.setObjectName(u"LaunchApp")


        self.horizontalLayout.addWidget(self.LaunchApp)

        self.SkipTrailer = QCheckBox(self.widget)
        self.SkipTrailer.setObjectName(u"SkipTrailer")

        self.horizontalLayout.addWidget(self.SkipTrailer)

        self.SkipGacha = QCheckBox(self.widget)
        self.SkipGacha.setObjectName(u"SkipGacha")

        self.horizontalLayout.addWidget(self.SkipGacha)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.startGroup)

        self.taskGroup = QGroupBox(self.Task)
        self.taskGroup.setObjectName(u"taskGroup")
        self.taskGroup.setMinimumSize(QSize(519, 230))
        self.groupBox = QGroupBox(self.taskGroup)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(380, 120, 120, 101))
        self.RadioButtons = QWidget(self.groupBox)
        self.RadioButtons.setObjectName(u"RadioButtons")
        self.RadioButtons.setGeometry(QRect(10, 20, 84, 74))
        self.AutoLayout = QVBoxLayout(self.RadioButtons)
        self.AutoLayout.setObjectName(u"AutoLayout")
        self.AutoLayout.setContentsMargins(0, 0, 0, 0)
        self.tokiAuto = QRadioButton(self.RadioButtons)
        self.tokiAuto.setObjectName(u"tokiAuto")

        self.AutoLayout.addWidget(self.tokiAuto)

        self.arenaAuto = QRadioButton(self.RadioButtons)
        self.arenaAuto.setObjectName(u"arenaAuto")

        self.AutoLayout.addWidget(self.arenaAuto)

        self.doNoAuto = QRadioButton(self.RadioButtons)
        self.doNoAuto.setObjectName(u"doNoAuto")

        self.AutoLayout.addWidget(self.doNoAuto)

        self.widget2 = QWidget(self.taskGroup)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 30, 481, 18))
        self.horizontalLayout_6 = QHBoxLayout(self.widget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.TaskLabelTitle = QLabel(self.widget2)
        self.TaskLabelTitle.setObjectName(u"TaskLabelTitle")

        self.horizontalLayout_6.addWidget(self.TaskLabelTitle)

        self.TaskLabel = QLabel(self.widget2)
        self.TaskLabel.setObjectName(u"TaskLabel")
        sizePolicy1.setHeightForWidth(self.TaskLabel.sizePolicy().hasHeightForWidth())
        self.TaskLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.TaskLabel)

        self.widget3 = QWidget(self.taskGroup)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(20, 60, 271, 142))
        self.verticalLayout = QVBoxLayout(self.widget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Sweep = QCheckBox(self.widget3)
        self.Sweep.setObjectName(u"Sweep")

        self.verticalLayout.addWidget(self.Sweep)

        self.TargetLayout = QHBoxLayout()
        self.TargetLayout.setObjectName(u"TargetLayout")
        self.target = QLabel(self.widget3)
        self.target.setObjectName(u"target")

        self.TargetLayout.addWidget(self.target)

        self.targetComboBox = QComboBox(self.widget3)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.targetComboBox.sizePolicy().hasHeightForWidth())
        self.targetComboBox.setSizePolicy(sizePolicy2)
        self.targetComboBox.setMinimumSize(QSize(200, 0))
        
        self.targetComboBox.setCurrentIndex(5) # added manually

        self.TargetLayout.addWidget(self.targetComboBox)


        self.verticalLayout.addLayout(self.TargetLayout)

        self.LevelLayout = QHBoxLayout()
        self.LevelLayout.setObjectName(u"LevelLayout")
        self.Level = QLabel(self.widget3)
        self.Level.setObjectName(u"Level")

        self.LevelLayout.addWidget(self.Level)

        self.levelComboBox = QComboBox(self.widget3)
        self.levelComboBox.addItem("Lv8")
        self.levelComboBox.addItem("Lv9")
        self.levelComboBox.addItem("Lv10")
        self.levelComboBox.addItem("Lv11")
        self.levelComboBox.addItem("Lv12")
        self.levelComboBox.addItem("Lv13")
        self.levelComboBox.setObjectName(u"levelComboBox")
        sizePolicy2.setHeightForWidth(self.levelComboBox.sizePolicy().hasHeightForWidth())
        self.levelComboBox.setSizePolicy(sizePolicy2)
        self.levelComboBox.setMinimumSize(QSize(200, 0))

        self.LevelLayout.addWidget(self.levelComboBox)


        self.verticalLayout.addLayout(self.LevelLayout)

        self.TimeLayout = QHBoxLayout()
        self.TimeLayout.setObjectName(u"TimeLayout")
        self.sweepTime = QLabel(self.widget3)
        self.sweepTime.setObjectName(u"sweepTime")

        self.TimeLayout.addWidget(self.sweepTime)

        self.sweepTimeComboBox = QComboBox(self.widget3)
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
        sizePolicy2.setHeightForWidth(self.sweepTimeComboBox.sizePolicy().hasHeightForWidth())
        self.sweepTimeComboBox.setSizePolicy(sizePolicy2)
        self.sweepTimeComboBox.setMinimumSize(QSize(200, 0))

        self.TimeLayout.addWidget(self.sweepTimeComboBox)


        self.verticalLayout.addLayout(self.TimeLayout)

        self.BattleLayout = QHBoxLayout()
        self.BattleLayout.setObjectName(u"BattleLayout")
        self.BattleScript = QLabel(self.widget3)
        self.BattleScript.setObjectName(u"BattleScript")

        self.BattleLayout.addWidget(self.BattleScript)

        self.battleInstruction = QComboBox(self.widget3)
        self.battleInstruction.addItem("Auto")
        self.battleInstruction.addItem("Default")
        self.battleInstruction.setObjectName(u"battleInstruction")
        sizePolicy2.setHeightForWidth(self.battleInstruction.sizePolicy().hasHeightForWidth())
        self.battleInstruction.setSizePolicy(sizePolicy2)
        self.battleInstruction.setMinimumSize(QSize(200, 0))

        self.BattleLayout.addWidget(self.battleInstruction)


        self.verticalLayout.addLayout(self.BattleLayout)

        self.widget4 = QWidget(self.taskGroup)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(380, 60, 118, 48))
        self.MissionLayout = QVBoxLayout(self.widget4)
        self.MissionLayout.setObjectName(u"MissionLayout")
        self.MissionLayout.setContentsMargins(0, 0, 0, 0)
        self.Daily = QCheckBox(self.widget4)
        self.Daily.setObjectName(u"Daily")


        self.MissionLayout.addWidget(self.Daily)

        self.Weekly = QCheckBox(self.widget4)
        self.Weekly.setObjectName(u"Weekly")

        self.MissionLayout.addWidget(self.Weekly)


        self.verticalLayout_3.addWidget(self.taskGroup)

        self.taskTab.addTab(self.Task, "")
        self.Battle = QWidget()
        self.Battle.setObjectName(u"Battle")
        self.taskTab.addTab(self.Battle, "")

        self.verticalLayout_2.addWidget(self.taskTab)

        self.ButtonGroup1 = QHBoxLayout()
        self.ButtonGroup1.setObjectName(u"ButtonGroup1")
        self.AllButton = QPushButton(self.centralwidget)
        self.AllButton.setObjectName(u"AllButton")

        self.AllButton.clicked.connect(self.fullSequence)

        self.ButtonGroup1.addWidget(self.AllButton) # manually added

        self.SweepCloseButton = QPushButton(self.centralwidget)
        self.SweepCloseButton.setObjectName(u"SweepCloseButton")

        self.SweepCloseButton.clicked.connect(self.sweepClose)

        self.ButtonGroup1.addWidget(self.SweepCloseButton)

        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.clicked.connect(self.startSequence)

        self.ButtonGroup1.addWidget(self.StartButton)

        self.SweepButton = QPushButton(self.centralwidget)
        self.SweepButton.setObjectName(u"SweepButton")
        self.SweepButton.clicked.connect(self.onlySweep) # manually added

        self.ButtonGroup1.addWidget(self.SweepButton)


        self.verticalLayout_2.addLayout(self.ButtonGroup1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 561, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.taskTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.tokiAuto.setChecked(True)  # added manually
        self.LaunchApp.setChecked(True) # added manually
        self.LaunchApp.setChecked(True) # added manually
        self.Daily.setChecked(True) # added manually
        self.Weekly.setChecked(True) # added manually
        self.Sweep.setChecked(True) # added manually
        self.targetComboBox.setCurrentIndex(9)
        self.levelComboBox.setCurrentIndex(3)

        self.loadPreset()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startGroup.setTitle(QCoreApplication.translate("MainWindow", u"\u30db\u30fc\u30e0\u753b\u9762\u307e\u3067", None))
        self.StartLabelTitle.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u52d5\u30b7\u30fc\u30af\u30a8\u30f3\u30b9:", None))
        self.StartLabel.setText("")
        self.Login.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30ab\u30a6\u30f3\u30c8\u7d99\u627f", None))
        self.LaunchApp.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30d7\u30ea\u8d77\u52d5", None))
        self.SkipTrailer.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u30b9\u30bf\u30a4\u30eb\u30b9\u30ad\u30c3\u30d7", None))
        self.SkipGacha.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u65e5\u4e00\u56de\u30ac\u30c1\u30e3", None))
        self.taskGroup.setTitle(QCoreApplication.translate("MainWindow", u"\u30db\u30fc\u30e0\u753b\u9762\u3042\u3068", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9589\u3058\u308b\u524d", None))
        self.tokiAuto.setText(QCoreApplication.translate("MainWindow", u"\u6642\u306e\u4fee\u7df4\u5834", None))
        self.arenaAuto.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30ea\u30fc\u30ca", None))
        self.doNoAuto.setText(QCoreApplication.translate("MainWindow", u"\u4f55\u3082\u3057\u306a\u3044", None))
        self.TaskLabelTitle.setText(QCoreApplication.translate("MainWindow", u"\u5468\u56de\u30b7\u30fc\u30af\u30a8\u30f3\u30b9:", None))
        self.TaskLabel.setText("")
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
        self.targetComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"\u3042\u3082\u3093Y", None))

        self.Level.setText(QCoreApplication.translate("MainWindow", u"\u30ec\u30d9\u30eb", None))
        self.sweepTime.setText(QCoreApplication.translate("MainWindow", u"\u56de\u6570", None))
        self.sweepTimeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u3042\u308b\u3060\u3051", None))
        self.sweepTimeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.sweepTimeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.sweepTimeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"10", None))
        self.sweepTimeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"15", None))
        self.sweepTimeComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"20", None))
        self.sweepTimeComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"25", None))
        self.sweepTimeComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"30", None))
        self.sweepTimeComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"35", None))
        self.sweepTimeComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"40", None))
        self.sweepTimeComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"45", None))
        self.sweepTimeComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"50", None))
        self.sweepTimeComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"55", None))
        self.sweepTimeComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"60", None))

        self.BattleScript.setText(QCoreApplication.translate("MainWindow", u"\u6226\u95d8\u6307\u793a", None))
        self.Daily.setText(QCoreApplication.translate("MainWindow", u"\u30c7\u30a4\u30ea\u30fc\u53d7\u3051\u53d6\u308a", None))
        self.Weekly.setText(QCoreApplication.translate("MainWindow", u"\u30a6\u30a3\u30fc\u30af\u30ea\u30fc\u53d7\u3051\u53d6\u308a", None))
        self.taskTab.setTabText(self.taskTab.indexOf(self.Task), QCoreApplication.translate("MainWindow", u"\u4f5c\u696d", None))
        self.taskTab.setTabText(self.taskTab.indexOf(self.Battle), QCoreApplication.translate("MainWindow", u"\u6226\u95d8\u6307\u793a", None))
        self.AllButton.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u52d5\u304b\u3089\u9589\u3058\u308b\u307e\u3067", None))
        self.SweepCloseButton.setText(QCoreApplication.translate("MainWindow", u"\u5468\u56de+\u9589\u3058\u308b", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u52d5\u30b7\u30fc\u30af\u30a8\u30f3\u30b9\u3060\u3051", None))
        self.SweepButton.setText(QCoreApplication.translate("MainWindow", u"\u5468\u56de\u3060\u3051", None))
    # retranslateUi

    # manually added

    def loadPreset(self):
        try:
            file = open('Preset.txt','r+')

            # self.Login.setChecked(True)
            # self.tokiAuto.setChecked(True)
            # self.SkipTrailer.setChecked(True)
            # self.SkipGacha.setChecked(True)
            # self.Sweep.setChecked(True)
            # self.targetComboBox.setCurrentIndex(1)
            # self.levelComboBox.setCurrentIndex(1)
            # self.sweepTimeComboBox.setCurrentIndex(1)
            # self.battleInstruction.setCurrentIndex(1)
            # self.Daily.setChecked(True)
            # self.Weekly.setChecked(True)
            # self.tokiAuto.setChecked(True)

        except FileNotFoundError:
            print("File not found. Please check the file path.")

    def fullSequence(self):
        print('full sequence')

    def sweepClose(self):
        print('sweepClose')
    
    def startSequence(self):
        print('startSequence')
        autoHvbn.launchApplication()

    def onlySweep(self):
        print('onlySweep')
        targetIndex = self.targetComboBox.currentIndex()
        autohvbn.enterBattleHandler(int(targetIndex/5)-1,targetIndex%5,self.levelComboBox.currentIndex()+1,self.sweepTimeComboBox.currentIndex(),self.battleInstruction.currentIndex())
            