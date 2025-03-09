import sqlite3, os

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE trade(Asset, TransactionType, Date, UptoPrice)")

def AllCSV(year: int):
    for csvFile in os.listdir(f"Reports/{year}/CSVCleanTxtPDF"):
        with open(f"Reports/{year}/CSVCleanTxtPDF/{csvFile}", 'r') as csv:
            for line in csv.readlines():
                AddToDB(line.split(","))
                
def Clean(textIn: str) -> str:
    return textIn.replace("'","\"").strip()

def AddToDB(csv: list):
    # Strip to remove whitespace
    asset = Clean(csv[0])
    transactionType = Clean(csv[1])
    date = Clean(csv[2])
    uptoPrice = Clean(csv[3])
    
    cur.execute(f"INSERT INTO trade VALUES('{asset}', '{transactionType}', '{date}', {uptoPrice})")

AllCSV(2025)
con.commit()

con.close()