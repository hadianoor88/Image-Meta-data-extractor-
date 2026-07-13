#day2
import exifread #imports the library 
with open("metadata_Tool\photos.jpg", "rb") as file:  #file stores the image metadata
    tags = exifread.process_file(file)                #process_file stores the image metadata 
                                  
#To print only specific contents of the meta data, we use .get() function.
#Method 1 was to use e.g camera= tags["Image Make"] Looks inside tags and finds "Image Make". Give me its value. 
#This is risky because when " image make " tag will not exist the program will crash, so thats why we prefer .get() which return unknown
#It is a built in function for dictionaries.
#def get(self, key, default=None):
    # self = the dictionary (tags)
    # key = the thing you're looking for ("Image Make")
    # default = what to return if not found ("Unknown")
    
  #  if key in self:        Check if the key exists
#    return self[key]       If yes, return its value
   # else:
     #   return default
# Step 4a: Check if "Image Make" exists in tags
#if "Image Make" in tags:
    # Step 4b: If yes, return the value
   # return tags["Image Make"]  # Returns "Apple"
#else:
    # Step 4c: If no, return "Unknown"
    #return "Unknown"
 # Extract specific fields                                    #Also another thing, the keys must be same as used otherwise unknown happens
                                                              #Another way is to use this method to see the names of exact keys.
                                                                   #import exifread

                                                               #with open("photos.jpg", "rb") as file:                                                   #tags = exifread.process_file(file)
                                                            #Another way is to use this method to see the names of exact keys.
                                                               # Print ALL keys so you know what to use
                                                                 #  for tag in tags:
                                                                   # print(tag)
    software = tags.get("Image Software", "Unknown")          #Another way is to use this method to see the names of exact keys.
    date = tags.get("Image DateTime", "Unknown")  
    width = tags.get("Image Width", "Unknown")
    height = tags.get("Image Length", "Unknown")
    camera = tags.get("Image Make", "Unknown")
    model = tags.get("Image Model", "Unknown")
    
    # Print results
    print("Camera:", camera, model)
    print("Software:", software)
    print("Date:", date)
    print("Dimensions:", width, "x", height)
                                                    
                                                    


