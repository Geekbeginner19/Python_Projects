# 🧩 DAILY PYTHON PROJECT — DAY 1 (BASIC → SOLID FOUNDATIONS)
# 📌 Project Title
# CLI Contact Book (OOP Edition)

import os
import json
filename = r"C:\Users\Rarissime\Downloads\CLI_Contact_Book.json"

class Contact:
    def __init__(self, name, phone, email):
        #Name validation
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        
        #Phone Validation
        if not phone.isdigit():
            raise ValueError("Phone number must contain digits only")
        
        self.name = name.strip()
        self.phone = phone
        self.email = email
    
    def to_dict(self):
        return{
            "name" : self.name,
            "phone" : self.phone,
            "email" : self.email
        }
    
    def display(self):
        print(f"Name: {self.name} | Phone: {self.phone} | Email:{self.email}")


# cnc = Contact("Kelvin", "0558096543", "oforikelvin71@gmail.com")
# print(cnc.to_dict())

class ContactBook:
    def __init__(self):
        self.contactLst = []
        self.jsonLst = []
    
    def add_contact(self, contact):
        self.contactLst.append(contact)
    
    def view_all_contact(self):
        if len(self.contactLst) == 0:
            print("No Contacts to View")
            return
        print("===== Contact List ======")
        for contact in self.contactLst:
            contact.display()
    
    def search_contact(self, name):
        if len(self.contactLst) == 0:
            print("No Contacts to Search")
            return
        found = False
        for contact in self.contactLst:
            if name.lower() in contact.name.lower(): #Partial Search
                contact.display()
                found = True
        if not found:
            print("No Match found")   

    def delete_contact(self, name):
        found = False
        for contact in self.contactLst:
            if name.lower() == contact.name.lower():
                self.contactLst.remove(contact)
                found = True
                break
        if not found:
            print("No Match found") 

    def jsondump(self):
        self.jsonLst = [] #clearing json list everytime I save prolly to prevent saving duplicates
        if len(self.contactLst) != 0:
            for contact in self.contactLst: #Loops through contact list
                self.jsonLst.append(contact.to_dict()) #adds all dictionary formatted contacts to the json list for saving
            with open(filename, "w") as file: #save opening & closing of json files
                json.dump(self.jsonLst, file, indent = 4) #saves with a neatly formatted values
            print("\nContact Saved Successfully!")
        else:
            print("\nNo Contacts Available")
    
    def jsonload(self):
        if os.path.exists(filename): #Checks if the contact json file path exists
            with open(filename , "r") as file: #Safe opening
                loaded_list = json.load(file)#Load it into a new list
            self.contactLst = [] #Clear contact list
            for data in loaded_list:
                contact_obj = Contact(data["name"], data["phone"], data["email"])
                self.contactLst.append(contact_obj)
            print("\nContacts Loaded Successfully!")
        else:
            print("\nNo Contacts to show")

#Create a ContactBook object
contactbook = ContactBook()

#Create Contact
def create_contact():
    while True:
        try:       
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            return Contact(name, phone, email)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")

#Main Menu
while True:
    print("\n=== CLI Contact Book with Persistence ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Save Contact")
    print("6. Load Contact")
    print("7. Quit\n")
    option = input("Choose an option >>> ")

    try:
        option = int(option)
        if option < 1 or option > 7:
            print("Invalid option entered")
        else:
            if option == 1:
                contact = create_contact()
                contactbook.add_contact(contact)
                contactbook.jsondump() #Saves after contact is entered
            elif option == 2:
                contactbook.view_all_contact()
            elif option == 3:
                name = input("Enter the name of the contact: ")
                contactbook.delete_contact(name)
                contactbook.jsondump()
            elif option == 4:
                name = input("Enter the name of the contact: ")
                contactbook.search_contact(name)
            elif option == 5:
                contactbook.jsondump()
            elif option == 6:
                contactbook.jsonload()
            elif option == 7:
                print("Goodbye!\n")
                break
    except ValueError as V:
        print(f"Invalid Option entered {V}")