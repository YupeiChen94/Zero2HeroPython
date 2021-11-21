import zipfile
import shutil

f = open('Files/fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('Files/filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()

# Create the compressed file archive
comp_file = zipfile.ZipFile('Files/comp_file.zip', 'w')
# Add files to the archive
comp_file.write('Files/fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('Files/filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# Extract files out of archive
zip_obj = zipfile.ZipFile('Files/comp_file.zip', 'r')
zip_obj.extract('Files/fileone.txt', 'extracted_single_content')
zip_obj.extractall('extracted_content')

# Compress entire directory using shutil
dir_to_zip = 'extracted_content'
output_filename = 'Files/directory_example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)

# Unpack archive using shutil
shutil.unpack_archive('Files/directory_example.zip', 'Files/final_unzip', 'zip')

