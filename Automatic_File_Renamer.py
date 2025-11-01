'''
🧩 Project Description:
You’ll build a Python program that automatically renames multiple files in a chosen folder, following a consistent pattern.
For example, if you have these files:

photo1.png
photo2.png
photo3.png


You can rename them automatically to:
Vacation_1.png
Vacation_2.png
Vacation_3.png


This is a real-world automation task — useful for organizing photo collections, downloaded files, or datasets.

🛠️ Requirements:
Ask the user for a folder path (or default to “Downloads”).
Ask the user for a base name (e.g., “Vacation”, “Project”, etc.).
Loop through all files in that folder.
Rename each file using this format: base_name + sequential_number + original_extension

Example: Vacation_1.jpg, Vacation_2.jpg, Vacation_3.jpg
If a file with the new name already exists, skip it and show a message.
Print a summary at the end:

15 files renamed successfully.
2 files skipped (already existed).

💡 Bonus Challenge (Optional):
Let the user choose whether to rename all files or only files of a specific type (like only .jpg or .mp3).
Add an undo feature by saving the old and new file names in a .txt log file.
'''

import os

userFolderPath = input("Please enter a folder path or type 'Y' to use the default test folder: ").lower()
if userFolderPath.lower() == "y":
    folder_path = r"C:\Users\Rarissime\Downloads\TestFolder"
else:
    folder_path = userFolderPath

userBaseName = input("Please specify the base name of the file: ").lower()


def rename():
        files = os.listdir(folder_path)
        count = 1#INITIALISED iterations should always be OUTSIDE the loops if being used in loops 
        for images in files:
            base_name = f"{userBaseName}_{count}"
            old_filesPath = os.path.join(folder_path, images)
            old_files, extension = os.path.splitext(images)#to split the extensions from it various files
            new_file_name = f"{userBaseName}_{count}{extension}" #Adds up the extensions to their newly renamed files
            new_filesPath = os.path.join(folder_path, new_file_name)#Creates the path ready for renaming
            print(images)
            if images.lower().endswith((".jpg", ".png", ".jpeg", ".webp", ".jfif")):
                if os.path.exists(new_filesPath):#checking if the new files path already exists
                    continue#if it does, you skip to the next loop iteration
                else:
                    os.rename(old_filesPath, new_filesPath)
                count += 1#counts when files are renamed
            else:
                continue  
        print(f"{count - 1} files renamed successfully")
rename()


