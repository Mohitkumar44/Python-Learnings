from tkinter import *
root=Tk()
root.geometry("800x500")
images = PhotoImage(file="2.png")
Label(image=images).pack()

root.mainloop()