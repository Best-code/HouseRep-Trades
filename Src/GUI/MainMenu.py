# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu copy.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        font = QFont()
        font.setFamilies([u"Copperplate"])
        font.setPointSize(96)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderLabel = QLabel(self.centralwidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeaderLabel.sizePolicy().hasHeightForWidth())
        self.HeaderLabel.setSizePolicy(sizePolicy)
        self.HeaderLabel.setMaximumSize(QSize(1536, 234))
        self.HeaderLabel.setFont(font)
        self.HeaderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HeaderLabel.setWordWrap(True)
        self.HeaderLabel.setIndent(0)

        self.gridLayout.addWidget(self.HeaderLabel, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMaximumSize(QSize(384, 836))
        font1 = QFont()
        font1.setFamilies([u"Copperplate"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, -1, 20, -1)
        self.L_LastName = QLabel(self.groupBox)
        self.L_LastName.setObjectName(u"L_LastName")
        self.L_LastName.setMinimumSize(QSize(128, 128))
        self.L_LastName.setMaximumSize(QSize(16777215, 336))
        font2 = QFont()
        font2.setFamilies([u"Copperplate"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.L_LastName.setFont(font2)

        self.horizontalLayout_14.addWidget(self.L_LastName)

        self.LE_LastName = QLineEdit(self.groupBox)
        self.LE_LastName.setObjectName(u"LE_LastName")

        self.horizontalLayout_14.addWidget(self.LE_LastName)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, -1, 20, -1)
        self.L_Ticker = QLabel(self.groupBox)
        self.L_Ticker.setObjectName(u"L_Ticker")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.L_Ticker.sizePolicy().hasHeightForWidth())
        self.L_Ticker.setSizePolicy(sizePolicy2)
        self.L_Ticker.setMinimumSize(QSize(128, 128))
        self.L_Ticker.setMaximumSize(QSize(16777215, 336))
        self.L_Ticker.setFont(font2)

        self.horizontalLayout_15.addWidget(self.L_Ticker)

        self.LE_Ticker = QLineEdit(self.groupBox)
        self.LE_Ticker.setObjectName(u"LE_Ticker")

        self.horizontalLayout_15.addWidget(self.LE_Ticker)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.L_After = QLabel(self.groupBox)
        self.L_After.setObjectName(u"L_After")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.L_After.sizePolicy().hasHeightForWidth())
        self.L_After.setSizePolicy(sizePolicy3)
        self.L_After.setMinimumSize(QSize(128, 128))
        self.L_After.setMaximumSize(QSize(16777215, 336))
        self.L_After.setFont(font2)

        self.horizontalLayout.addWidget(self.L_After)

        self.DE_After = QDateEdit(self.groupBox)
        self.DE_After.setObjectName(u"DE_After")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.DE_After.sizePolicy().hasHeightForWidth())
        self.DE_After.setSizePolicy(sizePolicy4)
        self.DE_After.setFont(font2)
        self.DE_After.setAccelerated(False)

        self.horizontalLayout.addWidget(self.DE_After)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.L_Before = QLabel(self.groupBox)
        self.L_Before.setObjectName(u"L_Before")
        self.L_Before.setMinimumSize(QSize(128, 128))
        self.L_Before.setMaximumSize(QSize(16777215, 336))
        self.L_Before.setFont(font2)

        self.horizontalLayout_5.addWidget(self.L_Before)

        self.DE_Before = QDateEdit(self.groupBox)
        self.DE_Before.setObjectName(u"DE_Before")
        sizePolicy4.setHeightForWidth(self.DE_Before.sizePolicy().hasHeightForWidth())
        self.DE_Before.setSizePolicy(sizePolicy4)
        self.DE_Before.setFont(font2)

        self.horizontalLayout_5.addWidget(self.DE_Before)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.B_Search = QPushButton(self.groupBox)
        self.B_Search.setObjectName(u"B_Search")

        self.verticalLayout.addWidget(self.B_Search)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 1, 1, 1, 1)

        self.SealLabel = QLabel(self.centralwidget)
        self.SealLabel.setObjectName(u"SealLabel")
        sizePolicy1.setHeightForWidth(self.SealLabel.sizePolicy().hasHeightForWidth())
        self.SealLabel.setSizePolicy(sizePolicy1)
        self.SealLabel.setMaximumSize(QSize(384, 234))
        self.SealLabel.setPixmap(QPixmap(u":/newPrefix/Seal_of_the_house_of_representatives.png"))

        self.gridLayout.addWidget(self.SealLabel, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HeaderLabel.setText(QCoreApplication.translate("MainWindow", u"House Of Representative Trades", None))
        self.groupBox.setTitle("")
        self.L_LastName.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.L_Ticker.setText(QCoreApplication.translate("MainWindow", u"Ticker Symbol", None))
        self.L_After.setText(QCoreApplication.translate("MainWindow", u"After Date", None))
        self.DE_After.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/mm/dd", None))
        self.L_Before.setText(QCoreApplication.translate("MainWindow", u"Before Date", None))
        self.DE_Before.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/mm/dd", None))
        self.B_Search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.SealLabel.setText("")
    # retranslateUi

