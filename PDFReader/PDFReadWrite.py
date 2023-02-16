from PyPDF2 import PdfReader
import csv

recipes = []

def readPDF(pdfFileName):
    pdfFile = open('PDFReader/RecipePDFs/' + pdfFileName + ".pdf", 'rb')
    Reader = PdfReader(pdfFile)
    for i in range((len(Reader.pages))): 
        pageObj = Reader.pages[i]
        content = (pageObj.extract_text())
         #print(content)
        extractMacrosAnabolicCookbook(content, i)
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


def extractMacrosAnabolicCookbook(content, pgNo):
    cals = ""
    carbs= ""
    fats = ""
    pro = ""
    for index, word in enumerate(content.split()):
        word = word.upper()
        i = 1
        if word == "GKCAL.PROTEINCARBS(FIBER)FAT":
            while (content.split()[index - i]).isdigit() or (content.split()[index - i])== ".":
                pro = (content.split()[index - i]) + pro
                i += 1
            i = 1

            while (content.split()[index + i]).isdigit() or (content.split()[index + i])== ".":
                fats += (content.split()[index + i])
                i += 1
            
            i = 1
            while not (content.split()[index + i]) == 'G':
                #print(content.split()[index + i])
                i +=1
            i += 1
            while(content.split()[index + (i)]).isdigit() or (content.split()[index + i])== ".":
                carbs += (content.split()[index + i])
                i += 1

            if all(i != "" for i in (carbs,fats,pro)) :
                cals = (float(pro) * 4 + float(carbs) * 4 + float(fats) * 9)
                recipes.append((cals, carbs, fats, pro, pgNo+1, "ABCB"))
                print("cals: " + str(cals) + "carbs: " + str(carbs) + "pro: " + str(pro) + "fat: " + str(fats) + '\n')
                break

def writeCSVs(pdfFileName):
    with open('PDFReader/RecipeCSVs/' + pdfFileName +'.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cals', 'carbs', 'fats', 'pro', 'pgNo', 'pdf'])

        for i in range(len(recipes)):
            writer.writerow(recipes[i])
    f.close()

def main():
    pdfFileName = 'The AnabolicMD Cookbook' 
    readPDF(pdfFileName)
    writeCSVs(pdfFileName)


if __name__ == "__main__":
    main()