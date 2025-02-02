from tkinter import *
root=Tk()
def lab():
    Label(root,text="Information Submitted").grid(row=5,column=1)
root.geometry("400x300")
root.title("Student Information")
Label(root,text="Students Name").grid(row=1,column=0)
Label(root,text="Roll Number",padx=50).grid(row=2,column=0)
Label(root,text="Course").grid(row=3,column=0)
Entry(root).grid(row=1,column=1)
Entry(root).grid(row=2,column=1)
Entry(root).grid(row=3,column=1)
Button(root,text="Submit",command=lab).grid(row=4,column=1)
root.mainloop()