from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from datetime import datetime
from reportlab.lib.enums import TA_LEFT

def generate_pdf(kpis, summary_text, chart_paths, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=A4,
                            rightMargin=30, leftMargin=30,
                            topMargin=30, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        name="CustomBody",
        parent=styles['BodyText'],
        fontSize=11,
        leading=14
    )

    elements = []
    heading3_style = styles['Heading3']
    heading3_style.alignment = TA_LEFT

    # Title
    
    elements.append(Paragraph("📊 Weekly Report"+ datetime.now().strftime("%b %Y"), styles['Title']))
    elements.append(Spacer(1, 12))

    # Summary
    elements.append(Paragraph("Executive Summary:",heading3_style))
    elements.append(Paragraph( summary_text, custom_style))
    elements.append(Spacer(1, 12))

    # KPIs
    elements.append(Paragraph( "Key Performance Indicators (KPIs):", heading3_style))
    for key, value in kpis.items():
        elements.append(Paragraph(f"<b>{key}</b>: {value}", custom_style))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 20))

    # Add charts — try to fit them nicely on the page
    for chart_path in chart_paths:
        try:
            img = Image(chart_path)
            img.drawHeight = 3.5 * inch  # Adjust to fit on one page
            img.drawWidth = 5.5 * inch
            elements.append(img)
            elements.append(Spacer(1, 12))
        except Exception as e:
            print(f"Error adding image {chart_path}: {e}")

    # Build the PDF
    doc.build(elements)
    print(f"✅ PDF report generated: {output_file}")
