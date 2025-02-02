from tkinter import *

def add():
    status.config(text="")
    m = name_var.get()
    if m:
        if m not in lt:
            lt.append(m)
            name_var.set("")
            update_listbox()
            status.config(text="Contact added", fg="green")
        else:
            status.config(text="Contact already exists", fg="red")
    else:
        status.config(text="Please enter a name", fg="red")

def view():
    status.config(text="")
    update_listbox()

def delete():
    status.config(text="")
    k = name_var.get()
    if k:
        if k in lt:
            lt.remove(k)
            name_var.set("")
            update_listbox()
            status.config(text="Contact deleted", fg="green")
        else:
            status.config(text="Contact not found", fg="red")
    else:
        status.config(text="Please enter a name", fg="red")

def search():
    status.config(text="")
    j = name_var.get()
    lst.delete(0, END)
    if j:
        found = False
        for item in lt:
            if j.lower() in item.lower():
                lst.insert(END, item)
                found = True
        if not found:
            status.config(text="Contact not found", fg="red")
    else:
        update_listbox()

def update_listbox():
    lst.delete(0, END)
    for item in lt:
        lst.insert(END, item)

root = Tk()
lt = ["Mohit", "Kanha", "Rohit"]

lst = Listbox(root)
lst.grid(row=7, column=1)

root.title("Contact Management System")
root.geometry("500x470")

Name = Label(root, text="Name", font="lucida 18")
Number = Label(root, text="Phone Number", font="lucida 18", padx=50)
Email = Label(root, text="Email", font="lucida 18")

Name.grid(row=0, column=0)
Number.grid(row=1, column=0)
Email.grid(row=2, column=0)

name_var = StringVar()
number_var = StringVar()
email_var = StringVar()

n1 = Entry(root, textvariable=name_var)
n2 = Entry(root, textvariable=number_var)
n3 = Entry(root, textvariable=email_var)

n1.grid(row=0, column=1)
n2.grid(row=1, column=1)
n3.grid(row=2, column=1)

add_button = Button(root, text="Add Contact", command=add)
view_button = Button(root, text="View Contact", command=view)
delete_button = Button(root, text="Delete", command=delete)
search_button = Button(root, text="Search Contact", command=search)

add_button.grid(row=3, column=1)
view_button.grid(row=4, column=1)
delete_button.grid(row=5, column=1)
search_button.grid(row=6, column=1)

status = Label(root, text="", fg="red")
status.grid(row=8, column=1)

root.mainloop()
