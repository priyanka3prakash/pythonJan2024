from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_simple_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Hello, World!")
    c.save()

create_simple_pdf("simple_pdf1.pdf")