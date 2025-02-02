from tkinter import *

def showmainframe():
    for item in b.winfo_children():
        item.destroy()
    Label(b,text="This is primary frame").pack(pady=50)

def first():
    global b
    for item in b.winfo_children():
        item.destroy()
    
def second():
    for item in b.winfo_children():
        item.destroy()
    Label(b,text="This is second game").pack(pady=50)


root = Tk()
root.title("New Testing")
root.geometry("600x400")

a = Frame(root,border=5,relief="sunken",width=150,height=2000)
a.pack(side=LEFT,fill=BOTH)
Button(a,text="First game",command=first).pack(pady=20,padx=20)
Button(a,text="second game",command=second).pack(pady=20,padx=20)





b = Frame(root,border=5,relief="sunken",width=2000,height=2000)
b.pack(fill=BOTH,expand=True)

menu = Menu(root)
root.config(menu=menu)

help = Menu(menu,tearoff=0)
help.add_command(label="My")
menu.add_cascade(label="help",menu=help)

showmainframe()




root.mainloop()