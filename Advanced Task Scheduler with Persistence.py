# PROJECT: Advanced Task Scheduler with Persistence
# WHAT YOU'RE BUILDING

# A command-line application that manages tasks with:
# Priority levels (High, Medium, Low)
# Due dates
# Categories (Work, School, Fitness, etc.)
# Search & filtering
# JSON persistence
# Optional threading timer feature

import os 
import json
filename = r"C:\Users\Rarissime\Downloads\Task Scheduler.json"

class Task:
    def __init__(self, title, priority, due_date:int, category):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.category = category
    
    def to_dict(self):
        return {
            "title" : self.title,
            "priority" : self.priority,
           "due_date" : self.due_date,
            "category" : self.category
        }
    
    def display(self):
        print(f"Task Title: {self.title} | Priority: {self.priority} | Due Date: {self.due_date} day(s) | Category: {self.category}")
    

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.json = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        found = False
        for tsk in self.tasks:
            if task.lower() == tsk.title.lower():
                self.tasks.remove(tsk)
                found = True
                break #after match is found stop looping (deletes safely too)
        if not found:
            print("No match!")    

    def search(self, task):
        found = False
        for tsk in self.tasks:
            if task.lower() == tsk.title.lower():
                tsk.display()
                found = True
        if not found:
            print("No match!") 
    
    def view_all_tasks(self):
        print("\n=== Advanced Task Scheduler ===")
        if not self.tasks: # If there is nothing in self.tasks list
            print("No tasks available.")
        else:
            for tsk in self.tasks:
                tsk.display()
    
    def filter_by_priority(self, priority:str):
        for prior in self.tasks:
            if priority.lower() == prior.priority.lower():
                prior.display()

    def filter_by_category(self, category:str):
        for cat in self.tasks:
            if category.lower() in cat.category.lower():
                cat.display()
    
    def jsondump(self):
        self.json = [] #Clear the json list
        if len(self.tasks) != 0:
            for tsk in self.tasks:#objects from the Task Class
                self.json.append(tsk.to_dict()) #Adding all objects from Task Class converted to dict to the json list
            with open(filename, "w") as file:
                json.dump(self.json, file, indent = 4)
        else:
            print("No Tasks to see here")
    
    def jsonload(self):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                loaded_list = json.load(file)
            self.tasks = [] #clear current task list
            for data in loaded_list:
                task_obj = Task(data["title"], data["priority"], int(data["due_date"]), data["category"])  # convert dict back to Item Object
                self.tasks.append(task_obj)#Adds the objects back into the self.items list
            print("\nTasks Loaded Successfully!")
        else:
            print("No Task available")
    
tskmanager = TaskManager()

def mktask():
    title = input("Enter Title: ")
    priority = input("Enter priority: ")
    due_date = int(input("Enter due date in number of day(s): "))
    category = input("Enter Category: ")

    return Task(title, priority, due_date, category)

while True:
    print("\n=== Advanced Task Scheduler with Persistence ===")
    print("1. Add task")
    print("2. View All Tasks")
    print("3. Remove Task")
    print("4. Search Task")
    print("5. Filter by Priority")
    print("6. Filter by Category")
    print("7. Save Task")
    print("8. Load Tasks")
    print("9. Quit\n")
    option = input("Choose an option >>> ")

    try:
        option = int(option)
        if option < 1 or option > 9:
            print("Please enter a valid option")
        else:
            if option == 1:
                addtask = mktask()
                tskmanager.add_task(addtask)
                tskmanager.jsondump()
            elif (option == 2):
                tskmanager.view_all_tasks()
            elif(option == 3):
                title = input("Enter task title: ")
                tskmanager.remove_task(title)
            elif(option == 4):
                title = input("Enter task title: ")
                tskmanager.search(title)
            elif(option == 5):
                priority = input("Enter priority type: ")
                tskmanager.filter_by_priority(priority)
            elif(option == 6):
                category = input("Enter category: ")
                tskmanager.filter_by_category(category)
            elif(option == 7):
                tskmanager.jsondump()
            elif(option == 8):
                tskmanager.jsonload()
            elif(option == 9):
                print("\nGoodbye!")
                break
    except ValueError as V:
        print(f"Invalid option entered {V}")
    

