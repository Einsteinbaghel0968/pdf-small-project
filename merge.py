import os
from PyPDF2 import PdfMerger

merger = PdfMerger()

while True:
    try:
        n = int(input("Enter the number of PDFs to merge: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

pdfs = []
for i in range(n):
    while True:
        name = input(f"Enter the name of PDF {i+1} (with or without .pdf): ").strip()
        if not name.lower().endswith(".pdf"):
            name += ".pdf"
        if os.path.exists(name):
            pdfs.append(name)
            break
        else:
            print("❌ File not found. Please try again.")

for pdf in pdfs:
    merger.append(pdf)

output_name = input("Enter the name for the merged PDF (without .pdf): ").strip() + ".pdf"
merger.write(output_name)
merger.close()

print(f"✅ Successfully merged {n} PDFs into '{output_name}'")
