'''
CREATE A PROGRAM TO CALCULATE THE BMI (BODY MASS INDEX) OF A PERSON.
ASK THE USER FOR HIS HEIGHT IN METERS AND HIS WEIGTH IN KG
BMI = WEIGHT / (HEIGHT * HEIGHT)

PRINT THE BMI AND THE CLASSIFICATION
*LESS THAN OR EQUAL TO 18.5 IS UNDERWEIGHT
*GREATER THAN 18.5 OR LESS THAN OR EQUAL TO 24.9 IS NORMAL WEIGHT
*GREATER THAN 24.9 OR LESS THAN OR EQUAL TO 29.9 OVERWEIGHT
*GREATER THAN OR EQUAL TO 30 IS OBESITY
'''

#collecting user info on weight & height
UserWeight = float(input("Please enter your weight in kilogram: "))
UserHeight = float(input("Please enter your height in meters: "))

#calculating BMI
BMI = UserWeight / (UserHeight * UserHeight)

#Showing results according to conditons, whether underweight
#overweight or obese
if (BMI <= 18.5):
    print(f"This is your body mass index:{BMI:2f}. You're underweight")
elif (BMI > 18.5 and BMI <= 24.9):
    print(f"This is your body mass index:{BMI:.2f}. Your weight is within the normal healthy range")
elif (BMI > 24.9 and BMI <= 29.9):
    print(f"This is your body mass index:{BMI:.2f}. You're overweight")
else:
    print(f"This is your body mass index:{BMI:.2f}. You're obese")


    
