from tkinter import *

def add_task():
    task = task_var.get()
    if task:
        tasks.append(task)
        task_var.set("")
        update_task_list()
        status_label.config(text="Task added", fg="green")
    else:
        status_label.config(text="Please enter a task", fg="red")

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
        status_label.config(text="Task deleted", fg="green")
    else:
        status_label.config(text="Please select a task to delete", fg="red")

def mark_as_done():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks[task_index] = tasks[task_index] + " (Done)"
        update_task_list()
        status_label.config(text="Task marked as done", fg="green")
    else:
        status_label.config(text="Please select a task to mark as done", fg="red")

def update_task_list():
    task_list.delete(0, END)
    for task in tasks:
        task_list.insert(END, task)

root = Tk()
root.title("To-Do List Application")
root.geometry("400x400")

tasks = []
task_var = StringVar()

Label(root, text="Task", font="lucida 18").grid(row=0, column=0, pady=10)
Entry(root, textvariable=task_var, font="lucida 18").grid(row=0, column=1, pady=10)

Button(root, text="Add Task", command=add_task, font="lucida 14").grid(row=1, column=1, pady=10)
Button(root, text="Delete Task", command=delete_task, font="lucida 14").grid(row=2, column=1, pady=10)
Button(root, text="Mark as Done", command=mark_as_done, font="lucida 14").grid(row=3, column=1, pady=10)

task_list = Listbox(root, font="lucida 14", width=30, height=10)
task_list.grid(row=4, column=0, columnspan=2, pady=10)

status_label = Label(root, text="", fg="red", font="lucida 12")
status_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
