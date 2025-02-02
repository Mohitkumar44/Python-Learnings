from tkinter import *

def add():
    m = name_var.get()
    if m not in lt:
        lt.append(m)
        name_var.set("")
        update_listbox()
    else:
        status.config(text="Contact already exists")
def view():
    update_listbox()
def delete():
    k=name_var.get()
    if k in lt:
        lt.remove(k)
        name_var.set("")
        update_listbox()
    else:
        status.config(text="Contact not found")
def search():
    j = name_var.get()
    lst.delete(0,END)
    if j in lt:
        lst.insert(END,j)
    else:
        status.config(text="Contact not found")
def update_listbox():
    lst.delete(0,END)
    for item in lt:
        lst.insert(END,item)
root=Tk()
lt = ["Mohit","Kanha","Rohit"]

lst =Listbox(root)
lst.grid(row=7,column=1)
root.title("Contact Management System")
root.geometry("500x470")
Name =Label(root,text="Name",font="lucida 18")
Number =Label(root,text="Phone Number",font="lucida 18",padx=50)
Email =Label(root,text="Email",font="lucida 18")
Name.grid(row=0,column=0)
Number.grid(row=1,column=0)
Email.grid(row=2,column=0)
name_var = StringVar()
number_var = StringVar()
email_var = StringVar()
n1 = Entry(root,textvariable=name_var)
n2 = Entry(root,textvariable=number_var)
n3 = Entry(root,textvariable=email_var)
n1.grid(row=0,column=1)
n2.grid(row=1,column=1)
n3.grid(row=2,column=1)
add = Button(root,text="Add Contact",command=add)
view = Button(root,text="View Contact",command=view)
delete = Button(root,text="Delete",command=delete)
search = Button(root,text="Search Contact",command=search)
add.grid(row=3,column=1)
view.grid(row=4,column=1)
delete.grid(row=5,column=1)
search.grid(row=6,column=1)
status = Label(root,text="",fg="red")
status.grid(row=8,column=1)

root.mainloop()