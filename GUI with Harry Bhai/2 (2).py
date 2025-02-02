from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.var = StringVar()
    def label(self,name):
        Label(self,text=name).pack(side=LEFT,padx=50)
    def addentry(self):
        Entry(self,textvariable=self.var,width="30").pack(side=LEFT)
    def savebutton(self,var):
        Button(self,text=var,command=self.save).pack(side=LEFT,padx=20)
    def save(self):
        c = self.var.get()
        with open("save.txt","w") as f:
            f.write(c)
if __name__=='__main__':
    window = GUI()
    window.label("Enter Your Name")
    window.addentry()
    window.savebutton("Save To File")
    window.mainloop()