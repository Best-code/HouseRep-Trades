import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QStyledItemDelegate
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

from MainMenu import Ui_MainWindow
from PySide6.QtSql import QSqlRelationalTableModel, QSqlDatabase, QSqlTableModel, QSqlRelation
from datetime import datetime

class CurrencyDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        """Format column as currency (e.g., $1,000.00)"""
        try:
            value = float(value)  # Ensure it's a number
            return f"${value:,.2f}"  # Format as money
        except ValueError:
            return value  # If not a number, return as-is

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
        self.purchase = True
        self.sale = True
        self.exchange = True
        
        self.ui.LE_Name.textChanged.connect(self.onNameUpdate)
        self.ui.LE_Asset.textChanged.connect(self.onTickerUpdate)
        self.ui.DE_Year.dateChanged.connect(self.onYearUpdate)
        self.ui.PB_Search.clicked.connect(self.executeSQL)
        self.ui.CB_Sale.clicked.connect(self.onSaleUpdate)
        self.ui.CB_Exchange.clicked.connect(self.onExchangeUpdate)
        self.ui.CB_Purchase.clicked.connect(self.onPurchaseUpdate)

        SealPixMap = QPixmap("Assets/Seal_of_the_house_of_representatives.png")
        self.ui.L_Seal.setPixmap(SealPixMap)

        self.ui.TV_Table.verticalHeader().hide()


    def onNameUpdate(self):
        self.name = self.ui.LE_Name.text()  # Update Name text

    def onTickerUpdate(self):
        self.ticker = self.ui.LE_Asset.text()  # Update Name text

    def onYearUpdate(self):
        self.year = self.ui.DE_Year.date().toString("yyyy")

    def onPurchaseUpdate(self):
        self.purchase = self.ui.CB_Purchase.isChecked()

    def onExchangeUpdate(self):
        self.exchange = self.ui.CB_Exchange.isChecked()

    def onSaleUpdate(self):
        self.sale = self.ui.CB_Sale.isChecked()

    def generateFilter(self):
        filter = self.generateCBFilters(self.generateNameTickerFilter())
        print(filter)
        return filter

    def generateNameTickerFilter(self):
        baseQuery = ""
        if(self.name and self.ticker):
            baseQuery += f"Name LIKE '%{self.name}%' AND AssetTicker LIKE '%{self.ticker}%'"
        elif(self.name):
            baseQuery += f"Name LIKE '%{self.name}%'"
        elif(self.ticker):
            baseQuery += f"AssetTicker LIKE '%{self.ticker}%'"
            
        return baseQuery
    
    def generateCBFilters(self, NameTickerFilter):
        # If accepting all checkboxes, filter nothing and return
        if (
        (self.exchange and self.purchase and self.sale) 
        or 
        (not self.exchange and not self.purchase and not self.sale)
        ):
            return NameTickerFilter

        if NameTickerFilter:
            NameTickerFilter += " AND "

        if self.purchase and self.exchange:
            NameTickerFilter += "TransactionType = 'P' OR TransactionType = 'E'"

        elif self.purchase and self.sale:
            NameTickerFilter += "TransactionType = 'P' OR TransactionType = 'S'"

        elif self.exchange and self.sale:
            NameTickerFilter += "TransactionType = 'E' OR TransactionType = 'S'"
        
        elif self.exchange:
            NameTickerFilter += "TransactionType = 'E'"

        elif self.purchase:
            NameTickerFilter += "TransactionType = 'P'"

        elif self.sale:
            NameTickerFilter += "TransactionType = 'S'"
            
        return NameTickerFilter
            

    def setFilters(self, model: QSqlRelationalTableModel):
        tradeTableName = f"trade_{self.year}"
        personTableName = f"person_{self.year}"
        model.setTable(tradeTableName)

        model.setRelation(4, QSqlRelation(personTableName, "DocumentID", "Name"))

        model.setFilter(self.generateFilter())
    
    def setColumnNames(self, model: QSqlRelationalTableModel):
        model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Asset")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Price")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Date")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "Name")
        model.setHeaderData(5, Qt.Orientation.Horizontal, "Type")

    def styleColumns(self, model : QSqlRelationalTableModel | QSqlTableModel):
        # Hide the ID Column
        self.ui.TV_Table.hideColumn(0)

        print(f"Total Columns: {model.columnCount()}")
        for i in range(model.columnCount()):
            print(f"Column {i}: {model.headerData(i, Qt.Orientation.Horizontal)}")

        self.ui.TV_Table.setItemDelegateForColumn(2, CurrencyDelegate())
        self.ui.TV_Table.setColumnWidth(1, 150)
        self.ui.TV_Table.setColumnWidth(2, 200)
        self.ui.TV_Table.setColumnWidth(3, 200)
        
    def executeSQL(self):

        model = QSqlRelationalTableModel()
        self.setFilters(model)
        model.select()
        self.setColumnNames(model)

        self.ui.TV_Table.setModel(model)
        self.ui.TV_Table.resizeColumnsToContents()
        
        self.styleColumns(model)


        


         
 


# Run the application
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
    con.close()