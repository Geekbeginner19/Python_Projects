# 🧾 Project: Expense Tracker (Console App)
# Goal: Create a simple expense tracker that helps users record and view their daily spending.
# 🧱 Requirements:
# When the program runs, show a menu:

# 1. Add expense
# 2. View all expenses
# 3. View total spent
# 4. Quit


# When the user adds an expense:
# Ask for a short description (e.g., “Groceries”)
# Ask for the amount spent
# Save it in a list or dictionary.

# When viewing expenses:
# Display all saved expenses in a clean format.
# When viewing total:
# Show the sum of all expenses so far.
# Allow the user to quit the program anytime.

expenses = {}#Empty dictionary to hold expense descriptions and amount
data_valid = False
while data_valid == False:#data validation
    print("---Expense Tracker---")
    option = input("1.Add Expense\n2.View all expenses\n3.View total spent\n4.Quit\nChoose an option: ")#Collecting user input
    try:
        option = int(option)#try to convert to integer
        if option < 1 or option > 4:#checking for out of range
            option = input("Please enter a valid option: ")
            continue#This skips to the next loop iteration and helps the code to keep looping well. Avoids unexpected outcomes 
        else:
            while option != 4:
                if option == 1:
                    expenseDescription = input ("Please enter the expense Description: ")
                    amount = float(input("Please enter amount: "))
                    expenses.update({f"{expenseDescription}" : amount})#adding the description and the amount to a dictionary
                    print("\nExpenses Entered Successfully!\n")
                    option = int(input("Choose an option: "))
                elif(option == 2):
                    if len(expenses) == 0:#Checking to see if expenses are empty
                        option = int(input("No Expenses to show\nChoose an option: "))
                    else:
                        count = 1
                        for key, values in expenses.items():#Showing the expenses
                            print(f"{count}.{key} - ${values}")
                            count += 1
                        print("\nAll Expenses accounted for.")
                        option = int(input("\nChoose an option: "))
                elif(option == 3):
                    if len(expenses) == 0:#Checking to see of expenses are empty
                        option = input("No expenses to total.\nChoose an option: ")
                    else:
                        totalSpent = sum(expenses.values())#Calculating the total of the Amounts
                        print(f"Total Spent: ${totalSpent}")
                        option = int(input("Choose an option: "))
                else:
                    option = 4
        print("Byee")#Exit Message
        data_valid = True
    except ValueError as e:
        print(f"\nAlphabets are not allowed. Error: {e}\n")#Printing error message if user inputs Alphabets
        