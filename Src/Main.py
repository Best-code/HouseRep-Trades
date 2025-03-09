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


# Obtains the Financial Disclosure (FD) from the Clerk website and stores it in Disclosures/{year}FD.txt
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

# Extracts the name, filing type, date and document ID from the FD and is sent to be populated by a CSV
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

# Creates the CSV and stores it in Disclosures/{year}FD.csv
def PopulateCleanUpCSV(file: str, content) -> None:
    with open(f"Disclosures/{file}.csv", "a") as csv:
        csv.write(", ".join(content) + "\n")
        csv.close()

# Creates / Obtains the Trade Report PDF and stores in Reports/{year}/PDF/{Date}-{DocID}.pdf
def GetTradeReport(year: int ,info : list) -> None:
    Name = info[0]
    Date = info[1]
    DocID = info[2]

    url = (f"https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{year}/{DocID}.pdf")
    filename = f"Reports/{year}/PDF/{Date.replace("/","-")}-{DocID}.pdf"
    urlretrieve(url, filename)

# Automatically runs GetTradeReport and obtains all of the P type (Stock purchase) reports using the CSV.
def GetAllTradeReports(year: int) -> None:
    fdCSV =f"Disclosures/{year}FD.csv"
    with open(fdCSV, "r") as csv:
         for line in csv.readlines():

            # Clean all new lines off the data
            info = [x.strip() for x in line.split(",")]
            GetTradeReport(year, info)

# Take a PDF and turn it into text which gets sent to Reports/{year}/TxtPDF/{pdfName}.txt
def PdfToText(year, pdfName):
    # Open the PDF file in read-binary mode
    with open(f"Reports/{year}/PDF/{pdfName}", 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Write the extracted text to a text file
    with open(f"Reports/{year}/TxtPDF/{pdfName[:-4]}.txt", 'w', encoding="utf-8") as txt_file:
        txt_file.write(text)
        txt_file.close()
     

# Runs all Pdfs in the directory of Reports/{Year}
def AllPdfsToText(year: int) -> None:
    # PdfToText(2025, "1-1-2025-20026489.pdf")
    for pdf in os.listdir(f"Reports/{year}/PDF"):
        PdfToText(2025, pdf)
    

# Check if each file contains a certain string
def Check(year: int):
    for pdf in os.listdir(f"Reports/{year}/TxtPDF"):
        with open(f"Reports/{year}/TxtPDF/{pdf}", 'r') as txtPdf:
            print(pdf, end=" ")
            if txtPdf.read().find("* For the complete list of asset type abbreviations") != -1:
                print("Good")
            else:
                print("Bad")
                
            txtPdf.close()
     
# Takes the TxtPDF file, cleans it up and stores it at Reports/{year}/CleanTxtPDF/Clean-{txtFile}
def CleanTextFile(year: int, txtFile: str) -> None:
    with open(f"Reports/{year}/TxtPDF/{txtFile}", 'r', encoding="utf-8") as txt:
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

            

        with open(f"Reports/{year}/CleanTxtPDF/Clean-{txtFile}", "w", encoding="utf-8") as cleanTxtFile:
            cleanTxtFile.write(cleanTxt)
            cleanTxtFile.close()
            
    txt.close()

def CleanAllTextFiles(year: int) -> None:
    for txt in os.listdir(f"Reports/{year}/TxtPDF"):
        CleanTextFile(year, txt)


# Takes The cleaned up PdfToText file which comes from CleanTextFile and extracts the
# Asset, Transaction Type, Date, Price 
# and stores it in a csv at CSVCleanTxtPDF
def RegexOutCleanText(year: int, txtFile: str) -> None:

        # Clean up csv overwrite
    try:
         os.remove(f"Reports/{year}/CSVCleanTxtPDF/{txtFile[:-4]}.csv")
    except FileNotFoundError:
        pass

    asset_pattern = r"^(.*?)(?=\s+\[ST\])"
    transaction_pattern = r"\](\w)"
    date_pattern = r"(\d{2}/\d{2}/\d{4})"
    price_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s*-\s*\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    upto_price_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s*-\s*\$"
    excess_pattern = r"TypeDate Notification DateAmount Cap . Gains > "
    
    with open(f"Reports/{year}/CleanTxtPDF/{txtFile}", 'r', encoding="utf-8") as txt:
        for (number, line) in enumerate(txt.readlines()):
            # Skip empty lines
            if line.isspace():
                continue
            
            #  Skip lines that don't have the right patterns
            if re.search(asset_pattern, line) is None:
                continue
            if re.search(transaction_pattern, line) is None:
                continue
            if re.search(date_pattern, line) is None:
                continue
            if re.search(price_pattern, line) is None:
                continue 
            
            
            asset = line[:re.search(asset_pattern, line).end()].replace(",","").strip()
            # # Cutting out the table spill over
            if re.search(excess_pattern, asset):
                asset = asset[re.search(excess_pattern, line).end():]
                
            transactionType = line[re.search(transaction_pattern, line).start()+1 : re.search(transaction_pattern, line).end()].replace(",","").strip()
            date = line[re.search(date_pattern, line).start() : re.search(date_pattern, line).end()].replace(",","").strip()
            price = line[re.search(upto_price_pattern, line).end() : re.search(price_pattern, line).end()].replace(",","").strip()

            GenerateStockCSV(year, txtFile, asset, transactionType, date, price)
        
        txt.close()
        
def RegexOutAllCleanText(year: int):
    for txt in os.listdir(f"Reports/{year}/CleanTxtPDF"):
        RegexOutCleanText(year, txt) 
        
# Generates the CSV for the Cleaned and Regexed PDFtoText file
def GenerateStockCSV(year, txtFile, asset, transactionType, date, price):
    with open(f"Reports/{year}/CSVCleanTxtPDF/{txtFile[:-4]}.csv", 'a', encoding="utf-8") as txtCleaner:
        txtCleaner.write(f"{asset}, ")
        txtCleaner.write(f"{transactionType}, ")
        txtCleaner.write(f"{date}, ")
        txtCleaner.write(f"{price}\n")
        txtCleaner.close()

# AllPdfsToText(2025)
# CleanAllTextFiles(2025)
RegexOutAllCleanText(2025)


# 1. GetFDReport
# 2. DesminateDocID -> PopulateCleanupCSV
# 3. GetAllTradeReports -> GetTradeReport
# 4. AllPdfsToText -> PdfToText
# 5. CleanAllTextFiles -> CleanTextFile
# 6. RegexOutCleanText -> GenerateStockCSV