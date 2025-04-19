from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_pdf_buffer(context):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    # Заголовок
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 800, "Электронный билет")

    # Информация о билете
    y = 750
    for key, value in context.items():
        if key != 'qr_data':
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, y, f"{key}: {value}")
            y -= 30
    pdf.save()
    buffer.seek(0)
    return buffer