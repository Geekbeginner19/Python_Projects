''' EXERCISE #1
Create a Program that asks the user for his birthday in format:
'DD-MM-YYYY'. then print 'You were born in [month]'''      

#Creating a tuple of the months of the Year
monthsOfYear = (" ", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#Collecting information from user
DOB = input ("Please enter your date of birth in this format'DD-MM-YYYY': ")

#Slicing the "MM" part outta the format & converting to integer
slicedDOB = int(DOB[3:5])

#parsing them to the created tuple
monthinwords = monthsOfYear[slicedDOB]

#Showing the results
print(f"You were born in {monthinwords}")






''' CREATE A PROGRAM WITH A PREDEFINED LIST OF PEOPLE. ASK THE USER FOR HIS NAME
    AND ADD IT TO THE END OF THE LIST & PRINT THE UPDATED LIST
'''

ListOfInvites = ["Kelvin", "Grant", "Ebenezer", "Jacqueline", "Comfort", "Barbara"]
nameofGuest = input("Please enter your first name: ")
ListOfInvites.append(nameofGuest)
print(ListOfInvites)
