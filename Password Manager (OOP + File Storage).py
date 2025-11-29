# 🔐 Daily Python Project: Password Manager (OOP + File Storage)

# A beginner-friendly but very real project.

# Concept

# Build a simple password manager where a user can:
# Add a website + username + password
# View saved passwords
# Search for a website
# Save data to a file (JSON or text—your choice)
# Use classes to keep things organized

import json

class Credential:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password
        

    def credentials_to_dict(self):
        return {

            "Website" : self.website,
            "Username" : self.username,
            "Password" : self.password

            }

    def display(self):
        print(f"Website:{self.website} | Username:{self.username} | Password:{self.password}")
    
class passwordManager(Credential):
    def __init__(self, credentials, filePath):
        self.credentials = []
        self.filePath = filePath

    def add_credential(self, credential):
        self.credentials.append(self.credentials_to_dict)

    def search(self, website):
        for i, website in enumerate(self.credentials):
            if website["Website"] in website:
                print(f"")
            
    
    def view_all(self):
        print()
    
    def save(self):
        return
    
    def load(self):
        return
    

    
