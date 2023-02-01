from PyPDF2 import PdfReader
import csv

recipes = []

def readPDF(pdfFileName):
    pdfFile = open('PDFReader/RecipePDFs/' + pdfFileName + ".pdf", 'rb')
    Reader = PdfReader(pdfFile)
    for i in range((len(Reader.pages))): 
        pageObj = Reader.pages[i]
        content = (pageObj.extract_text())
        extractMacros(content, i)
    pdfFile.close()

def extractMacros(content, pgNo):
    cals = 0
    carbs= 0
    fats = 0
    pro = 0
    for index, word in enumerate(content.split()):
        word = word.upper()
        if word == "CALORIES:":
            cals = (content.split()[index + 1])
        if word == "CARBS:":
            carbs = (content.split()[index + 1].removesuffix('G'))
        if word == "FAT:":
            fats = (content.split()[index + 1])
        if word == "PROTEIN:":
            pro = (content.split()[index + 1].removesuffix('G'))

        if all(i != 0 for i in (cals,carbs,fats,pro)) :
            recipes.append((cals, carbs, fats, pro, pgNo+1, "BTB"))
            break

def writeCSV(pdfFileName):
    with open('PDFReader/RecipeCSVs/' + pdfFileName +'.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cals', 'carbs', 'fats', 'pro', 'pgNo', 'pdf'])

        for i in range(len(recipes)):
            writer.writerow(recipes[i])
    f.close()

def main():
    pdfFileName = 'BTB-Cookbook' 
    readPDF(pdfFileName)
    writeCSV(pdfFileName)

if __name__ == "__main__":
    main()