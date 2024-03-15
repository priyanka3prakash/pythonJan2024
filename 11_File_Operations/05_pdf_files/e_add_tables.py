from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def add_table_to_pdf(filename):
    data = [
        ['Name', 'Age', 'Gender'],
        ['John', '30', 'Male'],
        ['Alice', '25', 'Female'],
        ['Bob', '35', 'Male']
    ]
    doc = SimpleDocTemplate(filename, pagesize=letter)
    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)
    doc.build([table])

add_table_to_pdf("pdf_with_table.pdf")
