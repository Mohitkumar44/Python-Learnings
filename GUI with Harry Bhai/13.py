from tkinter import *
root=Tk()
root.geometry("400x400")

Scrollbar=Scrollbar(root)
Scrollbar.pack(side=RIGHT,fill=Y)

listbox = Listbox(root,yscrollcommand=Scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item {i}")

listbox.pack()

Scrollbar.config(command=listbox.yview)
root.mainloop()