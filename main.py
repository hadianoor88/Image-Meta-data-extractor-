#day1
import exifread #imports the library 
with open("metadata_Tool\photos.jpg", "rb") as file:  #file stores the image metadat
    tags = exifread.process_file(file)                #process_file stores the image metadata 
    for tag in tags:                                  #tag is a variable that stores the value of keys
     print(tag, ":", tags[tag])                       #Inside the process function it looks like e.g metadata={}, an empty 
                                                      #dictionary  and we store values using the syntax metadata["key"]="term"
                                                     #and then the value is returned  


