from tkinter import *
def nextwindow():
    newwin=Toplevel(root)
    newwin.title("next window")
    newwin.geometry("300x200")
    Label(newwin,text="this is new window").pack(pady=20)
    Button(newwin,text="close",command=newwin.destroy).pack(pady=20)

root=Tk()
root.title("Testing")
root.geometry("300x200")
Button(root,text="next window",command=nextwindow).pack(pady=20)
root.mainloop()