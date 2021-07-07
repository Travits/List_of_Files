"""
Created on Mon May 25 16:25:32 2020
@author: Alex.Travisky
"""

"""
os.listdir('your_path') will list all content of a directory
os.path.isfile will check its file or not
"""

import os

#%%  Set path and get files list:
dir_path = 'C:\Temp'

# Check current work directory
try:
    os.chdir(dir_path)
    print("# Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("# Directory: {0} does not exist".format(dir_path))
except NotADirectoryError:
    print("# {0} is not a directory".format(dir_path))
except PermissionError:
    print("# You do not have permissions to change to {0}".format(dir_path))

# Get files list in current directory    
files = os.listdir(dir_path)
print("# Files in current directory:", files)   # for debug


#%%  Set work directory:
os.chdir(dir_path)

#%%  

keyword = "import"
counter = 0

for file in files:
    print("  ")
    if os.path.isfile(file):
        
        print("# File name:", file)
        
        # with open(file, "r", encoding="utf-8") as file:
        
        # with open(file, 'r') as file:
        #     for line in file:
        #         print(line.strip())
        
        
        f=open(os.path.join(dir_path,file),'r')
        file_contents = f.read()
        print(file_contents)
        
        for x in f:
            if keyword in x:
                #do what you want
                counter += 1
                
        f.close()
        
print (counter)