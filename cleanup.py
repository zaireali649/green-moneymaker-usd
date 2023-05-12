import glob
import os

def delete_generated_files():
    for file in glob.glob('*.dummy'):
        print(file)
        os.remove(file)
        
delete_generated_files()