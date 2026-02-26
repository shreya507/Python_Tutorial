import os

# Path of directory (change this to your folder path)
path = "/"

# Get directory contents
contents = os.listdir(path)

# Print each file/folder name
print("Contents of directory:")
for item in contents:
    print(item)
