import os
import shutil
# import send2trash

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
# Sending to trash instead of permenant removal
# send2trash.send2trash(file_path)

# Moving a file
shutil.move('practice.txt', 'C:\\Users\\flute\\PycharmProjects\\Zero2Hero\\Advanced\\Modules\\Files')

# Getting files
for folder, sub_folders, files in os.walk('C:\\Users\\flute\\PycharmProjects\\Zero2Hero\\Advanced'):
    print(f"Currently looking at {folder}")
    print('The subfolders are:')
    for sub_fold in sub_folders:
        print(f'\tSubfolder: {sub_fold}')
    print('The files are:')
    for f in files:
        print(f'\t\tFiles: {f}')
