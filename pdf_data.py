#Now we add the ability to process a batch of file. 
#concepts are same as in main.py ---> for image meta data 
import os #--->a python module for getting all PDF files from folder. 
from pypdf import PdfReader
folder = "Metadata_Project"
all_files= os.listdir(folder) #To get all file names from the folder
#Now for finding / filtering only the pdf files
pdf_files=[] #Empty list to store PDFs
for file in all_files:#Loop through each file
   if file.endswith(".pdf"):# endswith is an imported or built in fxn 
      pdf_files.append(file) #Add to the list 
#Now to loop through each pdf, as we have to get and print the data of all pdf files now
for pdf in pdf_files:
   filepath = os.path.join(folder,pdf)# To get the right path to give to the function
   reader = PdfReader(filepath)
   info = reader.metadata
      if info.title:
         title = info.title
      else:
         title = "unknown"
      if info.author:
    author = info.author
else:
    author = "Unknown"
   print("File:", pdf)
print("  Title:", title)
print("  Author:", author)
print("-" * 30)
         


