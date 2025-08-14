from PyPDF2 import PdfReader, PdfWriter
import os

pdf_name = input("Enter PDF name (with or without .pdf): ").strip()
if not pdf_name.lower().endswith(".pdf"):
    pdf_name += ".pdf"

if not os.path.exists(pdf_name):
    print("❌ File not found!")
    exit()

start = int(input("Enter start page number: ")) - 1  # PyPDF2 uses 0-based indexing
end = int(input("Enter end page number: "))

reader = PdfReader(pdf_name)
writer = PdfWriter()

for i in range(start, end):
    writer.add_page(reader.pages[i])

output_filename = f"split_{start+1}_to_{end}.pdf"
with open(output_filename, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"✅ Pages {start+1} to {end} saved as '{output_filename}'")
