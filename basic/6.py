from tkinter import *
def showframe(level):
    for item in mainframe.winfo_children():
        item.destroy()
    if level == 1:
        Label(mainframe,text="this is fisrt level").pack(pady=20)
        Button(mainframe,text="go to level 2",command=lambda: showframe(2)).pack(pady=20)
        Button(mainframe,text="back",command=showmainframe).pack(pady=20)
    elif level == 2:
        Label(mainframe,text="this is second level").pack(pady=20)
        Button(mainframe,text="go to level 3",command=lambda: showframe(3)).pack(pady=20)
        Button(mainframe,text="back",command=lambda: showframe(1)).pack(pady=20)
    elif level == 3:
        Label(mainframe,text="this is third level").pack(pady=20)
        Button(mainframe,text="go to level 4",command=lambda: showframe(4)).pack(pady=20)
        Button(mainframe,text="back",command=lambda: showframe(2)).pack(pady=20)
    elif level == 4:
        Label(mainframe,text="this is fourth level").pack(pady=20)
        Button(mainframe,text="back",command=lambda: showframe(3)).pack(pady=20)
def showmainframe():
    for item in mainframe.winfo_children():
        item.destroy()
    label = Label(mainframe,text="Primary Window")
    label.pack(pady=20)
    button = Button(mainframe,text="Go to level 1",command=lambda:showframe(1))
    button.pack(pady=20)
root=Tk()
root.title("Testing")
root.geometry("300x200")
mainframe = Frame(root)
mainframe.pack(fill=BOTH,expand=True)
showmainframe()
root.mainloop()