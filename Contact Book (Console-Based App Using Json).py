# 🔥 Python Project of the Day:

# 🧾 Contact Book (Console App)
# 🎯 Goal:
# Create a simple Contact Book that allows users to add, view, search, and delete contacts — 
# and saves everything in a file so the data isn’t lost.

# 🧱 Requirements:
# When the program runs, show this menu:

# --- Contact Book ---
# 1. Add a new contact
# 2. View all contacts
# 3. Search for a contact
# 4. Delete a contact
# 5. Quit

# ⚙️ Features:
# 1. Add a new contact
# Ask for Name, Phone Number, and Email.
# Save each contact as a dictionary and store them in a list.
# Write all contacts to a file named contacts.json using json.dump().

# 2. View all contacts
# Read all contacts from contacts.json and print them neatly:
# Name: John Doe | Phone: 0551234567 | Email: john@example.com

# 3. Search for a contact
# Ask for a name (or partial name).
# Show all contacts that match (case-insensitive).

# 4. Delete a contact
# Ask for the contact name.
# If it exists, remove it and save the updated list back to contacts.json.

# 5. Quit
# Exit the program gracefully.

import os
import json

filename = r"C:\Users\Rarissime\Downloads\Contacts.json"
contactList = []

def add_new_contact():
    contactDict = {}
    name = input("Please enter your name: ").lower()
    phone = input("Please enter your contact: ").lower()
    email = input("Please enter your email: ").lower()
    contactDict.update({"name" : name})
    contactDict.update({"phone" : phone})
    contactDict.update({"email" : email})
    if os.path.exists(filename):#checking if the json file already exist
        with open(filename, "r") as file:#reads contacts in file as 'file'
            contactList = json.load(file)#loads all contacts into
    else:
        contactList = []
    contactList.append(contactDict)#Putting the whole dictionary into a list (only way it can be converted to a json format)
    with open(filename, "w") as file:
        json.dump(contactList, file, indent = 4) #Converting or writing the list into a json file (Contacts.json) indent = 4 fives it some nice indentaation



def view_all_contacts():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            contacts = json.load(file)
        for contact in contacts:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
    else:
        print("No Contacts to View.")
    
    

def search_contact():
    if os.path.exists(filename):
        search = input("Please enter the name you want to search: ").lower()
        with open(filename, "r") as file:
            LoadedContactsList = json.load(file)
        found = False
        for contact in LoadedContactsList:
            if search.lower() == contact['name'].lower():
                print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
                found = True
            else:
                continue
        if not found:
            print("Couldn't find a match.")
    else:
        print("No contacts to View")


#def delete_contact():
    #to be continued


# add_new_contact()
# view_all_contacts()
search_contact()
