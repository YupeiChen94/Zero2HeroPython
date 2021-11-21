import shutil
import os
import re

shutil.unpack_archive('C://Users//flute//PycharmProjects//Zero2Hero//Advanced//unzip_me_for_instructions.zip', 'Files/puzzle', 'zip')

# You should now see 5 folders, each with a lot of random .txt files.
# Within one of these text files is a telephone number formated ###-###-####
# Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.

puzzle_dir = 'Files/puzzle/extracted_content'
pattern = r'\s(\d{3}-\d{3}-\d{4})\s'

def get_filepaths(directory):
    # List to store full filepaths
    phone_number = 'Not found'
    file_name = 'Not found'
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join root string to filename string to create full filepath
            filepath = os.path.join(root, filename)
            # print(filepath)
            with open(filepath, 'r') as file:
                content = file.read()
                match = re.search(pattern, content)
                if match is not None:
                    phone_number = match.group(1)
                    file_name = filename
                    # print(phone_number)
                    # print(file_name)
            # Add full filepath to list of filepaths
    return phone_number, file_name


phone_number, file_name = get_filepaths(puzzle_dir)
print(phone_number)
print(file_name)

