from tkinter import *

root = Tk()
a = 800
b = 500

root.geometry(f"{a}x{b}")

r = Canvas(root,width=a,height=b)
r.pack()

r.create_rectangle(10,10,500,500,fill="red")

root.mainloop()