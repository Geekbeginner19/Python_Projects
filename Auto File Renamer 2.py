#Rename all files in a given folder so that
# dog.jpg   →  dog_renamed.jpg  
# cat.png   →  cat_renamed.png  
# car.webp  →  car_renamed.webp

import os

def rename():
    folderpath = r"C:\Users\Rarissime\Downloads\TestFolder" #folder path(can be changed to whatever path)
    for files in os.listdir(folderpath):#listing the files in the folder path (ALWAYS DO THIS BEFORE ANY MANIPULATION CAN BE DONE)
        if not os.path.isdir(os.path.join(folderpath, files)):#checking to see if any content in the folder is not a directory or folder
            if "_renamed" in files:
                continue
            filename, extension = os.path.splitext(files)#splitting the filenames from it extensions
            newfilename = f"{filename}_renamed{extension}"#reattaching them to their new file names(makes them a real file btw)
            oldpath = os.path.join(folderpath,files)#joining oldpath of previous names of files
            newpath = os.path.join(folderpath, newfilename)#establishing a new path with the newly renamed files
            os.rename(oldpath, newpath)#renaming from old filename to new filename
            print(newfilename)#printing the filenames (newly renamed)
rename()#invoking the function