import os
import shutil

# Write to a text file
f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

# Get current working directory
print(os.getcwd())
# Get list of files in directory
print(os.listdir('C:\\Users'))

# Deleting a file
os.unlink('C:\\Users\\flute\\PycharmProjects\\Zero2Hero\\Advanced\\Modules\\Files\\practice.txt')
# Deleting an empty folder
# os.rmdir(path)
# Deleting files AND folders
# shutil.rmtree(path)

# Moving a file
shutil.move('practice.txt', 'C:\\Users\\flute\\PycharmProjects\\Zero2Hero\\Advanced\\Modules\\Files')
