'''
Scenario: Rename all .txt files in a folder to follow a uniform 
format (file1.txt, file2.txt, etc.).
'''

import os

# Folder containing files
folder_path = r'C:\Users\Sanana Mwanawina\Desktop\Commercial\Tech Talks\Automation with Python\files-to-organise'

'''
Showing we get the file names in a list
print(os.listdir(folder_path))
'''
counter = 0 

# Iterate over all files in folder
for filename in os.listdir(folder_path):

    # if statement for only .txt files
    if filename.endswith('.txt'):

        # Contruct old and new paths
        old_path = os.path.join(folder_path, filename)
        new_filename = f"file{counter+1}.txt"
        new_path = os.path.join(folder_path, new_filename)

        new_path = os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}.')

        counter += 1
