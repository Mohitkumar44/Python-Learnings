from tkinter import *
import tkinter.messagebox as tmsg

# basic gui operations
root=Tk()
root.title("Untitled-Notepad")
root.geometry("875x554")
root.iconbitmap(r"C:\Users\ASUS\Downloads\Notepad_23093.ico")

# making functions
def myfunc():
    print("It Works")

def help():
    print("Asking For Help")
    tmsg.showinfo("Help","Notepad By Mohit Kumar")

def rate():
    print("Asking For Rating")
    a=tmsg.askquestion("Feedback","Would You Like It")
    if a == "yes":
        msg="Rate us on app store"
    else:
        msg="Our team is working on issues"
    tmsg.showinfo("Feedback",msg)

def cut():
    text.event_generate(("<<cut>>"))


# creating menues starts
mymenu = Menu(root)
    # for file menu
m1 = Menu(mymenu,tearoff=0)
m1.add_command(label="New Tab",command=myfunc)
m1.add_command(label="New Window",command=myfunc)
m1.add_command(label="Open",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Save All",command=myfunc)
m1.add_separator()
m1.add_command(label="Page Setup",command=myfunc)
m1.add_command(label="Print",command=myfunc)
m1.add_separator()
m1.add_command(label="Close Tab",command=myfunc)
m1.add_command(label="Close Window",command=myfunc)
m1.add_command(label="Exit",command=myfunc)

mymenu.add_cascade(label="File",menu=m1)

    # for edit menu
m2 = Menu(mymenu,tearoff=0)
m2.add_command(label="Undo",command=myfunc)
m2.add_separator()
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Delete",command=myfunc)
m2.add_separator()
m2.add_command(label="Define With Bing",command=myfunc)
m2.add_separator()
m2.add_command(label="Find",command=myfunc)
m2.add_command(label="Find Next",command=myfunc)
m2.add_command(label="Find Previous",command=myfunc)
m2.add_command(label="Replace",command=myfunc)
m2.add_command(label="Go to",command=myfunc)
m2.add_separator()
m2.add_command(label="Select all",command=myfunc)
m2.add_command(label="Time/Date",command=myfunc)
m2.add_separator()
m2.add_command(label="Font",command=myfunc)

mymenu.add_cascade(label="Edit",menu=m2)

    # for view menu
m3 = Menu(mymenu,tearoff=0)
m5 = Menu(m3,tearoff=0)
m5.add_command(label="Zoom in",command=myfunc)
m5.add_command(label="Zoom out",command=myfunc)
m3.add_cascade(label="Zoom",menu=m5)
m3.add_command(label="Status bar",command=myfunc)
m3.add_command(label="Word wrap",command=myfunc)


mymenu.add_cascade(label="View",menu=m3)

    # for help menu
m4 = Menu(mymenu,tearoff=0)
m4.add_command(label="Help",command=help)
m4.add_command(label="Rate us",command=rate)
mymenu.add_cascade(label="Help",menu=m4)
# creating menues ends


root.config(menu=mymenu)

# scrollbar making
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

# textarea making
text = Text(root,yscrollcommand=scrollbar.set,font="lucida 12")
text.pack(expand=True,fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()