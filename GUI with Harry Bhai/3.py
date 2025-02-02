from tkinter import *
root = Tk()
root.geometry("800x500")

def p1():
    print("Hello Mohit")

def p2():
    print("Hello Tushar")

def p3():
    print("Hello Kanha")

def p4():
    print("Hello Rohit")

frame = Frame(root,borderwidth=9,bg="grey",relief="sunken")
frame.pack(side=TOP,fill="x")

b1 = Button(frame,text="print = Hello Mohit",command = p1,fg="green")
b1.pack(side=LEFT)

b3 = Button(frame,text="print = Hello Tushar",command = p2,fg="red")
b3.pack(side=LEFT)

b2 = Button(frame,text="print = Hello Kanha",command = p3,fg="blue")
b2.pack(side=LEFT)

b4 = Button(frame,text="print = Hello Rohit",command = p4,fg="orange")
b4.pack(side=LEFT)




root.mainloop()