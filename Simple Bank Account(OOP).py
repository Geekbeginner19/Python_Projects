# 🧩 PROJECT 2: Simple Bank Account Class

# Create a BankAccount class with:

# Attributes: owner, balance

# Methods:

# deposit(amount)
# withdraw(amount)
# display_balance()

# Try:
# acc = BankAccount("Kelvin", 500)
# acc.deposit(200)
# acc.withdraw(100)
# acc.display_balance()

class BankAccount():
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):#Not a good practice for methods in a class to be receiving input
        self.amount = amount
        if self.amount <= 0:
            print("Deposit cannot be made in zeros and negatives.")
        else:
            self.balance += amount
            print(f"{self.amount} successfully deposited!")
        
    def withdraw(self, amount):
        if self.amount > self.balance:
            print("Your balance is insufficient to make this transaction.")
        else:
            self.balance -= amount
            print(f"{self.amount} successfully withdrawn!")
    
    def display_balance(self):
        print(f"Account Holder:{self.owner_name} | Balance: ${self.balance}")

createdAccList = []

def createAcc():
    owner_name = input("Enter account owner name: ")
    balance = float(input("Enter account initial balance: "))
    return BankAccount(owner_name, balance)

def selectAcc():#It's very important feature!
    global createdAccList
    print("=== Select Account ===")
    for i, acc in enumerate(createdAccList):
        print(f"{i + 1}.{acc.owner_name}")
    option = int(input("Choose account number: "))
    return createdAccList[option - 1]

    
while True:
    print("\n===== Bank =====")
    print("1. Create an Account.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Display Balance.")
    print("5. Quit.\n")
    options = input("Choose an option >>> ")

    try:
        options = int(options)
        if options < 1 or options > 5:
            print("Enter a valid option")
        else:
            if options == 1:
                accountHolder = createAcc()
                createdAccList.append(accountHolder)
            elif(options == 2):
                accountHolder = selectAcc()#AccountHolder stores whatever the selectAcc() function returns (which is the user selcted object)
                amount = float(input("Enter an amount: "))
                accountHolder.deposit(amount)
            elif(options == 3):
                accountHolder = selectAcc()
                amount = float(input("Enter an amount: "))
                accountHolder.withdraw(amount)
            elif(options == 4):
                accountHolder = selectAcc()
                accountHolder.display_balance()
            elif(options == 5):
                print("Goodbye!\n")
                break
    except ValueError as V:
        print(f"Invalid Options {V}")
        
