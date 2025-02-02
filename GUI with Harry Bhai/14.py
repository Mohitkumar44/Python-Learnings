from tkinter import *
root = Tk()
root.geometry("500x300")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

text = Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()