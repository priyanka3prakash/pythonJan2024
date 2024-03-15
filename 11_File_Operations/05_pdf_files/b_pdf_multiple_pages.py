from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_multi_page_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    for i in range(5):
        c.drawString(100, 750 - (i * 100), f"Page {i+1}")
        c.showPage()  # Move to the next page
    c.save()

create_multi_page_pdf("multi_page_pdf.pdf")
