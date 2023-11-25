import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font(family="Times", size=16, style="B")

for filepath in filepaths:
    df = pd.read_csv(filepath)

    with open(filepath, "r") as file:
        content = file.read()

    title = Path(filepath).stem.capitalize()
    pdf.add_page()
    pdf.cell(w=0, h=0, txt=f"{title}", border=0, ln=1)
    pdf.multi_cell(w=0, h=10, txt=content)
    





pdf.output("output.pdf")
