# Import PdfReader from the library 
from pypdf import PdfReader 
#PdfReader is a function that creates an object. 
#An object is a thing that contains -Data and Functions
# This is what's INSIDE the library (simplified)
#def PdfReader(file_path):
   # 1. Open the file
#  file = open(file_path, "rb")
    # 2. Read the PDF data
   # pdf_data = file.read()
    # 3. Parse the PDF structure
    # Look for metadata, pages, etc.
    # 4. Create an object with all the data
   # reader_object = {
    #    "metadata": {
    #        "title": "My Document",
     #       "author": "John Doe"
      #  },
      #  "pages": ["page1", "page2"],
      #  "page_count": 2
  #  } 
    # 5. Return the object
   # return reader_object
reader = PdfReader("test.pdf")
#So up until now the function creates a reader object and returns it , which is stored 
# in reader 
#Looks like this, 
#reader = {
#    "metadata": {
#        "title": "My Document",
#        "author": "John Doe"
#    },
#   "pages": ["page1", "page2"],
 #   "page_count": 2
#}
info = reader.metadata 
#info is a variable that stores all the metadata. 
#reader.metadata is containing all the hidden PDF information
if info.title: 
  title= info.title
else:
  title="unknown"
  if info.author:
    author=info.author
  else:
    author="unknown"
pages= len(reader.pages) 
#Above one is self explanatory, just simple functions. And we assign unknown in case we dont find our terms 
print("=" * 40)
print("PDF METADATA")
print("=" * 40)
print("Title:", title)
print("Author:", author)
print("Pages:", pages)
print("=" * 40)
#the *40 is just for a like ======== this kinda output 

