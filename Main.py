from urllib.request import urlretrieve
from zipfile import ZipFile
import os, re
from openai import OpenAI
import PyPDF2
from dotenv import load_dotenv

"""
Order
1. GetFDReport
2. DesminateDocID -> PopulateCleanupCSV
3. GetAllTradeReports -> GetTradeReport
4. AllPdfsToText -> PdfToText
5. CleanAllTextFiles -> CleanTextFile
6. RegexOutCleanTextFile -> GenerateCleanCSV
"""

# Provides the TXT File which we derive the Clean CSV From
def GetFDReport(year: int) -> None:
    url = f"https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{year}FD.zip"
    filename = f"{year}FD.zip"
    urlretrieve(url, filename)

    folderName = f"{year}FD.zip"

    with ZipFile(folderName, "r") as myZip:
            myZip.extractall(path="Disclosures")
            myZip.close()

    os.remove(folderName)
    os.remove(f"Disclosures/{year}FD.xml")

# Provides the Trade Report PDF
def GetTradeReport(year: int ,info : list) -> None:
    Name = info[0]
    Date = info[1]
    DocID = info[2]

    url = (f"https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{year}/{DocID}.pdf")
    filename = f"Reports/{year}/{Date.replace("/","-")}-{DocID}.pdf"
    urlretrieve(url, filename)

# Creates the CSV
def PopulateCleanUpCSV(file: str, content) -> None:
    with open(f"{file}.csv", "a") as csv:
        csv.write(", ".join(content) + "\n")
        csv.close()

# Cleans up the FD Report Text File
def DeseminateDocID(year: int):

    # Generic File Name with no extension
    fdFile =f"Disclosures/{year}FD"

    # Clean up csv overwrite
    try:
         os.remove(f"{fdFile}.csv")
    except FileNotFoundError:
        pass

    # Open up the Disclosure and extract the useful information one line at a time
    with open(f"{fdFile}.txt", "r") as fd:
        for line in fd.readlines()[1:]:
                if re.search(r"\s+P\s+", line) is None:
                    continue
                
                # Regexes to locate certain patterns to help with substring extraction
                NameStartDelim = re.search(r"\s+.*", line).start()
                FilingTypeDelim = re.search(r"\b\w\b", line).start()
                DateDelim = re.search(r"\d{1,2}/\d{1,2}/2025\s+", line) 

                # Substring extraction
                repName = " ".join(line[NameStartDelim : FilingTypeDelim].strip().split())
                date = line[DateDelim.start():DateDelim.end()].strip()
                docID = line[DateDelim.end():].strip()

                # Population of the CSV of only type P and DocID with first number == 2
                if(docID[0] == '2'):
                    PopulateCleanUpCSV(fdFile, [repName, date, docID])
                
        fd.close()

# Automatically runs GetTradeReport and obtains all of the P type (Stock purchase) reports with the help of the CSV.
def GetAllTradeReports(year: int) -> None:
    fdCSV =f"Disclosures/{year}FD.csv"
    with open(fdCSV, "r") as csv:
         for line in csv.readlines():

            # Clean all new lines off the data
            info = [x.strip() for x in line.split(",")]
            GetTradeReport(year, info)

# Take a PDF and turn it into text which gets sent to Reports/{year}Txt
def PdfToText(year, pdfName):
    # Open the PDF file in read-binary mode
    with open(f"Reports/{year}/{pdfName}", 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Write the extracted text to a text file
    with open(f"Reports/{year}Txt/{pdfName[:-4]}.txt", 'w', encoding="utf-8") as txt_file:
        txt_file.write(text)
        txt_file.close()
     

# Runs all Pdfs in the directory of Reports/{Year}
def AllPdfsToText(year: int) -> None:
    # PdfToText(2025, "1-1-2025-20026489.pdf")
    for pdf in os.listdir(f"Reports/{year}"):
        PdfToText(2025, pdf)
    

# Check if each file contains a certain string
def Check():
    for pdf in os.listdir("Reports/2025Txt"):
        with open(f"Reports/2025Txt/{pdf}", 'r') as txtPdf:
            print(pdf, end=" ")
            if txtPdf.read().find("* For the complete list of asset type abbreviations") != -1:
                print("Good")
            else:
                print("Bad")
                
            txtPdf.close()
     
# Takes the PdfToText text file and cleans it up
def CleanTextFile(year: int, txtFile: str) -> None:
    with open(f"Reports/{year}Txt/{txtFile}", 'r', encoding="utf-8") as txt:
        stocks: bool = False
        cleanTxt: str = ""

        """"
        Only add lines that appear after $200? because that is where the stocks start
        """
        for line in txt.readlines():
            if line.count("* For the complete list of asset type") >= 1:
                break
            if line.find("$200?") != -1:
                stocks = True
            elif stocks:
                if(line.count(": ") == 0):
                    cleanTxt += line.strip() + " "
                else:
                    cleanTxt += "\n"

            

        with open(f"Reports/{year}Txt/Clean-{txtFile}", "w", encoding="utf-8") as cleanTxtFile:
            cleanTxtFile.write(cleanTxt)
            cleanTxtFile.close()
            
    txt.close()

# Takes The cleaned up PdfToText file which comes from CleanTextFile and extracts the Asset, Transaction Type, Date, Price and stores it in a csv
def RegexOutCleanTextFile(yar: int, txtFile: str) -> None:

        # Clean up csv overwrite
    try:
         os.remove(f"Reports/{year}Txt/Cleaner-{txtFile}")
    except FileNotFoundError:
        pass

    asset_pattern = r"^(.*?)(?=\s+\[ST\])"
    transaction_pattern = r"\](\w)"
    date_pattern = r"(\d{2}/\d{2}/\d{4})"
    price_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s*-\s*\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    
    with open(f"Reports/{year}Txt/Clean-{txtFile}", 'r', encoding="utf-8") as txt:
        for line in txt.readlines():
            
            # Skip empty lines
            if line == "\n":
                continue
            
            asset = line[:re.search(asset_pattern, line).end()]
            transactionType = line[re.search(transaction_pattern, line).start()+1 : re.search(transaction_pattern, line).end()]
            date = line[re.search(date_pattern, line).start() : re.search(date_pattern, line).end()]
            price = line[re.search(price_pattern, line).start() : re.search(price_pattern, line).end()]

            GenerateStockCSV(year, txtFile, asset, transactionType, date, price)
        
        txt.close()
        
# Formats the CSV for the Cleaned and Regexed PDFtoText file
def GenerateStockCSV(year, txtFile, asset, transactionType, date, price):
    with open(f"Reports/{year}Txt/Cleaner-{txtFile}", 'a', encoding="utf-8") as txtCleaner:
        txtCleaner.write(f"{asset}, ")
        txtCleaner.write(f"{transactionType}, ")
        txtCleaner.write(f"{date}, ")
        txtCleaner.write(f"{price}, \n")
        txtCleaner.close()


CleanTextFile(2025, "2-25-2025-20027846.txt")
RegexOutCleanTextFile(2025, "2-25-2025-20027846.txt")

