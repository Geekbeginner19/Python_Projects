'''
🔥 Python Project of the Day:
🧍 Project: Personal To-Do List (Console App)
Goal: Build a small app that lets users manage their daily tasks — add, view, mark as done, and delete tasks.

🧱 Requirements:
When the program runs, show this menu:

1. Add a new task
2. View all tasks
3. Mark a task as done
4. Delete a task
5. Quit


When adding a task:
Ask for the task name (e.g., “Finish homework”).
Store it in a dictionary or list, with a status (e.g., “Pending”).

When viewing tasks:
Show all tasks in a numbered list like:

1. Finish homework — Pending
2. Go for a walk — Done


When marking a task as done:
Let the user enter the task number.
Change its status to “Done.”

When deleting a task:
Let the user enter the task number to remove it from the list.

Quit option:
End the program gracefully with a goodbye message.
'''

task_dict = {}#creating a dictionary
task_list = []#creating a list
print("--- To-do List Console Application ---")
while True:#Opening an infinite loop
    options = int(input("\n1.Add a new task.\n2.View all tasks.\n3.Mark task as done\n4.Delete a task.\n5.Quit.\n\nChoose an option.\n>>>"))
    if options == 1:
        enterTask = input("Please enter a task: ").lower()
        task_dict[enterTask] = "Pending"#adding the user input to a dictionary
        print("Task entered successfully!")
    elif options == 2:
        if len(task_dict) == 0:#checking if dictionary is empty
            print("No Tasks to Show")
        else:
            print("\nTasks List")
            count = 1
            for key, value in task_dict.items():
                print(f"{count}.{key} - {value}")#Displying the contents of the Dictionary
                count += 1
    elif options == 3:
        if len(task_dict) == 0:
            print("No Tasks to Show")
        else:
            print("\nTasks List")
            count = 1
            for key, value in task_dict.items():
                print(f"{count}.{key} - {value}")
                count += 1
            task_list = list(task_dict.keys())#appending keys of the dictionary to the a list
            tasktToMark = int(input("Please enter the task number to mark as done: "))
            if (tasktToMark >= 1) and (tasktToMark <= len(task_list)):#Setting protocol for the range of input
                task_dict[task_list[tasktToMark - 1]] = "Done"#Updating the values of dictionary depending on what the user says
            else:
                print("Invalid Task Number.")
    elif options == 4:
        if len(task_dict) == 0:
            print("No Shows to Show")
        else:
            print("\nTasks List")
            count = 1
            for key, value in task_dict.items():
                print(f"{count}.{key} - {value}")
                count += 1
            task_list = list(task_dict.keys())
            tasktToMark = int(input("Please enter the task number to delete: "))
            if (tasktToMark >= 1) and (tasktToMark <= len(task_list)):#Setting protocol for the range of input
                del task_dict[task_list[tasktToMark - 1]]#Deleting the values of dictionary depending on what the user says
            else:
                print("Invalid Task Number.")
    elif options == 5:
        print("Goodbye")
        break

      
    


