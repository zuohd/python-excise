import csv

'''
Read PDF file:
import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager
'''
with open("test.csv", "r") as f:
    allfileinfo = csv.reader(f)
    for row in allfileinfo:
        print(row)
