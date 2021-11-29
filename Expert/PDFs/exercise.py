import csv
import PyPDF2
import re

# Grab google drive link from csv file
data = open('find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
# print(len(data_lines))
link = ''
for idx, line in enumerate(data_lines):
    # print(data_lines[idx][idx])
    link += data_lines[idx][idx]
# print(link)

# Find phone number in the document from google drive
phone_pattern = re.compile(r'(\d{3})\.(\d{3})\.(\d{4})')
f = open('Find_the_Phone_Number.pdf', mode='rb')
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    phone = re.search(phone_pattern, text)
    if phone is not None:
        print(phone.group())
        break

f.close()
