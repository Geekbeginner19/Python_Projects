#Tkinter Task Manager App
import os
import json

class Task:
    def __init__(self, title, completed = False):
        #Title Validation
        if not title or not title.strip():
            raise ValueError("Title Cannot be Empty")

        self.title = title.strip()
        self.completed = completed
    
    def to_dict(self):
        return {
            "title" : self.title,
            "completed" : self.completed
        }
    
    def mark_as_completed(self):
        if self.completed == False:
            self.completed = True
            print("Task Completed")

    def display(self):
        print(f"Task Title: {self.title} | Complete Status: {self.completed}")

# task1 = Task("Teach")
# task1.display()
# task1.mark_as_completed()
# task1.display()

class TaskStore:
    def __init__(self):
        self.taskLst = []
        self.jsonLst = []
    
    def add_task(self, task):
        self.taskLst.append(task)
    
    def view_all_tasks(self):
        if len(self.taskLst) == 0:
            print("No Tasks to view")
            return
        print("==== All Tasks ====")
        for task in self.taskLst:
            task.display()

    def search_task(self, title):
        if len(self.taskLst) == 0:
            print("No Tasks to view")
        found = False
        for task in self.task:
            if title.lower() == task.title.lower():
                task.display()
                found = True 
        if not found:
            print("No Match Found")
        