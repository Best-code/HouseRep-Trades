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
        self.tableName = f"trade_{self.year}"
        
        self.name = ""
        self.ticker = ""
        self.after = ""
        self.before = ""

        self.ui.LE_LastName.textChanged.connect(self.onNameUpdate)
        self.ui.LE_Ticker.textChanged.connect(self.onTickerUpdate)
        self.ui.DE_After.dateChanged.connect(self.onAfterUpdate)
        self.ui.DE_Before.dateChanged.connect(self.onBeforeUpdate)
        self.ui.B_Search.clicked.connect(self.executeSQL)

    def onNameUpdate(self):
        self.name = self.ui.LE_LastName.text()  # Update Name text

    def onTickerUpdate(self):
        self.ticker = self.ui.LE_Ticker.text()  # Update Name text

    def onAfterUpdate(self):
        self.after = self.ui.DE_After.date()

    def onBeforeUpdate(self):
        self.before = self.ui.DE_Before.date()

    def executeSQL(self):
        res = self.cur.execute(f"SELECT * FROM {self.tableName};")
        print(res.fetchall())
         
 


# Run the application
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
    con.close()