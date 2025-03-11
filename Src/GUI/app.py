import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

from MainMenu import Ui_MainWindow
import sqlite3, os
from PySide6.QtSql import QSqlRelationalTableModel, QSqlDatabase, QSqlTableModel
from datetime import datetime

    

    

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create UI instance
        self.ui.setupUi(self)  # Load UI
        
        self.name = ""
        self.ticker = ""
        self.year = self.ui.DE_Year.date().toString("yyyy")
        
        self.con = sqlite3.connect("/Users/melons/Documents/Code/Python/HOR-Trades/Src/Data-Collection-Processing/Finance.db")
        self.cur = self.con.cursor()

        self.ui.LE_Name.textChanged.connect(self.onNameUpdate)
        self.ui.LE_Asset.textChanged.connect(self.onTickerUpdate)
        self.ui.DE_Year.dateChanged.connect(self.onYearUpdate)
        self.ui.PB_Search.clicked.connect(self.executeSQL)

        SealPixMap = QPixmap("Assets/Seal_of_the_house_of_representatives.png")
        self.ui.L_Seal.setPixmap(SealPixMap)

        self.ui.TV_Table.verticalHeader().hide()


    def onNameUpdate(self):
        self.name = self.ui.LE_Name.text()  # Update Name text

    def onTickerUpdate(self):
        self.ticker = self.ui.LE_Asset.text()  # Update Name text

    def onYearUpdate(self):
        self.year = self.ui.DE_Year.date().toString("yyyy")

    """
    TODO!
    2. If their is a name filter, we will need to join Person x Trade together on ALL.
    3. Check the date range and pull info from those tables joined together.
    
    """

    def generateQuery(self):
        self.tableName = f"trade_{self.year}"
        baseQuery = f"SELECT * FROM {self.tableName}"
        
        # if(self.name != ""):
        #     baseQuery += " WHERE Name LIKE '%{self.name}%'"
        
        if(self.ticker != ""):
            baseQuery += f" WHERE AssetTicker LIKE '%{self.ticker}%'"
        
        return baseQuery+";"
    
    def executeSQL(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("/Users/melons/Documents/Code/Python/HOR-Trades/Src/Data-Collection-Processing/Finance.db")

        model = QSqlRelationalTableModel()
        model.setTable("trade_2024")
        model.select()

        self.ui.TV_Table.setModel(model)
        self.ui.TV_Table.resizeColumnsToContents()
        

        # res = self.cur.execute(self.generateQuery())

         
 


# Run the application
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
    con.close()