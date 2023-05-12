import os
import glob
import json
from typing import List, Tuple

if os.name == "nt":  # Windows
    slash = "\\"
else:  # Linux or other Unix-like systems
    slash = "/"

def get_info(path=os.getcwd()):
    """
    Returns a dictionary of dictionaries containing file information recursively for a given path or current working directory.
    :param path: Optional parameter for the path to start from. Default is current working directory.
    :return: A dictionary of dictionaries containing file information.
    """
    
    # If path is a relative path, append it to the current working directory
    if path[0] == '.':
        path = os.getcwd() + slash + path

    # Create a dictionary to store the file information for the given path
    files_dict = {"path": path.replace("\\", "/")}

    # Call the recursive function to get information about files and directories
    files_dict["files"], files_dict["size"] = get_info_recursive(path)

    # Return the dictionary of dictionaries containing file information
    return files_dict
    

def get_info_recursive(path: str) -> Tuple[List[dict], int]:
    """
    Recursively retrieves file information for a given path.

    Args:
        path (str): The path to start from.

    Returns:
        Tuple[List[dict], int]: A tuple containing a list of dictionaries with file information and the total size of all files.
    """

    files: List[dict] = []

    # Iterate over all files and directories in the given path recursively
    for file in glob.glob(path + '/**', recursive=False):
        file_dict: dict = {"path": file.replace("\\", "/"), "size": os.path.getsize(file)}

        # If the file is a directory, recursively call the function to get information about its files and directories
        if os.path.isdir(file):
            file_dict['files'], file_dict['size'] = get_info_recursive(file)

        files.append(file_dict)

    # Calculate the total size of all files in the given path and its subdirectories
    total_size: int = sum([f['size'] for f in files])

    return files, total_size
    

if __name__ == "__main__":
    # Call the function with a specific path and print the resulting dictionary of dictionaries
    files = get_info()
    print(json.dumps(files, indent=4))
