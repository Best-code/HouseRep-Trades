import sqlite3, os

con = sqlite3.connect("tutorial.db")
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
    transactionType = Clean(csv[1])
    date = Clean(csv[2])
    uptoPrice = Clean(csv[3])
    documentID = Clean(csv[4])
    
    cur.execute(f"INSERT INTO trade VALUES('{asset}', '{uptoPrice}', '{date}', '{documentID}', {transactionType})")
     
def AddAllPersonsToPerson(year: int):
    with open(f"Reports/{year}FD.csv", 'r') as csv:
        for line in csv.readlines():
            AddPersonToPerson(line.split(","))

def AddPersonToPerson(csv: list):
    name = Clean(csv[0])
    docID = Clean(csv[2])
    
    cur.execute(f"INSERT INTO person VALUES('{name}', '{docID}')")
                    
def Clean(textIn: str) -> str:
    return textIn.replace("'","\"").strip()

con.commit()
con.close()