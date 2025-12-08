import json
import os
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog


# ----------------------------------------------------
# JSON PATH FIX (works with .py and PyInstaller .exe)
# ----------------------------------------------------
def get_json_path(filename="inventory.json"):
    if hasattr(sys, "_MEIPASS"):
        # Running from PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running from the script/exe directory
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    return os.path.join(base_path, filename)


filePath = get_json_path("inventory.json")

# ----------------------------------------------------
# ITEM CLASS
# ----------------------------------------------------
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }


# ----------------------------------------------------
# INVENTORY CLASS
# ----------------------------------------------------
class Inventory:
    def __init__(self):
        self.items = []
        self.load_from_json()  # auto-load when app starts

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if name.lower() == item.name.lower():
                self.items.remove(item)
                return True
        return False

    def search(self, name):
        results = []
        for item in self.items:
            if name.lower() in item.name.lower():
                results.append(item)
        return results

    def update_item(self, name, price=None, quantity=None):
        for item in self.items:
            if item.name.lower() == name.lower():
                if price is not None:
                    item.price = float(price)
                if quantity is not None:
                    item.quantity = int(quantity)
                return True
        return False

    def save_to_json(self):
        data = [item.to_dict() for item in self.items]
        with open(filePath, "w") as f:
            json.dump(data, f, indent=4)
        return True

    def load_from_json(self):
        if os.path.exists(filePath):
            with open(filePath, "r") as f:
                data = json.load(f)
            self.items = [Item(d["name"], d["price"], d["quantity"]) for d in data]
        else:
            # Create empty file the first time
            with open(filePath, "w") as f:
                json.dump([], f)

# ----------------------------------------------------
# TKINTER APP
# ----------------------------------------------------
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory & Stock Management")

        self.inventory = Inventory()

        # UI Components
        tk.Label(root, text="Inventory Management System",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(root, text="Add Item", width=20, command=self.add_item).pack(pady=5)
        tk.Button(root, text="View Inventory", width=20, command=self.view_items).pack(pady=5)
        tk.Button(root, text="Search Item", width=20, command=self.search_item).pack(pady=5)
        tk.Button(root, text="Update Item", width=20, command=self.update_item).pack(pady=5)
        tk.Button(root, text="Remove Item", width=20, command=self.remove_item).pack(pady=5)
        tk.Button(root, text="Save Inventory", width=20, command=self.save_inventory).pack(pady=5)

        tk.Button(root, text="Quit", width=20, command=root.quit).pack(pady=15)

    # ---------------------------
    # BUTTON FUNCTIONS
    # ---------------------------
    def add_item(self):
        name = simpledialog.askstring("Item Name", "Enter item name:")
        if not name:
            return

        price = simpledialog.askfloat("Item Price", "Enter item price:")
        quantity = simpledialog.askinteger("Item Quantity", "Enter quantity:")

        self.inventory.add_item(Item(name, price, quantity))
        messagebox.showinfo("Success", "Item added successfully!")

    def view_items(self):
        if not self.inventory.items:
            messagebox.showinfo("Inventory", "No items available.")
            return

        display = ""
        for item in self.inventory.items:
            display += f"{item.name} | Price: ${item.price} | Qty: {item.quantity}\n"

        messagebox.showinfo("Inventory Items", display)

    def search_item(self):
        name = simpledialog.askstring("Search", "Enter item name:")
        if not name:
            return

        results = self.inventory.search(name)
        if not results:
            messagebox.showinfo("Search Result", "No items found.")
        else:
            display = ""
            for item in results:
                display += f"{item.name} | ${item.price} | Qty: {item.quantity}\n"
            messagebox.showinfo("Search Result", display)

    def update_item(self):
        name = simpledialog.askstring("Update", "Enter item name to update:")
        if not name:
            return

        price = simpledialog.askfloat("New Price", "Enter new price (leave blank to skip):", initialvalue=None)
        quantity = simpledialog.askinteger("New Quantity", "Enter new quantity (leave blank to skip):", initialvalue=None)

        updated = self.inventory.update_item(name, price, quantity)
        if updated:
            messagebox.showinfo("Success", "Item updated!")
        else:
            messagebox.showwarning("Error", "Item not found.")

    def remove_item(self):
        name = simpledialog.askstring("Remove", "Enter item name:")
        if not name:
            return

        removed = self.inventory.remove_item(name)
        if removed:
            messagebox.showinfo("Success", "Item removed!")
        else:
            messagebox.showwarning("Error", "Item not found.")

    def save_inventory(self):
        self.inventory.save_to_json()
        messagebox.showinfo("Saved", "Inventory saved successfully!")


# ----------------------------------------------------
# RUN APPLICATION
# ----------------------------------------------------
root = tk.Tk()
app = InventoryApp(root)
root.mainloop()
