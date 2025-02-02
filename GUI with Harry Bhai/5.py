from tkinter import *
root = Tk()

root.geometry("500x300")

def get():
    print("Value Submitted")

username = Label(root,text="Username")
password = Label(root,text="Password")

username.grid(row=0,column=1)
password.grid(row=1,column=1)

usernamevalue = StringVar
passwordvalue = StringVar

usernameentry = Entry(root,textvariable=usernamevalue)
passwordentry = Entry(root,textvariable=passwordvalue)

usernameentry.grid(row=0,column=3)
passwordentry.grid(row=1,column=3)

Button(root,text="Submit",command=get).grid(row=4,column=3)


root.mainloop()