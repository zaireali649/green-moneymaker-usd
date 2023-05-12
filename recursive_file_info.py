import os
import glob
import json

def get_info(path='*'):
    """
    Returns a list of dictionaries containing file information recursively for a given path or current working directory.
    :param path: Optional parameter for the path to start from. Default is current working directory.
    :return: A list of dictionaries containing file information.
    """
    
    # If path is not specified or is "*", use the current working directory
    if path == "*":
        path = os.getcwd()
    
    # If path is a relative path, append it to the current working directory
    elif path[0] == '.':
        path = os.path.join(os.getcwd(), path)

    if os.name == "nt":  # Windows
        slash = "\\"
    else:  # Linux or other Unix-like systems
        slash = "/"
    
    # Create an empty list to store file information
    files_list = []

    # Iterate over all files and directories in the given path recursively
    for file in glob.glob(path + slash + '**', recursive=True):

        # Get the size of the file in bytes
        file_size = os.path.getsize(file)

        # Create a dictionary containing the file path and size
        file_dict = {"path": file.replace("\\", "/"), "size": file_size}

        # Append the dictionary to the list of files
        files_list.append(file_dict)

    # Return the list of dictionaries containing file information
    return files_list

if __name__ == "__main__":
    # Call the function with a relative path and print the resulting list of dictionaries
    files = get_info('../boto3_python_scripts')
    print(json.dumps(files, indent=4))
