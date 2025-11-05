# 🎵 Project: MP3 File Renamer & Sorter
# 🎯 Goal
# You’ll create a program that:
# Scans a folder for all .mp3 files.
# Renames them in a clean format (like Artist - Song Title.mp3).
# Optionally sorts/moves them into folders by artist or album.

# 💡 Concepts You’ll Learn
# os → for file handling (rename, create folders, move files).
# os.path → for working with file names and extensions.
# mutagen → to read MP3 metadata (artist, title, album).
# Loops & error handling.

import os
from mutagen.easyid3 import EasyID3

userpath = input("Please enter the path to your audio files: ")
folderpath = os.listdir(userpath)
for audio_file in folderpath:
    if audio_file.endswith(".mp3"):
        audiofilepath = os.path.join(userpath, audio_file)#path for the old audio file
        try:
            audio = EasyID3(audiofilepath)#Loads the metadata of the audio file into the AUDIO VARIABLE(artist name, song title, album name, etc.)
            artist = audio.get("artist", ["Unknown Artist"])[0]#gets the artist name
            title = audio.get("title", ["Unknown Title"])[0]#gets the title of the song
            newaudiofile = f"{artist}_{title}.mp3"#making the new audio file name
            newaudiofilepath = os.path.join(userpath, newaudiofile)#making a new path for the new audio file
            os.rename(audiofilepath, newaudiofilepath)#renaming
            print(f"✅ Renamed: {audio_file} → {newaudiofile}")
        except Exception as e:#catches any kind of error and puts it in the variable 'e'
            print(f"⚠️ Could not rename {audio_file}: {e}")

print("\n🎵 All files processed successfully!")


