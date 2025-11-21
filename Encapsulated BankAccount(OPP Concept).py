# 🧩 MINI PROJECT 3: Encapsulated BankAccount

# Create a BankAccount class with:
# Private attribute
# __balance

# Public attributes
# owner

# Methods
# deposit(amount)
# withdraw(amount)
# get_balance()

# Requirements:
# ✔️ Balance must NEVER become negative
# ✔️ No direct access like acc.__balance
# ✔️ Only deposit/withdraw can modify balance
# ✔️ Use a getter to check balance

# Example usage:
# acc = BankAccount("Kelvin", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# print(acc.get_balance())   # should print 1300

class BankAccount():
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance #Private
    
    def deposit(self, amount):
        if amount <= 0:
            print("Cannot deposit in negatives or zeros")
        else:
            self.__balance += amount
            print(f"\n${amount} deposited successfully")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Your balance is insufficient to make this transaction.")
        else:
            self.__balance -= amount
            print(f"\n${amount} successfully withdrawn!")

    def get_balance(self):#Private Attributes can be accessed only here(Getters - helps to read private data safely)
        return self.__balance

    def display_info(self):                                        #calling the get_balance() function to display private account balance
        print(f"\nAccount Holder: {self.owner_name} | Account Balance: ${self.get_balance()}")

    def set_balance(self, amount):#Setting acc balance so that it can't be in negatives
        if amount >= 0:
            self.__balance = amount

accList = []
    
def createAcc():
    name = input("Please enter name: ")
    balance = float(input("Please enter balance: "))
    return BankAccount(name, balance)

def selectAcc():
    global accList
    print("=== Select Account ===")
    for i, acc in enumerate(accList):
        print(f"{i + 1}.{acc.owner_name}")
    option = int(input("Choose an option >>> "))
    return accList[option - 1]

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
                accList.append(accountHolder)
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
                accountHolder.display_info()
            elif(options == 5):
                print("Goodbye!\n")
                break
    except ValueError as V:
        print(f"Invalid Options {V}")
        

