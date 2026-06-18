from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
import textwrap
import os

input_path = 'docs/AI_ML_Fundamentals_Report.md'
output_path = 'docs/AI_ML_Fundamentals_Report.pdf'

with open(input_path, 'r', encoding='utf-8') as f:
    lines = [line.rstrip() for line in f]

canvas = Canvas(output_path, pagesize=letter)
width, height = letter
margin = inch * 0.75
text = canvas.beginText()
text.setTextOrigin(margin, height - margin)
text.setFont('Helvetica', 12)
max_width = width - 2 * margin

for line in lines:
    if line.strip() == '---':
        text.textLine('')
        continue
    if line.startswith('# '):
        text.setFont('Helvetica-Bold', 16)
        text.textLine(line[2:].strip())
        text.setFont('Helvetica', 12)
        continue
    if line.startswith('## '):
        text.setFont('Helvetica-Bold', 14)
        text.textLine(line[3:].strip())
        text.setFont('Helvetica', 12)
        continue
    if line.startswith('### '):
        text.setFont('Helvetica-Bold', 12)
        text.textLine(line[4:].strip())
        text.setFont('Helvetica', 12)
        continue
    if line.startswith('- '):
        wrapped = textwrap.wrap(line[2:].strip(), width=90)
        if wrapped:
            text.textLine('• ' + wrapped[0])
            for cont in wrapped[1:]:
                text.textLine('  ' + cont)
        else:
            text.textLine('•')
        continue
    if line.strip() == '':
        text.textLine('')
        continue
    for wrapped_line in textwrap.wrap(line, width=95):
        text.textLine(wrapped_line)

canvas.drawText(text)
canvas.save()
print(f'Created {os.path.abspath(output_path)}')
