from tkinter import *

def add_task():
    task = task_var.get()
    if task not in tasks:
        tasks.append(task)
        task_var.set("")
        status.config(text="Added")
        update_listbox()
    else:
        status.config(text="Already exists")
def remove_task():
    tsk = tasklst.curselection()
    tasks.pop(tsk[0])
    status.config(text="Deleted")
    update_listbox()
def mark_done():
    tk = tasklst.curselection()
    idx = tk[0]
    tasks[idx] = tasks[idx] + " (Done)"
    status.config(text="Marked as Done")
    update_listbox()
def update_listbox():
    tasklst.delete(0,END)
    for task in tasks:
        tasklst.insert(END,task)

root = Tk()
root.title("To-Do List Application")
root.geometry("500x500")

Label(root,text="Task",font="lucida 18").grid(row=0,column=0,padx=60)

task_var = StringVar()
Entry(root,textvariable=task_var).grid(row=0,column=1)

Button(root,text="Add Task",command=add_task).grid(row=1,column=1,pady=5)
Button(root,text="Delete Task",command=remove_task).grid(row=2,column=1,pady=5)
Button(root,text="Mark as Done",command=mark_done).grid(row=3,column=1,pady=5)

tasks = []

tasklst = Listbox(root,font="lucida 18")
tasklst.grid(row=4,column=0,padx=10)

scr = Scrollbar(root)
scr.grid(row=4,column=1,sticky=NS)
scr.config(command=tasklst.yview)
tasklst.config(yscrollcommand=scr.set)

status = Label(root,text="",fg="red")
status.grid(row=5,column=0)

root.mainloop()