# 🧩 PROJECT 1: Student Registration System

# Goal:
# Create a class called Student with the following:

# Attributes: name, age, student_id

# Method: display_info() → prints the student details

# Example Output:

# Name: Kelvin
# Age: 22
# Student ID: ST-101

class Student():#creating the student class
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
    
    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Student_id: {self.student_id}")

studentDetails = []#creating a list to store objects

def enterStudent():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student_id = input("Enter student id: ")
    return Student(name, age, student_id) #Returns an instance of the class

while True:
    print("\n===== Student Registration System =====")
    print("1. Enter Student Details")
    print("2. View Student Details.")
    print("3. Quit")
    options = input("\nChoose an option >>> ")
    try:
        options = int(options)
        if options < 1 or options > 3:
            print("Please enter a valid option\n")
        else:
            if options == 1:
                student = enterStudent()#Creating an object each time the user wants to enter student details
                studentDetails.append(student)#Appending each student object into a list
            elif(options == 2):
                for student in studentDetails:#Combing through the list of objects
                    student.display_info()#Using the display info attributes of each object found in the list
            elif(options == 3):
                print("Goodbye!\n")
                break
    except ValueError as V:
        print(f"Invalid Option {V}\n")