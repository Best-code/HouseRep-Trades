import sqlite3, os

year = 2024

con = sqlite3.connect(f"{year}.db")
cur = con.cursor()

# Creating tables
cur.execute("""
CREATE TABLE IF NOT EXISTS person (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    DocumentID TEXT UNIQUE NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS trade (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    AssetTicker TEXT NOT NULL,
    Price REAL NOT NULL,
    DatePurchased TEXT NOT NULL,
    DocumentID TEXT NOT NULL,
    TransactionType TEXT NOT NULL,
    FOREIGN KEY (DocumentID) REFERENCES persons(DocumentID) ON DELETE CASCADE
)
""")



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
    
    cur.execute("INSERT INTO trade (AssetTicker, Price, DatePurchased, DocumentID, TransactionType) VALUES (?, ?, ?, ?, ?)",
                (asset, uptoPrice, date, documentID, transactionType))
     
def AddAllPersonsToPerson(year: int):
    with open(f"Disclosures/{year}FD.csv", 'r') as csv:
        for line in csv.readlines():
            AddPersonToPerson(line.split(","))

def AddPersonToPerson(csv: list):
    name = Clean(csv[0])
    docID = Clean(csv[2])
    
    cur.execute("INSERT INTO person (Name, DocumentID) VALUES (?, ?)", (name, docID))
    
                    
def Clean(textIn: str) -> str:
    return textIn.replace("'","\"").strip()


# AddAllTradesToTrade(year)
# AddAllPersonsToPerson(year)

con.commit()
con.close()