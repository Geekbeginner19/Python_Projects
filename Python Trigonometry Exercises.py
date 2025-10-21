import math #Importing the Python Math Library

#Collecting information from user & conversion
radius = float(input ("Please enter the raduis: "))

#Calculating the area & circumference
area = ((math.pi) * (radius ** 2))
circumference = (2 * math.pi * radius)

#Displaying Results
print (f"Area:{area:.3f}, Circumference:{circumference:.3f}")

