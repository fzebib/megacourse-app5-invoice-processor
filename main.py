import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    filename = Path(filepath).stem
    invoice_nr, date = filename.split('-')

    pdf = FPDF(orientation="P", format="A4", unit="mm")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Nr.{invoice_nr}", ln=1)    
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{date}")
    pdf.output(f"PDFS/{filename}.pdf")
