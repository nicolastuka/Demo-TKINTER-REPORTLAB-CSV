from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph


def CreateReport(pathToFile, data):
    c = canvas.Canvas(pathToFile, pagesize=A4)
    posX = 50
    posY = 775
    width, height = A4
    strTitle = "REGISTRO DE ASISTENCIA DEL CURSO"
    paragraphTitle = Paragraph(
        strTitle,
        style=ParagraphStyle(
            name="Titulo",
            fontName="Helvetica-Bold",
            fontSize=20,
            textColor=colors.red,
            alignment=1,
            underline=True,
        ),
    )
    paragraphTitle.wrapOn(c, width, height)
    paragraphTitle.drawOn(c, -width / 100, posY)

    posY = 720
    c.drawString(posX, posY, "")
    for d in data:
        posY -= 15
        posX = 25
        offset = 0
        posList = 0
        for elem in d:
            if posList > 0:
                if elem == "1":
                    elem = "PRESENTE"
                else:
                    elem = "AUSENTE"
            c.drawString(posX, posY, elem)
            posX = 500 - offset
            offset += 75
            posList += 1
    c.save()
