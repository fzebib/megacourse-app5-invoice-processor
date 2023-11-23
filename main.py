import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    filename = Path(filepath).stem
    invoice_nr, date = filename.split('-')

    pdf = FPDF(orientation="P", format="A4", unit="mm")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Nr.{invoice_nr}", ln=1)    
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{date}", ln=1)
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    #Add a header

    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70,h=8, txt=columns[1],border=1)
    pdf.cell(w=34,h=8, txt=columns[2],border=1)
    pdf.cell(w=30,h=8, txt=columns[3],border=1)
    pdf.cell(w=30,h=8, txt=columns[4],border=1, ln=1)

    #Add Rows to the table

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70,h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=34,h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30,h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30,h=8, txt=str(row["total_price"]),border=1, ln=1)


    total_sum = str(df["total_price"].sum())

    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70,h=8, txt="",border=1)
    pdf.cell(w=34,h=8, txt="",border=1)
    pdf.cell(w=30,h=8, txt="",border=1)
    pdf.cell(w=30,h=8, txt=total_sum,border=1, ln=1)


    #Add total sum sentence

    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30,h=8, txt=f"The total price is {total_sum}", ln=1)

    #Add Company Name and Logo

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=30,h=8, txt=f"Pythonhow")
    pdf.image("pythonhow.png", w=10)
    
    pdf.output(f"PDFS/{filename}.pdf")

