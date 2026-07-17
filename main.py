#day4  Adding csv loading 
import exifread
import os
import csv

folder = "Metadata_Project"  # This is my folder in which I have worked on in vs code, if you have different name, you can ask an AI how to change this in the code.

# Now we need to find all the jpg files, as in day 3
images = []  # This will store all the jpg files, in form of a list
all_files = os.listdir(folder)  # Lists all the files in the folder.

for file in all_files:
    if file.endswith(".jpg"):
        images.append(file)  # This will store only those files in images, which end with .jpg

# Now that we talk about csv, there's a function called csv.writer that manages new lines and commas for us.
# Unlike for file.write() where we have to add everything ourselves, which is error prone

with open("csv_fileOutput.csv", "w", newline="") as csv_file:
    # We open a new file, to write csv contents into
    # Here new line ensures no extra new lines are left
    # And the csv_file is a file object, with which we can write, e.g using csv_file.write() but this will cause errors as we will have to add manual stuff

    writer = csv.writer(csv_file)  # This is a built in function and will manage, and next lines.
    # Now writer is a file object and using it we can write to our file. writer fxn creates a writer with which can write
    # writer is a writer that knows how to write csv

    # Let's introduce a new function now
    # writer.writerow([value1,value2,valueN])
    # This takes the list, joins the values with commands, adds a new line, writes to the file.
    # btw writer is an object that has the writerow function inside it (●'◡'●) and this will write a row in our original file

    writer.writerow(["Filename", "Camera", "Model", "Date", "Software"])
    # Till now our output will look something like "Filename", "Camera", "Model", "Date", "Software"

    # Now to access all the images.. recall they are all stored in images[].
    for image in images:  # images is the list with image.jpg files, keep that in mind ╰(*°▽°*)╯
        filepath = os.path.join(folder, image)

        with open(filepath, "rb") as f:
            tags = exifread.process_file(f)

            camera = tags.get("Image Make", "Unknown")
            model = tags.get("Image Model", "Unknown")
            date = tags.get("Image DateTime", "Unknown")
            software = tags.get("Image Software", "Unknown")

        writer.writerow([image, camera, model, date, software])
        print(f"Added: {image}")

print("\n Done! Results saved to csv_fileOutput.csv")

