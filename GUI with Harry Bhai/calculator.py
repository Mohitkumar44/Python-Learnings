from tkinter import *

def screenupdate(val):
    current_val = scval.get()
    if current_val == "0":
        scval.set(val)
    if val == "clear":
        scval.set("")
    else:
        scval.set(current_val + val)
    screen.update()


root = Tk()
root.geometry("400x500")
root.iconbitmap(r"C:\Users\ASUS\Downloads\cal.ico")
root.title("Calculator by Mohit Kumar")


scval= StringVar()
scval.set("")
screen = Entry(root,textvariable=scval,font="lucida 40 bold")
screen.pack()



frame1 = Frame(bg="grey")
frame1.pack()

b9 = Button(frame1,text=9,font="lucida 35 bold",command=lambda: screenupdate("9"),padx=3)
b8 = Button(frame1,text=8,font="lucida 35 bold",command=lambda: screenupdate("8"),padx=3)
b7 = Button(frame1,text=7,font="lucida 35 bold",command=lambda: screenupdate("7"),padx=3)
bequal = Button(frame1,text="c",font="lucida 35 bold",command=lambda: screenupdate("clear"),padx=3)
b9.pack(side=LEFT)
b8.pack(side=LEFT)
b7.pack(side=LEFT)
bequal.pack(side=LEFT)

frame2= Frame(bg="grey")
frame2.pack()

b5 = Button(frame2,text=5,font="lucida 35 bold",command=lambda: screenupdate("5"),padx=3)
b6 = Button(frame2,text=6,font="lucida 35 bold",command=lambda: screenupdate("6"),padx=3)
b4 = Button(frame2,text=4,font="lucida 35 bold",command=lambda: screenupdate("4"),padx=3)
b6.pack(side=LEFT)
b5.pack(side=LEFT)
b4.pack(side=LEFT)

frame3 = Frame(bg="grey")
frame3.pack()

b3 = Button(frame3,text=3,font="lucida 35 bold",command=lambda: screenupdate("3"),padx=3)
b2 = Button(frame3,text=2,font="lucida 35 bold",command=lambda: screenupdate("2"),padx=3)
b1 = Button(frame3,text=1,font="lucida 35 bold",command=lambda: screenupdate("1"),padx=3)
b3.pack(side=LEFT)
b2.pack(side=LEFT)
b1.pack(side=LEFT)

frame = Frame(bg="grey")
frame.pack()

b00 = Button(frame,text="00",font="lucida 35 bold",command=lambda: screenupdate("00"))
b0 = Button(frame,text=0,font="lucida 35 bold",command=lambda: screenupdate("0"))
bp = Button(frame,text=".",font="lucida 35 bold",command=lambda: screenupdate("."))

b00.pack(side=LEFT)
b0.pack(side=LEFT)
bp.pack(side=LEFT)


root.mainloop()