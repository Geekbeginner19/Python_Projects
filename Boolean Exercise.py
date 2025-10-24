'''
CREATE A PROGRAM AND STORE YOUR AGE IN A VARIABLE. THEN ASK THE USER FOR HIS AGE AND
PRINT WHETHER
*HE'S OLDER THAN YOU
*HE'S YOUNGER THAN YOU
*YOU TWO HAVE THE SAME AGE
'''

#STORING THE AGE IN A VARIABLE
KelvinAge = 23

#GETTING INTO THE CONDITIONS
userAge = int(input("Please enter your age: "))
if (userAge > KelvinAge):
    print("You're Older than Kelvin")
elif (userAge < KelvinAge):
    print("You're younger than Kelvin")
else:
    print("You're the same age as Kelvin:)")

