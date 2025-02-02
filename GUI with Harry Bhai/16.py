from tkinter import *
def update():
    statusvar.set("Busy...")
    str.update()
    import time
    time.sleep(1)
    statusvar.set("Ready")
root=Tk()
root.geometry("500x300")
statusvar = StringVar()
statusvar.set("Ready")
str=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
str.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=update).pack()
root.mainloop()