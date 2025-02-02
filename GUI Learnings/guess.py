from tkinter import *
from random import randint
from tkinter.messagebox import showinfo
a = randint(0,100)

def enter(self):
    no = int(str.get())
    listbox.insert(END,no)
    str.set("")
    if no == a:
        r = listbox.size()
        b.config(text=f"You Won in {r}th attempt")
    if no < a:
        b.config(text="Greater No. Please")
    if no > a:
        b.config(text="Smaller No. Please")
def help():
    showinfo("How to play","System will decide a no. between 1-100 and you have to guess that no. if you choose smaller no. than system, you will get (greater no. please) message and same as for greater no.")
def restart():
    global a
    str.set("")
    listbox.delete(0,END)
    b.config(text="")
    a = randint(0,100)
root=Tk()
root.geometry("500x500")
root.resizable(False,False)
root.iconbitmap(r"C:\Users\ASUS\Documents\basic\favicon.ico")
root.title("Guess The Number Game - ( Mohit Kumar )")
Label(root,text="Guess the number between 1-100",font="lucida 18",bg="green",fg="blue",pady=10).pack(anchor=N,fill=X,pady=10)
str = StringVar()
Label(root,text="Enter No.").pack(side=LEFT,anchor=NW,padx=50,pady=20)
e = Entry(root,textvariable=str,fg="green")
e.pack(anchor=NW,pady=20)
e.bind("<Return>",enter)
Button(root,text="Enter",fg="green",font="lucida 25",command=enter).pack(anchor=NE,padx=30)
listbox = Listbox(root,fg="blue")
listbox.pack(side=LEFT)
b = Label(root,text="",fg="red")
b.pack()
m = Menu(root)
m1 = Menu(m,tearoff=0)
m1.add_command(label="Help",command=help)
m.add_cascade(label="Help",menu=m1)
root.config(menu=m)
Button(text="Restart",command=restart,fg="blue",font="lucida 16 bold").pack()
root.mainloop()