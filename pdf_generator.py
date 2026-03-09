from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(articles):

    styles = getSampleStyleSheet()

    story = []

    for art in articles:

        story.append(Paragraph(art, styles['Normal']))
        story.append(Spacer(1,20))

    doc = SimpleDocTemplate("daily_news.pdf")

    doc.build(story)