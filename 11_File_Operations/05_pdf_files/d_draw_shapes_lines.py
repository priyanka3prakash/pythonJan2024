from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_shapes_and_lines(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setStrokeColorRGB(0, 0, 0.5)  # Set stroke color to blue
    c.rect(100, 700, 200, 100)  # Draw a rectangle
    c.setLineWidth(2)  # Set line width
    c.line(100, 700, 300, 800)  # Draw a line
    c.save()

draw_shapes_and_lines("pdf_with_shapes_and_lines.pdf")
