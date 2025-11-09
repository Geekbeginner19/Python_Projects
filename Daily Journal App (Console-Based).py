# 🔥 Python Project of the Day:
# 📅 Project: Daily Journal App (Console-Based)

# Goal: Create a small journaling app where the user can write short daily notes that get saved to a file
# (so they persist even after the program closes).
# 🧱 Requirements:
# When the program starts, show this menu:
# 1. Write a new journal entry
# 2. View all entries
# 3. Search entries by keyword
# 4. Quit


# Writing a new entry:
# Ask the user for a short title.
# Ask for the main text of the entry.
# Save it with today’s date to a text file (journal.txt).

# Viewing all entries:
# Read all saved entries from journal.txt.
# Display them clearly with title, date, and content.

# Searching entries:
# Ask for a keyword (e.g., “work”, “happy”).
# Show only the entries that contain that word (case-insensitive search).

# Quit option:
# Display a “Goodbye!” message and end the program gracefully.

import datetime as dt 
import os

currentDate = dt.date.today()#Pulling the current date from the datetime module
print(f"{currentDate}")

fileName = r"C:\Users\Rarissime\Downloads\journal.txt" #Test File
accessmode = "a"#Access mode set as Append to ensure persistence (Creates a new file if file doesn't exist)
file = open(fileName, accessmode)#Opening the file in append mode

def journal_entry():
    journalEntry = {}
    title = input("Please enter a short title for your journal entry: ").lower()
    entry = input("Please make today's entry: ").lower()
    journalEntry.update({title : entry})
    Date = currentDate
    file.write(f"\n\n[{Date}] - ")#Writing the date into the file
    for ttle, content in journalEntry.items():
        file.write(f"{ttle.upper()}\n{content}\n")#Writing the Content into the file
    file.close()#Files should always be closed after opening — otherwise, they can lock or not save properly.
    print("File Written Successfully!")

def view_all_entries():
    if os.stat(fileName).st_size == 0:#Checking if the file is empty using os.stat()
        print("File is Empty.")
    else:
        accessmode = "r"
        file = open(fileName, accessmode)
        fileContent = file.read()
        print(fileContent)
        file.close()#Files should always be closed after opening — otherwise, they can lock or not save properly.

def keywordSearch():
    if os.stat(fileName).st_size == 0:#Checking if the file is empty using os.stat()
        print("File is empty.")
    else:
        keywrd = input("Please enter a keyword to search: ").lower()
        accessmode = "r"
        file = open(fileName, accessmode)
        found = False
        for line in file:#looping through all lines in the file
            if keywrd in line.lower():#checking for the keywrd entered while converting contents of file to lowercase for more accurate search
                print(line)#displaying the entire line that has that keyword
                found = True
            else:
                continue
        if not found:#If the keyword doesn't match any word inside the file
            print("No entries matched your search\n")
        file.close()#Files should always be closed after opening — otherwise, they can lock or not save properly.

while True:
    option = input("--- Daily Journal ---\n1.Write a new journal entry.\n2.View all entries.\n3.Search entries by keyword.\n4.Quit.\n\nChoose an option>>> ")
    try:
        option = int(option)
        if option < 1 or option > 4:
            print("Please enter a valid range of options.")
        else:
            if option == 1:
                journal_entry()
            elif option == 2:
                view_all_entries()
            elif option == 3:
                keywordSearch()
            elif option == 4:
                print("Goodbye")
                file.close()
                break
    except:
        print("Please enter a valid option(No Alphabets)")

