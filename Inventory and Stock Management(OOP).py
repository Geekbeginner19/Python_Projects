# 🔥Daily Python OOP Project (Beginner-Friendly, Real-World, Step-by-Step)
# Project of the Day: Inventory & Stock Management System (OOP)
# This is not hard, but it will stretch your OOP thinking in a practical way.

# ✅ PROJECT CONCEPT

# You are building a small system that manages items in a store:

# Add items
# Remove items
# Update stock
# Show items
# Search items
# Save/load inventory to a JSON file
# Just like a real mini-POS (Point of Sale) system.

import json
import os

filePath = r"C:\Users\Rarissime\Downloads\InventoryManager.json"

class Item:
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name 
        self.price = price
        self.quantity = quantity
    
    def to_dict(self):
        return {
            "name" : self.name,
            "price" : self.price,
            "quantity" : self.quantity
        }

    def add_stock(self, amount:int):
        if amount > 0:
            self.quantity += amount
        else:
            print("Cannot add negative items to the stock")
        
    def reduce_stock(self, amount:int):
        if amount > 0 and amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Cannot remove more than stock quantity")
        
    def display(self):
        print(f"Stock Name: {self.name} | Price: ${self.price} | Quantity: {self.quantity}")
        
# item = Item("Sugar", 35, 200)
# item.add_stock(200)
# item.display()
# item.reduce_stock(350)
# item.display()
        
#Class Composition inventoty to handle multiple item objects
class Inventory:
    def __init__(self):
        self.items = []
        self.jsonlst = []
    
    def add_items(self, item):
        self.items.append(item)
    
    def remove_item(self, name:str):
        if len(self.items) == 0 or not os.path.exists(filePath):
            print("\nNothing to see here")
        else:               
            for item in self.items:
                if name.lower() == item.name.lower():
                    self.items.remove(item)
                else:
                    continue

    def view_all_items(self):
        if len(self.items) == 0 or not os.path.exists(filePath):
            print("Nothing to see here")
        else:    
            for item in self.items:
                item.display()

    def search(self, name:str):
        if len(self.items) == 0 or not os.path.exists(filePath):
            print("\nNothing to see here")
        else:                
            found = False
            for item in self.items:
                if name.lower() in item.name.lower(): #partial matches
                    item.display()
                    found = True
                else:
                    continue
            if not found:
                print("\nNo match found")
    
    #Update Stock Items
    def update_item(self, name:str, price = None, quantity = None):
        found = False
        if len(self.items) == 0 or not os.path.exists(filePath):
            print("\nNo inventory Available to update")
        else:
            for item in self.items:#looping through the item objects
                if name.lower() == item.name.lower():
                    if price is not None:
                        item.price = price
                    
                    if quantity is not None:
                        item.quantity = quantity
                else:
                    continue
                print("\nSuccessfully Updated Inventory!") 
            if not found:
                print("\nNo match found")
           
    
    def dumpjson(self):
        if os.path.exists(filePath):        
            self.jsonlst = []  # clear previous json list
            for item in self.items:
                self.jsonlst.append(item.to_dict())  # convert each Item object to dict
            with open(filePath, "w") as file:
                json.dump(self.jsonlst, file, indent=4)  #save
            print("\nInventory Saved Successfully!")
        else:
            print("\nNo Inventory to save")

    def loadjson(self):
        if os.path.exists(filePath):#check to see if json file exists
            with open(filePath, "r") as file:
                loaded_list = json.load(file)  # load list of dicts from JSON
            self.items = []  # clear current items
            for data in loaded_list:
                item_obj = Item(data["name"], data["price"], data["quantity"])  # convert dict back to Item Object
                self.items.append(item_obj)#Adds the objects back into the self.items list
            print("\nInventory loaded successfully!")
        else:
            print("\nNo inventory to see")
                
    
inventory = Inventory()
# inventory.add_items(Item("Sugar", 450, 50))
# inventory.view_all_items()
# inventory.update_item("Sugar", 500, 40)
# inventory.view_all_items()
# inventory.dumpjson()  # save inventory
# inventory.loadjson()  # load inventory and rebuild Item objects

def addItems():
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    return Item(name, price, quantity)

while True:
    print("\n=== Stock and Inventory Management System ===")
    print("1. Add item")
    print("2. View All Items")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. Update Item")
    print("6. Save Inventory")
    print("7. Load Inventory")
    print("8. Quit\n")
    option = input("Choose an option >>> ")

    try:
        option = int(option)
        if option < 1 or option > 8:
            print("Please enter a valid option")
        else:
            if option == 1:
                add = addItems()
                inventory.add_items(add)
                inventory.dumpjson() # saves after inventory is added 
            elif (option == 2):
                inventory.view_all_items()
            elif(option == 3):
                name = input("Enter item name: ")
                inventory.remove_item(name)
            elif(option == 4):
                name = input("Enter item name: ")
                inventory.search(name)
            elif(option == 5):
                name = input("Enter item name: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                inventory.update_item(name, price, quantity)
            elif(option == 6):
                inventory.dumpjson()
            elif(option == 7):
                inventory.loadjson()
            elif(option == 8):
                print("Goodbye!\n")
                break
    except ValueError as V:
        print(f"Invalid option entered {V}")
    
