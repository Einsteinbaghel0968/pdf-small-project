from PyPDF2 import PdfReader, PdfWriter
import os

pdf_name = input("Enter PDF name (with or without .pdf): ").strip()
if not pdf_name.lower().endswith(".pdf"):
    pdf_name += ".pdf"

if not os.path.exists(pdf_name):
    print("❌ File not found!")
    exit()

start = int(input("Start page number to rotate: ")) - 1
end = int(input("End page number to rotate: "))
rotation = int(input("Enter rotation angle (90, 180, 270): "))

reader = PdfReader(pdf_name)
writer = PdfWriter()

for i, page in enumerate(reader.pages):
    if start <= i < end:
        page.rotate(rotation)
    writer.add_page(page)

output_file = f"rotated_{start+1}_to_{end}.pdf"
with open(output_file, "wb") as f:
    writer.write(f)

print(f"✅ Rotated PDF saved as '{output_file}'")
