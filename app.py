import os, sys
import csv
from docxtpl import DocxTemplate

# change path to current working directory
os.chdir(sys.path[0])

# hash to clean header
m = {}

# user input
file = './' + input("csv file name : ")
output = input("output file name format : ")

with open(file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)

    # header
    headers = next(reader)
    c = 0
    for i in headers:
        m[c] = i
        c += 1

    # data
    for line in enumerate(reader):
        i = 0
        context = {}
        for placeholder in line[1]:
            context[m[i]] = placeholder
            i += 1

        # template docx
        doc = DocxTemplate('template.docx')
        doc.render(context)
        doc.save(output)

