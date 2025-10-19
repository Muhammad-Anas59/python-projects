from PyPDF2 import PdfMerger
import os
folder_path = input("Enter the folder path containing PDFs: ").strip()
merger = PdfMerger()
os.chdir(folder_path)
files = [f for f in os.listdir() if f.lower().endswith(".pdf")]
for pdf in files:
    print(f"Adding: {pdf}")
    merger.append(pdf)
merger.write("Merged.pdf")
merger.close()
print("✅ All PDFs merged successfully!")
print(f"📂 Merged file saved in: {folder_path}")
