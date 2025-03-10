import sqlite3, os
from datetime import datetime

year = 2023

con = sqlite3.connect("Finance.db")
cur = con.cursor()

# Creating tables
personTableName = f"person_{int(year)}"  # Ensure year is integer to prevent SQL injection
cur.execute(f"""
CREATE TABLE IF NOT EXISTS {personTableName} (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    DocumentID TEXT UNIQUE NOT NULL
)
""")

tradeTableName = f"trade_{int(year)}"  # Ensure year is integer to prevent SQL injection
cur.execute(f"""CREATE TABLE IF NOT EXISTS {tradeTableName} (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    AssetTicker TEXT NOT NULL,
    Price REAL NOT NULL,
    DatePurchased TEXT NOT NULL,
    DocumentID TEXT NOT NULL,
    TransactionType TEXT NOT NULL,
    FOREIGN KEY (DocumentID) REFERENCES persons(DocumentID) ON DELETE CASCADE
)""")




def AddAllTradesToTrade(year: int):
    for csvFile in os.listdir(f"Reports/{year}/CSVCleanTxtPDF"):
        with open(f"Reports/{year}/CSVCleanTxtPDF/{csvFile}", 'r') as csv:
            for line in csv.readlines():
                AddTradeToTrade(line.split(","))    
     
def AddTradeToTrade(csv: list):
    # Strip to remove whitespace
    asset = Clean(csv[0])
    uptoPrice = Clean(csv[1])
    date = Clean(csv[2])
    documentID = Clean(csv[3])
    transactionType = Clean(csv[4])

    # Convert to SQLite format (YYYY-MM-DD)
    date_obj = datetime.strptime(date, "%m/%d/%Y")
    sqlite_date = date_obj.strftime("%Y-%m-%d")
    
    query = f"INSERT INTO {tradeTableName} (AssetTicker, Price, DatePurchased, DocumentID, TransactionType) VALUES (?, ?, ?, ?, ?)"
    cur.execute(query,(asset, uptoPrice, sqlite_date, documentID, transactionType))
     
def AddAllPersonsToPerson(year: int):
    with open(f"Disclosures/{year}FD.csv", 'r') as csv:
        for line in csv.readlines():
            AddPersonToPerson(line.split(","))

def AddPersonToPerson(csv: list):
    name = Clean(csv[0])
    docID = Clean(csv[2])
    
    query = f"INSERT INTO {personTableName} (Name, DocumentID) VALUES (?, ?)"
    cur.execute(query, (name, docID))
    
                    
def Clean(textIn: str) -> str:
    return textIn.replace("'","\"").strip()


# AddAllTradesToTrade(year)
# AddAllPersonsToPerson(year)

con.commit()
con.close()