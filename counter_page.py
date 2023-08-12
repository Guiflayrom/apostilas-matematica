import PyPDF2
from glob import glob

files = glob("*.pdf")

totalpages = 0
for file in files:

	f = open(file, 'rb')
	readpdf = PyPDF2.PdfFileReader(f)
	totalpages += int(readpdf.numPages)

print(totalpages)
