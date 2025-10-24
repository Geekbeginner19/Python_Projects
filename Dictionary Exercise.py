'''
Create a program with a predefined dictionary for a person. Include the following
information: name, gender, age, address & phone.
Ask the user what information he wants to know about the person (example:"name"), then
print the value associated to that key or dsiplay a message in case the key is not found
'''

#Creating a Predefined Dictionary
userInfo = {"name":"Kelvin Ofori Amoafo", "gender":"Male","age":23, "address":"Suncity, Tema-West", "phone":"+233-614-281-742"}.lower()

#Asking the user for information
AskUser = input ("Please enter the details of your target:\nname, gender, age, address, age or phone: ")

#Printing the result with a .get() function to handle errors
print(userInfo.get(AskUser, "Detail no found"))
