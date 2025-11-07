#Simple interest Calculator
while True:#Creating an infinite loop for data validation
    try:#Entering the trying blook
        principal_amount = float(input("Please enter the principal amount($): "))
        rate = float(input("Please enter the rate(%): "))
        time = float(input("Please enter the time(years): "))
        if principal_amount <= 0:
            print("Please enter valid parameters.")
        elif(rate <= 0):
            print("Please enter valid parameters")
        elif(time <= 0):
            print("Please enter valid parameters")
        else:
            break#break from infinite loop if the above conditions in the if block are not met
    except Exception as e:#If the above block can't execute it's then thrown to the exception
        print(f"Invalid input due to the following error: {e}")

def simple_interest(principal_amount: float, rate: float, time: float):
    interest_rate = (principal_amount * rate * time)/100
    return interest_rate

result = simple_interest(principal_amount, rate, time)
print(f"The Simple interest is: ${result}")



