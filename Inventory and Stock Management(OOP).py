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
        
item = Item("Sugar", 35, 200)
item.add_stock(200)
item.display()
item.reduce_stock(350)
item.display()
        
#Mini Project One done!
#TO BE CONTINUED