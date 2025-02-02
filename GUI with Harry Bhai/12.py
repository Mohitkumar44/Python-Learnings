from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("410x200")
root.title("Radiaobutton Tutorial")

def func():
    tmsg.showinfo("Order Placed",f"Your Order for {var.get()} has been placed")


Label(root,text="What would you like to have sir?",font="lucida 19 bold").pack(pady=10)

var = StringVar()
var.set("ok")

radio = Radiobutton(root,text="Dosa",padx=20,variable=var,value="Dosa").pack(anchor='w')
radio = Radiobutton(root,text="Idly",padx=20,variable=var,value="Idly").pack(anchor='w')
radio = Radiobutton(root,text="Paratha",padx=20,variable=var,value="Paratha").pack(anchor='w')
radio = Radiobutton(root,text="Samosa",padx=20,variable=var,value="Samosa").pack(anchor='w')

Button(root,text="Order Now",command=func).pack()

root.mainloop()