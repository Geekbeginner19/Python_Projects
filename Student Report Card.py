# 🔥 Beginner OOP Project of the Day
# 🧾 Project: Student Report Card (OOP Basics)

# Simple, practical, and perfect for people transitioning from beginner → intermediate.

# 🎯 Goal
# Create a system that stores students and their scores, then calculates their average automatically — using classes.

#  🧩 Requirements
# 1. Create a class called Student

# Each student should have:
# name
# math score
# english score
# science score

# Inside the class, create a method:
# calculate_average(self)
# Returns the student’s average score.

# Also create:

# display_info(self)
# Prints:
# Name: Kelvin
# Math: 85
# English: 92
# Science: 78
# Average: 85.0

# 2. In the main program:
# Create an empty list called students.

# Create this menu:
# --- Student Report Card ---
# 1. Add Student
# 2. View All Students
# 3. Quit

# Add Student
# Ask for the student's:
# name
# math score
# english score
# science score

# Create a Student object and append it to the list.

# View All Students
# Loop through the list and call student.display_info() for each object.

# Quit
# Exit gracefully.

class Student:
    def __init__(self, name, mathScore, englishScore, scienceScore):
        self.name = name 
        self.mathScore = mathScore
        self.englishScore = englishScore
        self.scienceScore = scienceScore

    def get_date(self):
        self.name = input("Please enter your name: ")
        self.mathScore = float(input("Please enter you math score: "))
        self.englishScore = float(input("Please enter your english score: "))
        self.scienceScore = float(input("Please enter your science score: "))
    
    def calculate_average(self, average):
        self.average = average
        self.average = (self.mathScore + self.englishScore + self.scienceScore) / 3
        return self.average
    
    def display_info(self):
        print(self.name)
        print(self.mathScore)
        print(self.englishScore)
        print(self.mathScore)
        print(self.average)
    
studentList = []
student1 = Student("", "", "", "")
student1.get_date()
student1.display_info()
