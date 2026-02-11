#Tkinter Task Manager App
import os
import json
import tkinter as tk 
from tkinter.font import Font
from tkinter import messagebox

filename = "Tasks.json"

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
        for task in self.taskLst:
            if title.lower() == task.title.lower():
                task.display()
                found = True 
        if not found:
            print("No Match Found")
        
    def jsondump(self):
        self.jsonLst = [] #clearing json list everytime I save prolly to prevent saving duplicates
        if len(self.taskLst) != 0:
            for task in self.taskLst: #Loops through tasks list
                self.jsonLst.append(task.to_dict()) #adds all dictionary formatted tasks to the json list for saving
            with open(filename, "w") as file: #save opening & closing of json files
                json.dump(self.jsonLst, file, indent = 4) #saves with a neatly formatted values
            print("\nTask Saved Successfully!")
        else:
            print("\nNo Tasks Available")
    
    def jsonload(self):
        if os.path.exists(filename): #Checks if the contact json file path exists
            with open(filename , "r") as file: #Safe opening & closing
                loaded_list = json.load(file)#Load it into a new list
            self.taskLst = [] #Clear contact list
            for data in loaded_list:
                task_obj = Task(data["title"], data["completed"])
                self.taskLst.append(task_obj)
            print("\nTasks Loaded Successfully!")
        else:
            print("\nNo Tasks to show")
    
class TaskApp(tk.Tk):
    def __init__(self, store):
        super().__init__() #Very Important
        self.store = store
        self.title("Task Manager App")
        self.geometry("400x500")

        #Creating Fonts
        font1 = Font(
            family = "verdana",
            size = 18,
            weight = "bold",
            slant = "roman",
            underline = 0,
            overstrike = 0
        )

        #Main Title Label
        self.title_Label = tk.Label(self, text = "Task Manager", font = font1)
        self.title_Label.pack()
    
        #Create a main frame for everything else
        self.mainframe = tk.Frame(self)
        self.mainframe.pack(pady = 10)

        #Everything else goes onto the mainframe
        #tasks labels & entry
        self.task_label = tk.Label(self.mainframe, text = "Enter Task")
        self.task_entry = tk.Entry(self.mainframe, width = 30)

        #add task button
        self.task_button = tk.Button(
            self.mainframe,
            text = "Add Task",
            command = self.add_task
        )
        self.task_label.grid(column = 0, row = 0)
        self.task_entry.grid(column = 1, row = 0)
        self.task_button.grid(column = 2, row = 0, padx = 10)

        #Search Task Label & Button
        self.search_label = tk.Label(self.mainframe, text = "Search Task")
        self.search_entry = tk.Entry(self.mainframe, width = 30)
        self.search_button = tk.Button(
            self.mainframe,
            text = "Search"
        )
        #Placements
        self.search_label.grid(column = 0, row = 1 )
        self.search_entry.grid(column = 1, row = 1)
        self.search_button.grid(column = 2, row = 1, pady = 10)

        #Frame2
        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        #Listbox & List Labels
        self.task_listLabel = tk.Label(self.frame2, text = "Task List" )
        self.task_listbox = tk.Listbox(self.frame2, width = 40, height = 15)
        self.task_listLabel.grid(column = 1, row = 0)
        self.task_listbox.grid(column = 1, row = 1, pady = 10)
    
    #Connecting Buttons to logic
    #1. The Add_Task Button
    def add_task(self):
        title = self.task_entry.get()
        try:
            task = Task(title)
            self.store.add_task(task)
            self.store.jsondump()

            self.task_listbox.insert(tk.END, f"{task.title}")
            self.task_entry.delete(0, tk.END) 
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))


store = TaskStore() #Creates an instance of TaskStore
app = TaskApp(store) #Puts the instance of the TaskStore Class into the tkinter window
app.mainloop() #Runs the whole shebang

