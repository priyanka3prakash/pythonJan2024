# pypdfminer
# pypdf2

# pip install pypdf2

import PyPDF2

def read_pdf(filename):
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.getPage(0)  # Read the first page
        text = page.extractText()
        return text

pdf_text = read_pdf('simple_pdf1.pdf')
print(pdf_text)


