'''
CREATE A PROGRAM AND STORE YOUR AGE IN A VARIABLE. THEN ASK THE USER FOR HIS AGE AND
PRINT WHETHER
*HE'S OLDER THAN YOU
*HE'S YOUNGER THAN YOU
*YOU TWO HAVE THE SAME AGE
'''

#STORING THE AGE IN A VARIABLE
KelvinAge = 23

#COLLECTING USER INFO
userAge = input("Please enter your age: ")
#Handling an error where user enters a string
while True:
    try:
        userAge = int(userAge)
        #Validating the data whether it's within the valid range
        dataValid = False
        while dataValid == False:
            if userAge < 0:
                userAge = int(input("Please enter a valid age: "))
            else:
                dataValid = True
                continue #skips into the inner while True loop
        break #jumps out of the Outta while True loop
    except:
        userAge = input("Please enter a number: ")
        continue #goes back to execute the loop until the condition is met

#HANDLING CONDITIONS
if (userAge > KelvinAge):
    print("You're Older than Kelvin")
elif (userAge < KelvinAge):
    print("You're younger than Kelvin")
else:
    print("You're the same age as Kelvin:)")

