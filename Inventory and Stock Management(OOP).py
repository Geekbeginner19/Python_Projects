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
        
    def reduce_stock(self, amount):
        if amount > 0 and amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Cannot remove more than stock quantity")
        
    def display(self):
        print(f"Stock Name: {self.name} | Price: {self.price} | Quantity: {self.quantity}")
        
# item = Item("Sugar", 35, 200)
# item.add_stock(200)
# item.display()
# item.reduce_stock(350)
# item.display()
        
#Class Composition inventoty to handle multiple item objects
class Inventory:
    def __init__(self):
        self.items = []
    
    def add_items(self, item:str):
        self.items.append(item)
    
    def remove_item(self, name:str):
        for item in self.items:
            if name.lower() == item.name.lower():
                self.items.remove(item)
            else:
                continue

    def view_all_items(self):
        for item in self.items:
            item.display()

    def search(self, name:str):
        found = False
        for item in self.items:
            if name.lower() == item.name.lower():
                item.display()
                found = True
            else:
                continue
        if not found:
            print("No match found")
    
    #Update Stock Items
    def update_item(self, name:str, price = None, quantity = None):
        for item in self.items:#looping through the item objects
            if name.lower() == item.name.lower():
                if price is not None:
                    item.price = price
                
                if quantity is not None:
                    item.quantity = quantity
            else:
                continue
            print("Successfully Updated Items!")

    
# inventory = Inventory()
# inventory.add_items(Item("Sugar", 450, 50))
# inventory.view_all_items()
# inventory.update_item("Sugar", 500, 40)
# inventory.view_all_items()

