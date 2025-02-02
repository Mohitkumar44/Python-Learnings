from tkinter import *
root=Tk()

root.geometry("800x500")
root.title("The Indian News")


f1= Frame(root,borderwidth=9)
f1.pack()


Label(f1,text="The Indian Newspaper",font="lucida 20 bold").pack()
Label(f1,text="July 16, 2024",font="arail 10 bold").pack()

def every_100(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text += text[i]
        if i%100 == 0 and i != 0:
            final_text += "\n"
    return final_text


texts = []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

r1 = Frame(root,borderwidth=9)
r1.pack(anchor="w")

Label(r1,text=texts[0],font="Arial 7 bold",padx=22, pady=22).pack()

root.mainloop()