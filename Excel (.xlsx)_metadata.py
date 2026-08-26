import os
import csv #-->For csv loading
from openpyxl import load_workbook
folder = "."
all_files = os.listdir(folder)
xlsx_files = []
for file in all_files:
    if file.endswith(".xlsx"):
        xlsx_files.append(file)
with open("excel_output.csv", "w", newline="") as csv_file: #excel_output.csv is the output
    # We open the file as csv_file
    #And create a writer in csv_file
    writer = csv.writer(csv_file)
    writer.writerow(["Filename", "Creator", "Title", "Created", "Sheets"]) #-->Just a function
    for xlsx in xlsx_files:
        filepath = os.path.join(folder, xlsx)
        wb = load_workbook(filepath)
        props = wb.properties
        if props.creator:
            creator = props.creator
        else:
            creator = "Unknown"
        if props.title:
            title = props.title
        else:
            title = "Unknown"
        if props.created:
            created = props.created
        else:
            created = "Unknown"
        sheets = len(wb.sheetnames)
        writer.writerow([xlsx, creator, title, created, sheets])
        print(f"Added: {xlsx}")

print("\n✅ Done! Results saved to excel_output.csv")
