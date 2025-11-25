# 🧩 MINI PROJECT 3: Encapsulated BankAccount with Inheritance

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

# Then create two Child Classes:

# SavingsAccount(BankAccount)
# has an extra method: add_interest(rate)

# StudentAccount(BankAccount)
# allows only 1 free withdrawal, afterwards fee = $5 per withdrawal
# track number of withdrawals

# Requirements:
# Create one SavingsAccount and one StudentAccount.
# Test deposit, withdraw, and the special features.
# Use inheritance + super().

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
        print(f"\nAccount Holder(Current Account): {self.owner_name} | Account Balance: ${self.get_balance()}")

    def set_balance(self, amount):#Setting acc balance so that it can't be in negatives
        if amount >= 0:
            self.__balance = amount

class SavingsAccount(BankAccount):
    #Super() method is important if the child class needs a new attribute
    #so the super() method is employed to override the parent class constructor within the child class(only)
    #in order to add a new attribute to the child class(only)
    def __init__(self, owner_name, balance):
        super().__init__(owner_name, balance)# calls BankAccount's __init__ (There is actually no need for that since the child class adds no new attributes)

    def interest(self, time, rate = 0.10):
        self.rate = rate 
        self.time = time
        return self.get_balance() * self.rate * time
    
    def display_info(self):
        print(f"\nAccount Holder(Savings Account): {self.owner_name} | Interest Made: ${self.interest(time)}"
             f" | Account Balance: ${self.interest(time) + self.get_balance()}")
    
class StudentAccount(BankAccount):
    def __init__(self, owner_name, balance):
        super().__init__(owner_name, balance) #Overriding the methods of parent class with the super() method within this child class
        self.withdrawals = 0  #Tracking number of withdraws
    
    def withdraw(self, amount):
        fee = 0
        if self.withdrawals >= 1:
            fee = 5
        
        total_amount = amount + fee 

        if total_amount > self.get_balance(): #Checking if the total amount is bigger than the account balance
            print("Insufficient balance for this transaction (including fee).")
            return
        
        #Performing method through parent method
        super().withdraw(total_amount)

        self.withdrawals += 1 #Updating the number of withdraws after the parent method performs the withdrawal

        if fee > 0:
            print(f"A $5 fee was charged (withdrawal #{self.withdrawals}).")
        else:
            print("Free withdrawal used!")
    
    def display_info(self):
        print(f"\nAccount Holder(Student Account): {self.owner_name}"
             f" | Account Balance: ${self.get_balance()}")
        

accList = []    
        
def createSavAcc():
    name = input("Please enter name: ")
    balance = float(input("Please enter balance: "))
    return SavingsAccount(name, balance)

def createStuAcc():
    name = input("Please enter name: ")
    balance = float(input("Please enter balance: "))
    return StudentAccount(name, balance)

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
    print("1. Create a Current Account.")
    print("2. Create a Saving Account. ")
    print("3. Create a Student Account. ")
    print("4. Deposit.")
    print("5. Withdraw.")
    print("6. Display Balance.")
    print("7. Quit.\n")
    options = input("Choose an option >>> ")

    try:
        options = int(options)
        if options < 1 or options > 7:
            print("Enter a valid option")
        else:
            if options == 1:
                accountHolder = createAcc()
                accList.append(accountHolder)
            elif(options == 2):
                accountHolder = createSavAcc()
                accList.append(accountHolder)
                time = int(input("\nEnter the time for your interest (Years): "))
                accountHolder.interest(time)
                accountHolder.display_info()
            elif(options == 3):
                accountHolder = createStuAcc()
                accList.append(accountHolder)
            elif(options == 4):
                accountHolder = selectAcc()#AccountHolder stores whatever the selectAcc() function returns (which is the user selected object)
                amount = float(input("Enter an amount: "))
                accountHolder.deposit(amount)
            elif(options == 5):
                accountHolder = selectAcc()
                amount = float(input("Enter an amount: "))
                accountHolder.withdraw(amount)
            elif(options == 6):
                accountHolder = selectAcc()
                accountHolder.display_info()
            elif(options == 7):
                print("Goodbye!\n")
                break
    except ValueError as V:
        print(f"Invalid Options {V}")
        

