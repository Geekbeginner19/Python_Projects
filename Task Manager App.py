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
        self.jsonLst = [] #Empties List

        for task in self.taskLst:
            self.jsonLst.append(task.to_dict())

        with open(filename, "w") as file:
            json.dump(self.jsonLst, file, indent=4)

        print("\nTask Saved Successfully!")
    
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
        self.minsize(400, 500)

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
            text = "Search",
            command = self.search_tasks
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
        #Toggle to complete button
        self.task_listbox.bind("<Double-Button-1>", self.toggle_task)

        self.view_all_tasks_button = tk.Button(
            self.frame2,
            text = "View All Tasks",
            command = self.view_all_tasks
        )
        self.view_all_tasks_button.grid(column = 1, row = 2, pady = 10)

        # Load existing tasks visually
        self.refresh_listbox()

        #Delete Tasks Button
        self.delete_button = tk.Button(
            self.frame2,
            text = "Delete Task",
            command = self.delete_task
        )
        self.delete_button.grid(column = 1, row = 3, pady = 5)

    #Connecting Buttons to logic
    #1. The Add_Task Button
    def add_task(self):
        title = self.task_entry.get()
        try:
            task = Task(title)
            self.store.add_task(task)
            self.store.jsondump()

            self.task_listbox.insert(tk.END, f"[ ]{task.title}")
            self.task_entry.delete(0, tk.END) 
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))
    
    #Refreshing the listbox
    def refresh_listbox(self):        
        self.task_listbox.delete(0, tk.END)

        for task in self.store.taskLst:
            if task.completed:
                self.task_listbox.insert(tk.END, f"[✓] {task.title}")
            else:
                self.task_listbox.insert(tk.END, f"[ ] {task.title}")

    def search_tasks(self):
        name = self.search_entry.get() #Collects entry info

        self.task_listbox.delete(0, tk.END)
        if len(self.store.taskLst) != 0:
            found = False
            for task in self.store.taskLst:
                if name.lower() == task.title.lower():
                    self.search_entry.delete(0, tk.END) #Clears entry
                    if task.completed: #Checks for task completion
                        self.task_listbox.insert(tk.END, f"[✓] {task.title}")
                    else:
                        self.task_listbox.insert(tk.END, f"[ ] {task.title}")
                    found = True
            if not found:
                messagebox.showerror("Error","No Match Found")
        else:
            messagebox.showerror("Error","Nothing to Show here!")
            return
    
    def view_all_tasks(self):
        self.refresh_listbox()
        if len(self.store.taskLst) == 0:
            messagebox.showerror("Error","No Tasks to View")
            return
    
    #Double click to toggle to complete
    def toggle_task(self, event):        
        selection = self.task_listbox.curselection()

        if not selection:
            return

        index = selection[0]
        task = self.store.taskLst[index]

        # Toggle completion
        task.completed = not task.completed

        self.store.jsondump()
        self.refresh_listbox()
    
    #Delete tasks
    def delete_task(self):
        selection = self.task_listbox.curselection()

        if not selection:
            messagebox.showerror("Error", "Select a task first")
            return

        # Get selected item text
        selected_text = self.task_listbox.get(selection[0])

        # Extract title (remove [ ] or [✓])
        title = selected_text[4:].strip()

        # Remove matching task from store
        self.store.taskLst = [
            task for task in self.store.taskLst
            if task.title != title
        ]

        self.store.jsondump()
        self.refresh_listbox()
    


store = TaskStore() #Creates an instance of TaskStore
store.jsonload() #Loads data when app starts
app = TaskApp(store) #Puts the instance of the TaskStore Class into the tkinter window
app.mainloop() #Runs the whole shebang

