#pip install openpyxl ---> In terminal to install excel library
#Why We Need It:
#Python cannot read Excel files by default. We need this library to:
#Open .xlsx files
#Read their metadata
#Extract author, title, dates, etc.
from openpyxl import load_workbook 
#Imports the load_workbook from the library , which will read excel files
#Now we use the variable wb to open the file test.xlsx using our function , and so wb will contain all the sheets in the excel 
#file, all the metadata in those sheets asw
wb = load_workbook("test.xlsx")
#wb is a variable that stores the workbook object 
props = wb.properties
#probs is a varibale that stores the wb properties like creation time, title, subject, created etc 
creator = props.creator #pretty self-explanatory
print("Creator:", creator)
creator = props.creator 
if props.creator:
    creator = props.creator
else:
    creator = "Unknown"
  if props.title:
    title = props.title
else:
    title = "Unknown"
print("Title:", title) 
if props.created:
    created = props.created
else:
    created = "Unknown"
  print("Created:", created)
sheets = len(wb.sheetnames) 
# wb.sheetnames ---> gets a list of all sheet names 
# len--> gets the count of how many sheets there are 
# sheets stores the count 

