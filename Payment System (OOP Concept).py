# 🧩 SMALL MINI-PROJECT: PAYMENT SYSTEM (Polymorphism)

# You will create:

# A base class: PaymentMethod

# Child classes:
# CreditCardPayment
# MobileMoneyPayment
# CashPayment

# Each class will have methods with the SAME name:

# Required Methods:
# pay(amount)
# receipt(amount)

# But their internal behavior will be different.

# Usage Example:
# methods = [CreditCardPayment(), MobileMoneyPayment(), CashPayment()]

# for m in methods:
#     m.pay(200)
#     m.receipt(200)

# 🚀 YOUR TASK

# Write this polymorphism mini-project:

# Class Requirements

# PaymentMethod (Base Class)
# pay(amount) → just print something basic
# receipt(amount) → print “Generic receipt”

# CreditCardPayment
# Override both methods
# Simulate card processing

# MobileMoneyPayment
# Override both methods
# Simulate MoMo processing

# CashPayment
# Override both methods
# Simple cash message

class PaymentMethod():
    def __init__(self, name):
        self.name = name
        self.amount = 0 #safe default
    
    def pay(self, amount):
        self.amount = amount #Initializing the amount here so the receipt methid can use it too
        print(f"Payment made for ${amount} from Account Holder: {self.name}")
    
    def receipt(self, amount):
        print("Generic Receipt")
    
class CreditCardPayment(PaymentMethod):
    def __init__(self, name):
        super().__init__(name)
              
    def pay(self, amount):
        self.amount = amount
        print(f"Card Processing an amount of ${amount} for payment from Account Holder: {self.name}")
    
    def receipt(self, amount):
        print(f"Card Payment Receipt of ${self.amount} from Account Holder: {self.name}")
    

class MobileMoneyPayment(PaymentMethod):
    def __init__(self, name):
        super().__init__(name)       

    def pay(self, amount):
        self.amount = amount
        print(f"MobileMoney Payment for ${amount} from Account Holder: {self.name}")
    
    def receipt(self, amount):
        print(f"MobileMoney Payment of ${self.amount} Receipt from Account Holder: {self.name}")


class CashPayment(PaymentMethod):
    def __init__(self, name):
        super().__init__(name)
        
    def pay(self, amount):
        self.amount = amount
        print(f"Cash Payment for ${amount} from Account Holder: {self.name}")
    
    def receipt(self, amount):
        print(f"Cash Payment of ${self.amount} Receipt from Account Holder: {self.name}")


payMethodsList = []

def selectAcc(): #After User creates an account he has to select it to make payments from the specified account
    global payMethodsList
    print("\n=== Select Account ===")
    for i, acc in enumerate(payMethodsList):
        print(f"{i + 1}.{acc.name}")
    options = int(input("Select an Account: "))
    return payMethodsList[options - 1]

def momo():
    name = input("Enter your name: ")
    print("\nMomo Account Successfully Created!")
    return MobileMoneyPayment(name)

def card_pay():
    name = input("Enter your name: ")
    print("\nAccount Successfully Created!")
    return CreditCardPayment(name)

def cash_pay():
    name = input("Enter your name: ")
    print("\nAccount Successfully Created!")
    return CashPayment(name)

while True:
    print("\n=== Payment Methods Available ===")
    print("1. Credit Card Payment.")
    print("2. Mobile Money Payment.")
    print("3. Cash Payment.")
    print("4. Quit\n")
    options = input("Choose an option >>> ")

    try:
        options = int(options)
        if options < 1 or options > 4:
            print("Enter a valid option.")
        else:
            if (options == 1):
                accountHolder = card_pay()
                payMethodsList.append(accountHolder)
                accountHolder = selectAcc()
                amount = int(input("Enter the amount: "))
                accountHolder.pay(amount)
                accountHolder.receipt(amount)
            elif(options == 2):
                accountHolder = momo()
                payMethodsList.append(accountHolder)
                accountHolder = selectAcc()
                amount = int(input("Enter the amount: "))
                accountHolder.pay(amount)
                accountHolder.receipt(amount)
            elif(options == 3):
                accountHolder = cash_pay()
                payMethodsList.append(accountHolder)
                accountHolder = selectAcc()
                amount = int(input("Enter the amount: "))
                accountHolder.pay(amount)
                accountHolder.receipt(amount)
            elif (options == 4):
                print("Goodbye!\n")
                break
    except ValueError as V:
        print(f"Invalid option {V}")