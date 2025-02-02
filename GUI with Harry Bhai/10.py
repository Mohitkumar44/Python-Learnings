from tkinter import *
root=Tk()
root.geometry("800x500")

myslider = Scale(root,from_=0,to=10)
myslider.pack()

myslider = Scale(root,from_=0,to=10,orient=HORIZONTAL)
myslider.pack()


root.mainloop()