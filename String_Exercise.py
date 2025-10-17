#EXERCISE 1

#collecting information from users
first_name = input("Please enter your first name: ")
middle_name = input("Please enter your middle name: ")
last_name = input("Please enter your last name: ")

#doing some uppercase conversion
FN = first_name.upper()
MN = middle_name.upper()
LN = last_name.upper()

#printing the initials
print("Your initials are", FN[0], MN[0], LN[0])



#EXERCISE 2

#collecting info from users and converting to integer
productNumber = input("Please enter the product number:\n example: 0370090100027\n")
if (len(productNumber) == 13):
    #Slicing the string
    countryCode = productNumber[0:3]
    productCode = productNumber[3:8]
    batchNumber = productNumber[-5:]

    #printing the output
    print("The country code is:", countryCode)
    print("The product code is:", productCode)
    print("The batch number is:", batchNumber)
else:
    print("The Product Number must have 13 digits, please recheck and enter again")



        
        





