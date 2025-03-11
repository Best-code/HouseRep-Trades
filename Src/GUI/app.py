import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from MainMenu import Ui_MainWindow
import sqlite3, os
from datetime import datetime

    

    

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create UI instance
        self.ui.setupUi(self)  # Load UI
        
        self.year = 2025
        self.con = sqlite3.connect("/Users/melons/Documents/Code/Python/HOR-Trades/Src/Data-Collection-Processing/Finance.db")
        self.cur = self.con.cursor()
        
        self.name = ""
        self.ticker = ""
        self.year = self.ui.DE_Year.date().toString("yyyy")
        self.after = ""
        self.before = ""

        self.ui.LE_LastName.textChanged.connect(self.onNameUpdate)
        self.ui.LE_Ticker.textChanged.connect(self.onTickerUpdate)
        self.ui.DE_After.dateChanged.connect(self.onAfterUpdate)
        self.ui.DE_Year.dateChanged.connect(self.onYearUpdate)
        self.ui.DE_Before.dateChanged.connect(self.onBeforeUpdate)
        self.ui.B_Search.clicked.connect(self.executeSQL)

    def onNameUpdate(self):
        self.name = self.ui.LE_LastName.text()  # Update Name text

    def onTickerUpdate(self):
        self.ticker = self.ui.LE_Ticker.text()  # Update Name text

    def onYearUpdate(self):
        self.year = self.ui.DE_Year.date().toString("yyyy")

    def onAfterUpdate(self):
        self.after = self.ui.DE_After.date()

    def onBeforeUpdate(self):
        self.before = self.ui.DE_Before.date()


    """
    TODO!
    
    1. Simplify the date range to just one year at a time for now between 2023-2025
    2. If their is a name filter, we will need to join Person x Trade together on ALL.
    3. Check the date range and pull info from those tables joined together.
    
    """

    def generateQuery(self):
        self.tableName = f"trade_{self.year}"
        baseQuery = f"SELECT * FROM {self.tableName}"
        # If there is nothing, then search everything
        
        # if(self.name != ""):
        #     baseQuery += " WHERE Name LIKE '%{self.name}%'"
        
        if(self.ticker != ""):
            baseQuery += f" WHERE AssetTicker LIKE '%{self.ticker}%'"
        
        return baseQuery+";"
    
    def executeSQL(self):
        res = self.cur.execute(self.generateQuery())
        print(res.fetchall())
         
 


# Run the application
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
    con.close()