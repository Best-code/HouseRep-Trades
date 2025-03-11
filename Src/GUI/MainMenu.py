# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewMainMenu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Copperplate"])
        font.setPointSize(24)
        font.setBold(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"*{\n"
"	font-family: Copperplate;\n"
"	font-size: 24pt;\n"
"	font-weight: normal;\n"
"\n"
"	background-color: black;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SealWidget = QWidget(self.centralwidget)
        self.SealWidget.setObjectName(u"SealWidget")
        self.SealWidget.setMaximumSize(QSize(384, 234))
        self.gridLayout_2 = QGridLayout(self.SealWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.L_Seal = QLabel(self.SealWidget)
        self.L_Seal.setObjectName(u"L_Seal")
        self.L_Seal.setMaximumSize(QSize(384, 234))
        self.L_Seal.setPixmap(QPixmap(u":/newPrefix/Seal_of_the_house_of_representatives.png"))
        self.L_Seal.setScaledContents(True)

        self.gridLayout_2.addWidget(self.L_Seal, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.SealWidget)

        self.HeaderBar = QWidget(self.centralwidget)
        self.HeaderBar.setObjectName(u"HeaderBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeaderBar.sizePolicy().hasHeightForWidth())
        self.HeaderBar.setSizePolicy(sizePolicy)
        self.HeaderBar.setMaximumSize(QSize(1920, 234))
        self.HeaderBar.setStyleSheet(u"*{\n"
"	font-family: Copperplate;\n"
"	font-size: 64pt;\n"
"	font-weight: normal;\n"
"}\n"
"QWidget{\n"
"background-color: #991916;\n"
"}")
        self.gridLayout = QGridLayout(self.HeaderBar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(48, 0, 48, 0)
        self.label_2 = QLabel(self.HeaderBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(1536, 234))
        font1 = QFont()
        font1.setFamilies([u"Copperplate"])
        font1.setPointSize(64)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.HeaderBar)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LeftSideBar = QWidget(self.centralwidget)
        self.LeftSideBar.setObjectName(u"LeftSideBar")
        self.LeftSideBar.setMaximumSize(QSize(384, 846))
        self.LeftSideBar.setStyleSheet(u"QWidget {\n"
"	background-color: #19225F;\n"
"}\n"
"\n"
"*[isFilterOption=\"true\"] {\n"
"	background-color: rgba(255, 255, 255 , 25);\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 25px;\n"
"}\n"
"\n"
"QRadioButton, *[isFilterLabel=\"true\"] {\n"
"		background-color: transparent;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.LeftSideBar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.OptionFrame = QWidget(self.LeftSideBar)
        self.OptionFrame.setObjectName(u"OptionFrame")
        self.verticalLayout = QVBoxLayout(self.OptionFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, 0, 24, 0)
        self.Filters = QLabel(self.OptionFrame)
        self.Filters.setObjectName(u"Filters")
        sizePolicy.setHeightForWidth(self.Filters.sizePolicy().hasHeightForWidth())
        self.Filters.setSizePolicy(sizePolicy)
        self.Filters.setMaximumSize(QSize(336, 54))
        font2 = QFont()
        font2.setFamilies([u"Copperplate"])
        font2.setBold(False)
        self.Filters.setFont(font2)
        self.Filters.setStyleSheet(u"font-size: 36px;\n"
"\n"
"")
        self.Filters.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Filters)

        self.FilterOption = QWidget(self.OptionFrame)
        self.FilterOption.setObjectName(u"FilterOption")
        self.FilterOption.setMaximumSize(QSize(336, 72))
        self.FilterOption.setProperty(u"isFilterOption", True)
        self.horizontalLayout_2 = QHBoxLayout(self.FilterOption)
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.RB_Name = QRadioButton(self.FilterOption)
        self.RB_Name.setObjectName(u"RB_Name")

        self.horizontalLayout_2.addWidget(self.RB_Name)

        self.LE_Name = QLineEdit(self.FilterOption)
        self.LE_Name.setObjectName(u"LE_Name")

        self.horizontalLayout_2.addWidget(self.LE_Name)


        self.verticalLayout.addWidget(self.FilterOption)

        self.FilterOption_3 = QWidget(self.OptionFrame)
        self.FilterOption_3.setObjectName(u"FilterOption_3")
        self.FilterOption_3.setMaximumSize(QSize(336, 72))
        self.FilterOption_3.setProperty(u"isFilterOption", True)
        self.horizontalLayout_4 = QHBoxLayout(self.FilterOption_3)
        self.horizontalLayout_4.setSpacing(18)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.RB_Asset = QRadioButton(self.FilterOption_3)
        self.RB_Asset.setObjectName(u"RB_Asset")

        self.horizontalLayout_4.addWidget(self.RB_Asset)

        self.LE_Asset = QLineEdit(self.FilterOption_3)
        self.LE_Asset.setObjectName(u"LE_Asset")

        self.horizontalLayout_4.addWidget(self.LE_Asset)


        self.verticalLayout.addWidget(self.FilterOption_3)

        self.FilterOption_5 = QWidget(self.OptionFrame)
        self.FilterOption_5.setObjectName(u"FilterOption_5")
        self.FilterOption_5.setMaximumSize(QSize(336, 72))
        self.FilterOption_5.setProperty(u"isFilterOption", True)
        self.horizontalLayout_6 = QHBoxLayout(self.FilterOption_5)
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.L_Year = QLabel(self.FilterOption_5)
        self.L_Year.setObjectName(u"L_Year")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.L_Year.sizePolicy().hasHeightForWidth())
        self.L_Year.setSizePolicy(sizePolicy1)
        self.L_Year.setMaximumSize(QSize(72, 72))
        self.L_Year.setProperty(u"isFilterLabel", True)

        self.horizontalLayout_6.addWidget(self.L_Year)

        self.DE_Year = QDateEdit(self.FilterOption_5)
        self.DE_Year.setObjectName(u"DE_Year")
        self.DE_Year.setMinimumDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.DE_Year.setMaximumDate(QDate(2025, 12, 31))

        self.horizontalLayout_6.addWidget(self.DE_Year)


        self.verticalLayout.addWidget(self.FilterOption_5)

        self.widget = QWidget(self.OptionFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(384, 50))
        self.widget.setStyleSheet(u"font-size: 14px;")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CB_Purchase = QCheckBox(self.widget)
        self.CB_Purchase.setObjectName(u"CB_Purchase")
        sizePolicy.setHeightForWidth(self.CB_Purchase.sizePolicy().hasHeightForWidth())
        self.CB_Purchase.setSizePolicy(sizePolicy)
        self.CB_Purchase.setMaximumSize(QSize(96, 50))
        self.CB_Purchase.setFont(font2)
        self.CB_Purchase.setChecked(True)

        self.horizontalLayout_3.addWidget(self.CB_Purchase)

        self.CB_Sale = QCheckBox(self.widget)
        self.CB_Sale.setObjectName(u"CB_Sale")
        sizePolicy.setHeightForWidth(self.CB_Sale.sizePolicy().hasHeightForWidth())
        self.CB_Sale.setSizePolicy(sizePolicy)
        self.CB_Sale.setMaximumSize(QSize(64, 50))
        self.CB_Sale.setFont(font2)
        self.CB_Sale.setChecked(True)

        self.horizontalLayout_3.addWidget(self.CB_Sale)

        self.CB_Exchange = QCheckBox(self.widget)
        self.CB_Exchange.setObjectName(u"CB_Exchange")
        sizePolicy.setHeightForWidth(self.CB_Exchange.sizePolicy().hasHeightForWidth())
        self.CB_Exchange.setSizePolicy(sizePolicy)
        self.CB_Exchange.setMaximumSize(QSize(96, 50))
        self.CB_Exchange.setFont(font2)
        self.CB_Exchange.setChecked(True)

        self.horizontalLayout_3.addWidget(self.CB_Exchange)


        self.verticalLayout.addWidget(self.widget)

        self.PB_Search = QPushButton(self.OptionFrame)
        self.PB_Search.setObjectName(u"PB_Search")
        self.PB_Search.setMaximumSize(QSize(336, 72))

        self.verticalLayout.addWidget(self.PB_Search)


        self.verticalLayout_2.addWidget(self.OptionFrame)


        self.horizontalLayout_7.addWidget(self.LeftSideBar)

        self.MainBody = QWidget(self.centralwidget)
        self.MainBody.setObjectName(u"MainBody")
        sizePolicy.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy)
        self.MainBody.setMaximumSize(QSize(1536, 846))
        self.horizontalLayout_5 = QHBoxLayout(self.MainBody)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.TV_Table = QTableView(self.MainBody)
        self.TV_Table.setObjectName(u"TV_Table")
        self.TV_Table.setMaximumSize(QSize(1536, 846))
        self.TV_Table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TV_Table.setAlternatingRowColors(True)
        self.TV_Table.setSortingEnabled(True)

        self.horizontalLayout_5.addWidget(self.TV_Table)


        self.horizontalLayout_7.addWidget(self.MainBody)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.L_Seal.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"House Of Representative Trades", None))
        self.LeftSideBar.setProperty(u"id", QCoreApplication.translate("MainWindow", u"LeftSideBar", None))
        self.Filters.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.RB_Name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.RB_Asset.setText(QCoreApplication.translate("MainWindow", u"Asset", None))
        self.L_Year.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.DE_Year.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy", None))
        self.CB_Purchase.setText(QCoreApplication.translate("MainWindow", u"Purchase", None))
        self.CB_Sale.setText(QCoreApplication.translate("MainWindow", u"Sale", None))
        self.CB_Exchange.setText(QCoreApplication.translate("MainWindow", u"Exchange", None))
        self.PB_Search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

