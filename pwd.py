import os
import win32api

# Specify the directory
directory = 'C:\\Users\\Administrator\\Desktop\\'

# List files in the directory
files = win32api.FindFiles(os.path.join(directory, '*'))

# Print file names
for file in files:
    print(file)
