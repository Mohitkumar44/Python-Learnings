from tkinter import *

root = Tk()

root.geometry("800x500")
root.title("Mohit Kumar")

# root.maxsize(1000,900)

f1 = Frame(root,borderwidth=8,bg="grey",relief = "sunken")
f1.pack(side=LEFT,fill="y")

f2 = Frame(root,bg="grey",borderwidth=8,relief="sunken")
f2.pack(side=TOP,fill="x")

l = Label(f1,text="Side wali line",font = "Arial 16 bold",fg="red")
l.pack(pady=142,padx=9)

l = Label(f2,text="Top wali line",font= "arial 16 bold",fg="green")
l.pack(pady=45)

root.mainloop()