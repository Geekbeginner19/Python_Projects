# 🔐 Daily Python Project: Password Manager (OOP + File Storage)

# A beginner-friendly but very real project.

# Concept

# Build a simple password manager where a user can:
# Add a website + username + password
# View saved passwords
# Search for a website
# Save data to a file (JSON or text—your choice)
# Use classes to keep things organized

# import json
# import os

# class Credential:
#     def __init__(self, website, username, password):
#         self.website = website
#         self.username = username
#         self.password = password

#     def credentials_to_dict(self):
#         return {
#             "website": self.website,
#             "username": self.username,
#             "password": self.password
#         }

#     def display(self):
#         print(f"Website: {self.website} | Username: {self.username} | Password: {self.password}")


# class PasswordManager:
#     def __init__(self, filePath):
#         self.filePath = filePath
#         self.credentials = []
#         self.load()   # Load data automatically at start

#     def add_credential(self, credential):
#         self.credentials.append(credential)
#         print("Credential added successfully.")

#     def search(self, website):
#         website = website.lower()
#         found = False
#         for cred in self.credentials:
#             if cred.website.lower() == website:
#                 cred.display()
#                 found = True
#         if not found:
#             print("No record found for that website.")

#     def view_all(self):
#         if not self.credentials:
#             print("No stored credentials yet.")
#             return

#         for cred in self.credentials:
#             cred.display()

#     def save(self):
#         data = [cred.credentials_to_dict() for cred in self.credentials]
#         with open(self.filePath, "w") as file:
#             json.dump(data, file, indent=4)
#         print("All credentials saved.")

#     def load(self):
#         if not os.path.exists(self.filePath):
#             return  # no file yet

#         with open(self.filePath, "r") as file:
#             try:
#                 data = json.load(file)
#                 for item in data:
#                     cred = Credential(
#                         item["website"],
#                         item["username"],
#                         item["password"]
#                     )
#                     self.credentials.append(cred)
#             except json.JSONDecodeError:
#                 pass  # file empty or corrupted

# manager = PasswordManager(r"C:\Users\Rarissime\Downloads\passwords.json")

# while True:
#     print("\n--- Password Manager ---")
#     print("1. Add Credential")
#     print("2. View All Credentials")
#     print("3. Search Credential")
#     print("4. Save")
#     print("5. Quit")

#     choice = input("Choose an option >>> ")
#     try:
#         choice = int(choice)        
#         if choice < 1 or choice > 5:
#             print("Enter a valid range")
#         else:
#             if choice == 1:
#                 site = input("Website: ")
#                 user = input("Username: ")
#                 pw = input("Password: ")
#                 cred = Credential(site, user, pw)
#                 manager.add_credential(cred)
#             elif choice == 2:
#                 manager.view_all()
#             elif choice == 3:
#                 site = input("Enter website to search: ")
#                 manager.search(site)
#             elif choice == 4:
#                 manager.save()
#             elif choice == 5:
#                 manager.save()
#                 print("Goodbye!")
#                 break
#     except ValueError as V:
#         print(f"Invalid option. {V}")

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

# --------- OOP Core Classes ---------
class Credential:
    def __init__(self, website: str, username: str, password: str):
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        return {"website": self.website, "username": self.username, "password": self.password}

    @classmethod
    def from_dict(cls, d):
        return cls(d["website"], d["username"], d["password"])

    def __repr__(self):
        return f"Credential(website={self.website!r}, username={self.username!r})"


class PasswordManager:
    def __init__(self, filepath="C:/Users/Rarissime/Downloads/passwords.json"):
        self.filepath = filepath
        self.credentials: list[Credential] = []
        self.load()

    def add_credential(self, cred: Credential):
        self.credentials.append(cred)

    def search(self, website: str) -> list:
        website = website.lower().strip()
        return [c for c in self.credentials if website in c.website.lower()]

    def delete_by_index(self, index: int):
        if 0 <= index < len(self.credentials):
            self.credentials.pop(index)

    def all_websites(self) -> list:
        return [c.website for c in self.credentials]

    def save(self):
        data = [c.to_dict() for c in self.credentials]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.filepath):
            self.credentials = []
            return
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            self.credentials = [Credential.from_dict(d) for d in data]
        except (json.JSONDecodeError, KeyError):
            # If file corrupted or unexpected format, start fresh but warn
            self.credentials = []
            # don't raise — keep program usable


# --------- GUI Class ---------
class PasswordManagerGUI:
    def __init__(self, root: tk.Tk, manager: PasswordManager):
        self.root = root
        self.manager = manager
        self.root.title("Password Manager")
        self.root.geometry("700x420")
        self.root.resizable(False, False)

        # Top frame: input fields
        top = ttk.Frame(root, padding="10 10 10 0")
        top.pack(fill=tk.X)

        ttk.Label(top, text="Website:").grid(column=0, row=0, sticky=tk.W)
        self.website_var = tk.StringVar()
        self.website_entry = ttk.Entry(top, width=30, textvariable=self.website_var)
        self.website_entry.grid(column=1, row=0, sticky=tk.W, padx=5)

        ttk.Label(top, text="Username:").grid(column=2, row=0, sticky=tk.W, padx=(10, 0))
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(top, width=25, textvariable=self.username_var)
        self.username_entry.grid(column=3, row=0, sticky=tk.W, padx=5)

        ttk.Label(top, text="Password:").grid(column=0, row=1, sticky=tk.W, pady=(8, 0))
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(top, width=30, textvariable=self.password_var, show="*")
        self.password_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=(8, 0))

        # Show/hide password checkbox
        self.show_pw_var = tk.BooleanVar(value=False)
        def toggle_pw():
            self.password_entry.config(show="" if self.show_pw_var.get() else "*")
        show_pw = ttk.Checkbutton(top, text="Show", variable=self.show_pw_var, command=toggle_pw)
        show_pw.grid(column=1, row=1, sticky=tk.E, padx=(0, 5))

        # Buttons for add/save/search
        btn_frame = ttk.Frame(root, padding="10 5 10 5")
        btn_frame.pack(fill=tk.X)

        add_btn = ttk.Button(btn_frame, text="Add Credential", command=self.add_credential)
        add_btn.grid(column=0, row=0, padx=5, pady=5)

        save_btn = ttk.Button(btn_frame, text="Save", command=self.manager.save)
        save_btn.grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(btn_frame, text="Search:").grid(column=2, row=0, padx=(20, 0))
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(btn_frame, textvariable=self.search_var, width=30)
        search_entry.grid(column=3, row=0, padx=5)
        search_btn = ttk.Button(btn_frame, text="Go", command=self.search)
        search_btn.grid(column=4, row=0, padx=5)

        # Middle frame: list of websites and details
        middle = ttk.Frame(root, padding="10")
        middle.pack(fill=tk.BOTH, expand=True)

        # Listbox
        list_frame = ttk.Frame(middle)
        list_frame.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(list_frame, text="Saved Websites:").pack(anchor=tk.W)
        self.listbox = tk.Listbox(list_frame, height=15, width=35)
        self.listbox.pack(side=tk.LEFT, fill=tk.Y, padx=(0,5))
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Details panel
        details_frame = ttk.Frame(middle, padding=(15,0))
        details_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        ttk.Label(details_frame, text="Details:", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W)
        self.details_text = tk.Text(details_frame, width=45, height=12, state=tk.DISABLED)
        self.details_text.pack(fill=tk.BOTH, expand=True)

        # Bottom frame: remove, view all, quit
        bottom = ttk.Frame(root, padding="10")
        bottom.pack(fill=tk.X)

        view_all_btn = ttk.Button(bottom, text="View All", command=self.view_all)
        view_all_btn.pack(side=tk.LEFT, padx=5)

        delete_btn = ttk.Button(bottom, text="Delete Selected", command=self.delete_selected)
        delete_btn.pack(side=tk.LEFT, padx=5)

        quit_btn = ttk.Button(bottom, text="Quit", command=self.on_quit)
        quit_btn.pack(side=tk.RIGHT, padx=5)

        # populate listbox with loaded data
        self.populate_listbox()

    # -------- GUI helper methods --------
    def populate_listbox(self, items=None):
        """Populate listbox. If items provided, use that (list of Credential)."""
        self.listbox.delete(0, tk.END)
        if items is None:
            items = self.manager.credentials
        for c in items:
            self.listbox.insert(tk.END, c.website)

    def add_credential(self):
        website = self.website_var.get().strip()
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not website or not username or not password:
            messagebox.showwarning("Missing data", "Please fill Website, Username and Password.")
            return

        cred = Credential(website, username, password)
        self.manager.add_credential(cred)
        self.populate_listbox()
        # clear fields
        self.website_var.set("")
        self.username_var.set("")
        self.password_var.set("")
        messagebox.showinfo("Added", f"Credential for {website} added.")

    def view_all(self):
        self.populate_listbox()
        self.clear_details()

    def search(self):
        key = self.search_var.get().strip()
        if not key:
            messagebox.showinfo("Search", "Please enter a search keyword.")
            return
        results = self.manager.search(key)
        if not results:
            messagebox.showinfo("Search", "No matches found.")
            return
        self.populate_listbox(results)
        self.clear_details()

    def on_select(self, event):
        selected = self.listbox.curselection()
        if not selected:
            return
        index = selected[0]
        website = self.listbox.get(index)
        # Find the actual credential with matching website and index in current display
        # We must map index -> credential in current list display.
        # We'll reconstruct which credentials are currently shown in listbox
        shown_websites = [self.listbox.get(i) for i in range(self.listbox.size())]
        # Find the position of the website in the manager's list by matching names in order
        # To be robust with search/list subsets, we will search credentials in manager in same order.
        creds_shown = [c for c in self.manager.credentials if c.website in shown_websites]
        if index < len(creds_shown):
            cred = creds_shown[index]
            self.show_details(cred)
        else:
            # fallback: linear search by website exact match
            for c in self.manager.credentials:
                if c.website == website:
                    self.show_details(c)
                    return

    def show_details(self, cred: Credential):
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete("1.0", tk.END)
        self.details_text.insert(tk.END, f"Website: {cred.website}\n")
        self.details_text.insert(tk.END, f"Username: {cred.username}\n")
        self.details_text.insert(tk.END, f"Password: {cred.password}\n")
        self.details_text.config(state=tk.DISABLED)

    def clear_details(self):
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete("1.0", tk.END)
        self.details_text.config(state=tk.DISABLED)

    def delete_selected(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Delete", "No item selected.")
            return
        idx = selected[0]
        # map index to credential like in on_select
        shown_websites = [self.listbox.get(i) for i in range(self.listbox.size())]
        creds_shown = [c for c in self.manager.credentials if c.website in shown_websites]
        if idx < len(creds_shown):
            # find index in full manager.credentials
            cred = creds_shown[idx]
            full_index = self.manager.credentials.index(cred)
            if messagebox.askyesno("Confirm Delete", f"Delete credential for '{cred.website}'?"):
                self.manager.delete_by_index(full_index)
                self.populate_listbox()
                self.clear_details()
                messagebox.showinfo("Deleted", "Credential deleted.")
        else:
            messagebox.showerror("Error", "Could not delete the selected item.")

    def on_quit(self):
        try:
            self.manager.save()
        except Exception:
            pass
        self.root.destroy()


# -------- Main start ----------
if __name__ == "__main__":
    manager = PasswordManager(r"C:\Users\Rarissime\Downloads\passwords.json")
    root = tk.Tk()
    app = PasswordManagerGUI(root, manager)
    root.mainloop()
