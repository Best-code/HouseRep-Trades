import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

from MainMenu import Ui_MainWindow
from PySide6.QtSql import QSqlRelationalTableModel, QSqlDatabase, QSqlTableModel
from datetime import datetime

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create UI instance
        self.ui.setupUi(self)  # Load UI

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("/Users/melons/Documents/Code/Python/HOR-Trades/Src/Data-Collection-Processing/Finance.db")
        
        self.name = ""
        self.ticker = ""
        self.year = self.ui.DE_Year.date().toString("yyyy")
        
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

    def setFilters(self, model: QSqlRelationalTableModel):
        self.tableName = f"trade_{self.year}"
        model.setTable("trade_2024")
        
        if(self.ticker != ""):
            model.setFilter(f"AssetTicker LIKE '%{self.ticker}%'")
    
    def setColumnNames(self, model: QSqlRelationalTableModel):
        column = 0
        model.setHeaderData(column, Qt.Orientation.Horizontal, "ID")
        if(model.columnCount() == 7):
            column+1
            model.setHeaderData(column, Qt.Orientation.Horizontal, "Name")
            
        model.setHeaderData(column+1, Qt.Orientation.Horizontal, "Asset")
        model.setHeaderData(column+2, Qt.Orientation.Horizontal, "Price")
        model.setHeaderData(column+3, Qt.Orientation.Horizontal, "Date")
        model.setHeaderData(column+4, Qt.Orientation.Horizontal, "DocID")
        model.setHeaderData(column+5, Qt.Orientation.Horizontal, "Type")
    
    def executeSQL(self):

        model = QSqlRelationalTableModel()
        self.setFilters(model)
        model.select()
        self.setColumnNames(model)

        self.ui.TV_Table.setModel(model)
        self.ui.TV_Table.resizeColumnsToContents()
        


         
 


# Run the application
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
    con.close()