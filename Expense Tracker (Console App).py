# 🔥 Python Project of the Day:
# 🧾 Expense Tracker (Console App)

# 🎯 Goal:
# Build a simple expense tracker that helps you record, view, and analyze your daily spending — and stores the data permanently using JSON.

# 🧱 Features:
# Add a New Expense
# Ask for:
# Description (e.g., “Groceries”)
# Amount (float)
# Category (e.g., “Food”, “Transport”, “Bills”)
# Save each expense as a dictionary in a list, then write it to a file expenses.json.

# View All Expenses
# Read and display all expenses neatly:
# Description: Groceries | Amount: GHS 120.5 | Category: Food


# View Total Spent
# Calculate and display the sum of all expenses from the file.

# Search by Category
# Let the user type a category (e.g., “food”) and show all matching expenses.

# Quit
# Exit gracefully with a thank-you message.

# Add menu options exactly like this:

# --- Expense Tracker ---
# 1. Add Expense
# 2. View All Expenses
# 3. View Total Spent
# 4. Search by Category
# 5. Quit


import os
import json

filename = r"C:\Users\Rarissime\Downloads\Expenses.json"
expenseList = []

def jsonLoad():
    if os.path.exists(filename): #checking if json file already exists
        with open(filename, "r") as file:#Safe opening of the expense file (in read mode)
            expenseList = json.load(file)#reading/loading the contents and assigning it into the expenseList
    else:
        expenseList = []#return empty list if there are no contents in the file 

def jsonDump():
    with open(filename, "w") as file:#Safe Opening the expense file in write mode
        json.dump(expenseList, file, indent = 4)#writing/dumping the contents of the expenseList into the json file


def add_expense():
    expenseDict = {}
    description = input("Please enter the description: ").lower()
    amount = float(input("Please enter the amount: "))
    category = input("Please enter the category: ").lower()
    expenseDict.update({"description": description})
    expenseDict.update({"amount": amount})
    expenseDict.update({"category": category})
    jsonLoad()
    expenseList.append(expenseDict)#addes all inputs from dictionary into a list
    jsonDump()

def view_all_expenses():
    if os.path.exists(filename):#checks if the json file exists(MAY RUN THROUGHOUT THE CODE)
        with open(filename, "r") as file:#safe opening of json file
            expenseList = json.load(file)
        for expenses in expenseList:#going through all the dictionaries in the list
            print(f"Description : {expenses['description'].capitalize()} | Amount : ${expenses['amount']} | Category : {expenses['category'].capitalize()}")
    else:
        print("No expenses to show")

def view_total_spent():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            expenseList = json.load(file)
        sumOfamount = 0    
        for expenses in expenseList:#going through all the dictionaries in the list
            sumOfamount += expenses['amount']#Calculating all amounts in the expenses
        print(f"The total spent is >> ${sumOfamount}")
    else:
        print("No expenses to show")
    

def search_by_category():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            expenseList = json.load(file)
        while True:
            search = input("Please enter the category you want to search: ").lower()
            try :
                search = int(search)
                print("Invalid Input.")
            except:
                break
        found = False
        for expenses in expenseList:
            if search.lower() in expenses['category'].lower():#checking if the user input matches the categories (using 'in' to allowing for partial matches)
                print(f"Description : {expenses['description'].capitalize()} | Amount : ${expenses['amount']} | Category : {expenses['category'].capitalize()}")
                found = True
            else:
                continue
        if not found:#if no match found
            print("No Match")
    else:
        print("No expenses available to search")

while True:
    options = input("\n--- Expense Tracker ---\n1. Add Expense\n2. View All Expenses\n3. View Total Spent\n4. Search by Category\n5. Quit\n\n Choose an option>>> ")
    try:#eror handling
        options = int(options)
        if options < 1 or options > 5:
            print("Please enter a valid option.")
        else:
            if options == 1:
                add_expense()
            elif(options == 2):
                view_all_expenses()
            elif(options == 3):
                view_total_spent()
            elif(options == 4):
                search_by_category()
            elif(options == 5):
                print("Goodbye!")
                break
    except ValueError as V:
        print(f"Please enter a valid option {V}")

