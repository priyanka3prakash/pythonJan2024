from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def add_image_to_pdf(filename, image_path):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawImage(image_path, 100, 600, width=200, height=100)
    c.save()

add_image_to_pdf("pdf_with_image.pdf", "image.jpg")
