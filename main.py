import PyPDF2.utils
import os
import re


def search(directory, word):
    directory = re.sub('/$', '', directory)
    for name in os.listdir(directory):
        file = directory + "/" + name
        if os.path.isdir(file):
            search(file, word)
        else:
            try:
                obj = PyPDF2.PdfFileReader(file)
            except PyPDF2.utils.PdfReadError:
                break
            numPages = obj.getNumPages()

            found = False
            for i in range(0, numPages):
                pageObj = obj.getPage(i)
                text = pageObj.extractText()
                if word in text.lower():
                    found = True
                    print("-")
                    print("FOUND!")
                    print(text.lower())

            if found:
                print(file)


search("ExportedContents/", "dais")
