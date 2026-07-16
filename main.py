#day 3
#Current code has processes files only when we put the path in its place. 
#Today we implement something so all the image images in the folder can be processed automatically
#os stands for "Operating System". It's a built-in Python module that lets you talk to your computer's file system.
#Task	Code
#List all files in a folder	os.listdir("folder_name")
#Join folder and file names	os.path.join("folder", "file.jpg")
#Check if a path exists	os.path.exists("file.txt")
#Get current working directory	os.getcwd()
#os.listdir() - The Most Important One
#What It Does:
#Returns a list of ALL files and folders in a directory.
#Syntax:
#os.listdir(folder_path)
#Breaking It Down:
#Part	Meaning
#os	The module (imported)
#.	"Look inside os"
#listdir	The function name (list directory)
#(folder_path)	The folder you want to look in
#Example:
#import os
#files = os.listdir("metadata_Tool")
#print(files)
# Output: ['photos.jpg', 'image2.jpg', 'image3.jpg', 'notes.txt']
#os.path.join() - Building Paths
#What It Does:
#Joins folder and file names into a complete path.
#Syntax:
#os.path.join(folder, filename)
#Why We Need It:
#Without os.path.join	With os.path.join
#"metadata_Tool" + "/" + "photo.jpg"	os.path.join("metadata_Tool", "photo.jpg")
#Works on Windows only	Works on ALL operating systems
#Example:
#import os
#folder = "metadata_Tool"
#file = "photo.jpg"
#full_path = os.path.join(folder, file)
#print(full_path)
# Output: "metadata_Tool/photo.jpg" (or "metadata_Tool\photo.jpg" on Windows) 
#Concept 2 
#String Methods - .endswith() 
#Syntax:
#text.endswith(suffix)
#To filter only image files:
#if filename.endswith(".jpg"):
#   print("This is a JPG file")
#else:
#    print("Not a JPG file")
#CONCEPT 3: List Comprehension
#What Is It?
#A shorter way to create lists based on conditions.
#Syntax:
#[thing for thing in list if condition]
#Breaking It Down:
#Part	Meaning
#thing	The item you want
#for thing in list	Loop through the list
#if condition	Only include if this is true
#Example - Manual Way (Long):
#all_files = ["photo.jpg", "notes.txt", "image2.jpg", "data.pdf"]
#images = []
#for file in all_files:
#    if file.endswith(".jpg"):
#       images.append(file)
#print(images)  # ['photo.jpg', 'image2.jpg']
#Example - List Comprehension (Short):
#all_files = ["photo.jpg", "notes.txt", "image2.jpg", "data.pdf"]
#images = [file for file in all_files if file.endswith(".jpg")]
#print(images)  # ['photo.jpg', 'image2.jpg']
#CONCEPT 5: len() Function
#What It Does:
#Returns the number of items in a list.
#Syntax:
#len(list)
#Example:
#images = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]
#count = len(images)
#print(f"Number of images: {count}")  # Number of images: 3
import os
import exifread

# Tell Python where your images are
folder = "metadata_Tool"

# Step 1: Get all files from the folder
all_files = os.listdir(folder)

# Step 2: Keep only .jpg files
images = []
for file in all_files:
    if file.endswith(".jpg"):
        images.append(file)

# Step 3: Show how many images found
print("Found", len(images), "images")
print("----------------------------------------")

# Step 4: Process each image
for image in images:
    # Build the full path
    filepath = folder + "/" + image
    
    # Open and read metadata
    with open(filepath, "rb") as f:
        tags = exifread.process_file(f)
    
    # Get specific fields
    camera = tags.get("Image Make", "Unknown")
    model = tags.get("Image Model", "Unknown")
    date = tags.get("Image DateTime", "Unknown")
    software = tags.get("Image Software", "Unknown")
    width = tags.get("Image Width", "Unknown")
    height = tags.get("Image Length", "Unknown")
    
    # Print results
    print("File:", image)
    print("  Camera:", camera, model)
    print("  Date:", date)
    print("  Software:", software)
    print("  Size:", width, "x", height)
    print("----------------------------------------")
