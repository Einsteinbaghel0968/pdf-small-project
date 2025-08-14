from PyPDF2 import PdfReader, PdfWriter
import os

pdf_name = input("Enter the PDF name (with or without .pdf): ").strip()
if not pdf_name.lower().endswith(".pdf"):
    pdf_name += ".pdf"

if not os.path.exists(pdf_name):
    print("❌ File not found!")
    exit()

reader = PdfReader(pdf_name)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.add_metadata(reader.metadata)

output_file = "compressed_" + pdf_name
with open(output_file, "wb") as f:
    writer.write(f)

print(f"✅ Compressed PDF saved as '{output_file}'")
