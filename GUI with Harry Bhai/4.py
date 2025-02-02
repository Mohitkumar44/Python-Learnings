from tkinter import *

root=Tk()
root.title("Dance Form")
root.geometry("800x500")

def printit():
    print(nameentry.get())
    print(ageentry.get())


name = Label(root,text="Enter Name ")
name.grid(row=0,column=0)

age = Label(root,text="Enter Age     ")
age.grid(row=1,column=0)

namevalue = StringVar()
agevalue = StringVar()

nameentry = Entry(root,textvariable=namevalue)
ageentry = Entry(root,textvariable=agevalue)

nameentry.grid(row=0,column=1)
ageentry.grid(row=1,column=1)

Button(root,text="Print",command=printit).grid(row=2,column=0)

root.mainloop()