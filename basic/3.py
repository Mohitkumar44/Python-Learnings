from tkinter import *
def secondwindow():
    # destroy
    for b in mainframe.winfo_children():
        b.destroy()
    
    label = Label(mainframe,text="Second window")
    label.pack(pady=20)

    Button(mainframe,text="Go back",command=showmainframe).pack(pady=20)
def showmainframe():
    # destroy
    for a in mainframe.winfo_children():
        a.destroy()

    label = Label(mainframe,text="Primary window")
    label.pack(pady=20)

    Button(mainframe,text="Next window",command=secondwindow).pack(pady=20)

root = Tk()
root.title("Single Window App")
root.geometry("300x200")
mainframe = Frame(root)
mainframe.pack(fill=BOTH,expand=True)
showmainframe()
root.mainloop()