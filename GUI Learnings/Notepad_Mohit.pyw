from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

if __name__=='__main__':

    def newfile():
        global file
        root.title("Untitled - Notepad")
        file = None
        textarea.delete(1.0,END)

    def openfile():
        global file
        file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file)+" - Notepad")
            textarea.delete(1.0,END)
            f = open(file,"r")
            textarea.insert(1.0,f.read())
            f.close()

    def save():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if file == "":
                file = None
            else:
                f = open(file,"w")
                f.write(textarea.get(1.0,END))
                f.close()

                root.title(os.path.basename(file)+" - Notepad")
                print("File Saved Successfully")
        else:
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
    def Quit():
        root.destroy()
    
    def cut():
        textarea.event_generate(("<<Cut>>"))
    
    def copy():
        textarea.event_generate(("<<Copy>>"))
    
    def paste():
        textarea.event_generate(("<<Paste>>"))
    
    def about():
        showinfo("Notepad","Notepad by Mohit Kumar")
    
    # basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.iconbitmap(r"C:\Users\ASUS\Downloads\Notepad_23093.ico")
    root.geometry("875x510")
    
    # Adding Text Area
    textarea = Text(root,font="lucida 12")
    file = None
    textarea.pack(expand=True,fill=BOTH)

    # creating menu bar
    MenuBar = Menu(root)

    # file menu starts
    Filemenu = Menu(MenuBar,tearoff=0)

        # to open new file, to open a existing file and for save
    Filemenu.add_command(label="New",command=newfile)
    Filemenu.add_command(label="Open",command=openfile)
    Filemenu.add_command(label="Save",command=save)

    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=Quit)
    MenuBar.add_cascade(label="File",menu=Filemenu)
    # file menu ends

    # edit menu starts
    Editmenu = Menu(MenuBar,tearoff=0)

        # to give features for cut, copy and paste
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=Editmenu)
    # edit menu ends

    # help menu starts
    Helpmenu = Menu(MenuBar,tearoff=0)
    Helpmenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=Helpmenu)
    # help menu ends

    root.config(menu=MenuBar)
    
    # adding Scrollbar
    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)


    root.mainloop()