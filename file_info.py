import os
import glob
import json


if os.name == "nt":  # Windows
    slash = "\\"
else:  # Linux or other Unix-like systems
    slash = "/"

# Create an empty list to store file information
files = []

# Iterate over all files in the current working directory
for file in glob.glob(os.getcwd() + slash + '*'):
    
    # Create a dictionary containing the file path and size
    # Replace backslashes with forward slashes in the file path using the replace() method
    # Get the size of the file in bytes using the os.path.getsize() function
    file_dict = {"path":file.replace("\\","/"), "size":os.path.getsize(file)}
    
    # Append the dictionary to the list of files
    files.append(file_dict)

# Print the list of dictionaries containing file information
print(json.dumps(files, indent=4))
