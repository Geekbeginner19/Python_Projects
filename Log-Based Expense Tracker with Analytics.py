# 🧩 WHAT YOU’RE BUILDING

# A command-line expense tracker that lets a user:

# Add expenses
# Categorize them (Food, Transport, Bills, Fun, etc.)
# Store date & amount
# Persist data using JSON
# Analyze spending patterns
# Think of it as the foundation of a real finance app.

import json
import datetime
import os
filename = r"C:\Users\Rarissime\Downloads\log-based_Tracker.json"

class Expense:
    def __init__(self, title, amount:float, category, date = None):
        self.title = title
        self.amount = amount 
        self.category = category
        self.date = date if date else datetime.datetime.now()
        
    def to_dict(self):
        return {
            "title" : self.title,
            "amount" : self.amount,
            "category" : self.category,
            "date" : self.date.isoformat()
        }
    
    def display(self):
        print(f"Title: {self.title} | Amount: ${float(self.amount)} | Category: {self.category} | Date: {self.date}")
    

# exp1 = Expense("Bread", 100, "Food")
# exp1.display()

class ExpenseManager:
    def __init__(self):
        self.expenseLst = []
        self.jsonLst = []
    
    def add_expense(self, expense):
        self.expenseLst.append(expense)
    
    def remove_expense(self, title):
        found = False
        for exp in self.expenseLst:
            if title.lower() == exp.title.lower():
                self.expenseLst.remove(exp)
                found = True
                break
        if not found:
            print("No match!")

    def view_all_expense(self):
        if len(self.expenseLst) == 0:
            print("Nothing to show here")
            return
        print("=== ALL EXPENSES ===")
        for exp in self.expenseLst:
            exp.display()

    def search_by_category(self, category):
        if len(self.expenseLst) == 0:
            print("Nothing to show here")
            return
        found = False
        for exp in self.expenseLst:
            if category.lower() in exp.category.lower():
                exp.display()
                found = True
        if not found:
            print("No match!")
    
    def jsondump(self):
        self.jsonLst = [] #clearing json list everytime I save prolly to prevent saving duplicates
        if len(self.expenseLst) != 0:
            for exp in self.expenseLst:
                self.jsonLst.append(exp.to_dict())
            with open(filename, "w") as file:
                json.dump(self.jsonLst, file, indent = 4)
            print("\nExpenses Saved Successfully!")
        else:
            print("\nNo Expenses Available")

    def loadjson(self):
        if os.path.exists(filename):
            with open(filename , "r") as file:
                loaded_list = json.load(file)
            self.expenseLst = []
            for data in loaded_list:
                exp_obj = Expense(data["title"], data["amount"], data["category"], datetime.datetime.fromisoformat(data["date"]))
                self.expenseLst.append(exp_obj)
            print("\nExpenses Loaded Successfully!")
        else:
            print("No Expenses to show")
    
    def analytics(self):
        total_amount = 0 #Initialise variables before accumulating
        avg_exp = 0
        highest_exp = 0

        print("=== Expenses Analytics ===")
        if len(self.expenseLst) == 0:
            print("No expense Analytics to show here")
            return

        for exp in self.expenseLst:
            total_amount += float(exp.amount)
            if exp.amount > highest_exp:
                highest_exp = exp.amount
        print(f"Total Amount: ${total_amount}")
        avg_exp = total_amount/len(self.expenseLst)
        print(f"Average Expense: ${avg_exp}")
        print(f"Highest Expense: ${float(highest_exp)}")       


expMan = ExpenseManager()
# exp1 = Expense("Bread", 100, "Food")
# expMan.add_expense(exp1)
# expMan.view_all_expense()
# expMan.search_by_category("Food")
# expMan.remove_expense("Bread")
# expMan.view_all_expense()

def createExp():
    title = input("Enter title: ")
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    return Expense(title, amount, category, date=datetime.datetime.now())

while True:
    print("\n=== Advanced Task Scheduler with Persistence ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Remove Expense")
    print("4. Filter by Category")
    print("5. Show Analytics")
    print("6. Save Expenses")
    print("7. Load Expenses")
    print("8. Quit\n")
    option = input("Choose an option >>> ")

    try:
        option = int(option)
        if option < 1 or option > 8:
            print("Invalid option entered")
        else:
            if (option == 1):
                addExp = createExp()
                expMan.add_expense(addExp)
                expMan.jsondump()
            elif (option == 2):
                expMan.view_all_expense()
            elif (option == 3):
                title = input("Enter title of expense you want to remove: ")
                expMan.remove_expense(title)
                expMan.jsondump()
            elif (option == 4):
                category = input("Enter Category: ")
                expMan.search_by_category(category)
            elif (option == 5):
                expMan.analytics()
            elif (option == 6):
                expMan.jsondump()
            elif (option == 7):
                expMan.loadjson()
            elif (option == 8):
                print("\nGoodbye!")
                break
    except ValueError as V:
        print(f"Invalid option entered {V}")
            


