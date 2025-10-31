'''
🧩 Project Description:
You’re going to build a small program that organizes all the files in a given folder automatically.

For example:
If your “Downloads” folder contains:

    photo.png
    music.mp3
    document.pdf
    video.mp4


Your program will automatically create folders:

    Images/
    Music/
    Documents/
    Videos/

and move each file into the correct one.

🛠️ Requirements:

Ask the user for a folder path (or let them use a default folder like “Downloads”).
Scan all files in that folder.
Check each file’s extension (e.g., .jpg, .pdf, .mp3).

Move files into category folders:
    Images → .png, .jpg, .jpeg
    Documents → .pdf, .docx, .txt
    Music → .mp3, .wav
    Videos → .mp4, .mov, .avi
    Others → everything else

If a folder doesn’t exist, create it automatically.

💡 Bonus Challenge (Optional):
Let the user choose whether to copy or move the files.
Add a summary at the end:
    “3 images, 2 documents, and 1 video moved successfully.”
'''
import os
import shutil

'''
TESTING....
x = os.listdir(path = "C:/Users/Rarissime/Downloads")
for extensions in x:
    os.path.splitext(extensions)
    if ".png" in extensions:
        print(extensions)
  
parent_folder = "C:/Users/Rarissime/Downloads"
small_folder = "test1"
path = os.path.join(parent_folder, small_folder)

if not os.path.exists(path):
    os.mkdir(path)
    print("espass through")
else:
    print("Folder already dey bro")

path2 = "C:/Users/Rarissime/Downloads/test1"
os.rmdir(path2)
'''

print("Hello, I've built a small program that organises files in a given folder automatically\n")
data_valid = False
#Error handling against numbers
while data_valid == False:
    userPath = input("Please enter the path or Type 'yes' to use your PC's main downloads folder: ").lower()
    try:
        userPath = int(userPath)
        print("Numbers are not allowed.")
    except:
        data_valid = True 

if (userPath.lower() == "yes"):
    path = "C:/Users/Rarissime/Downloads"
else:
    path = userPath

music_folder = "music"
images_folder = "images"
others_folder = "others"

creatMusicFolder = os.path.join(path, music_folder)
createImagesFolder = os.path.join(path, images_folder)
createOthersFolder = os.path.join(path, others_folder)

Documents = "C:/Users/Rarissime/Downloads/Documents"

def moveFiles(): #Function to handle moving the files
    folderContents = os.listdir(path) #Listing contents in the directory
    for file in folderContents: #looping through the contents in the directtory
        if os.path.isdir(os.path.join(path, file)): #ignores all folders if any in the directory
            continue
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):#checking for extensions in files
            if not os.path.exists(createImagesFolder):#checking if the image folder doesn't exist
                os.mkdir(createImagesFolder)#creating the folder if it doesn't
                shutil.move((f"{path}" + "/" + file), (createImagesFolder))#moving image files to the created folder
            else:
                #print("Folder for Images Already exist")
                shutil.move((f"{path}" + "/" + file), (createImagesFolder))
        elif(file.lower().endswith((".mp3", ".wav"))):
            if not os.path.exists(creatMusicFolder):
                os.mkdir(creatMusicFolder)
                shutil.move((f"{path}" + "/" + file), (creatMusicFolder))
            else:
                #print("Folder for Music Already Exists")
                shutil.move((f"{path}" + "/" + file), (creatMusicFolder))
        elif(file.lower().endswith((".docx", ".xlsx", ".pptx", ".pdf"))):
                if not os.path.exists(Documents):
                    os.mkdir(Documents)
                    shutil.move((f"{path}" + "/" + file), (Documents))
                else:
                    shutil.move((f"{path}" + "/" + file), (Documents))
        else:
            if not os.path.exists(createOthersFolder):
                os.mkdir(createOthersFolder)
                shutil.move((f"{path}" + "/" + file), (createOthersFolder))
            else:
                #print("Folder for Other files already exists")
                shutil.move((f"{path}" + "/" + file), (createOthersFolder))

                
def copyFiles():#Function to handle copying the files
    folderContents = os.listdir(path)#Listing contents in the directory
    for file in folderContents:#looping through the contents in the directtory
        if os.path.isdir(os.path.join(path, file)):#ignores all folders if any in the directory
            continue
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):#checking for extensions in files
            if not os.path.exists(createImagesFolder):#checking if the image folder doesn't exist
                os.mkdir(createImagesFolder)#creating the folder if it doesn't
                shutil.copy((f"{path}" + "/" + file), (createImagesFolder))#copying image files to the created folder
            else:
                #print("Folder for Images Already exist")
                shutil.copy((f"{path}" + "/" + file), (createImagesFolder))
        elif(file.lower().endswith((".mp3", ".wav"))):
            if not os.path.exists(creatMusicFolder):
                os.mkdir(creatMusicFolder)
                shutil.copy((f"{path}" + "/" + file), (creatMusicFolder))
            else:
                #print("Folder for Music Already Exists")
                shutil.copy((f"{path}" + "/" + file), (creatMusicFolder))
        elif(file.lower().endswith((".docx", ".xlsx", ".pptx", ".pdf"))):
                if not os.path.exists(Documents):
                    os.mkdir(Documents)
                    shutil.copy((f"{path}" + "/" + file), (Documents))
                else:
                    shutil.copy((f"{path}" + "/" + file), (Documents))
        else:
            if not os.path.exists(createOthersFolder):
                os.mkdir(createOthersFolder)
                shutil.copy((f"{path}" + "/" + file), (createOthersFolder))
            else:
                #print("Folder for Other files already exists")
                shutil.copy((f"{path}" + "/" + file), (createOthersFolder))

data_valid = False
#error handling against alphabets & numbers out of range and data validation
while data_valid == False:
    copyOrMove = input("Please do you want to copy the files or move the files?\n1.Copy Files\n2.Move Files\nPlease select the option you want: ")
    try:
        copyOrMove = int(copyOrMove)
        if copyOrMove == 1:
            copyFiles()
            data_valid = True
        elif(copyOrMove == 2):
            moveFiles()
            data_valid = True
        else:
            print("Please enter a valid option.") 
    except:
        print("Alphabets are not allowed.")              
print("Your Files have been organised successfully!")




