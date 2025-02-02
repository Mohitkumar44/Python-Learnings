from tkinter import *
root=Tk()

root.title("Restaurent")
root.geometry("800x500")

def func():
    rating = slider.get()
    print(f"Your Ranting : {rating}")
    with open("rate.txt",'a') as f:
        f.write(f"\nYour Latest Rating : {rating}")
    print("Rating Saved Successfully!")


root.iconbitmap(r"C:\Users\ASUS\Downloads\favicon.ico")

f1 = Frame(root,borderwidth=5,relief=SUNKEN)
f1.pack(pady=30)

slider = Scale(root,from_=0,to=10,orient=HORIZONTAL)

slider.pack()

Label(f1,text="Thank You!",font="Arial 30 bold",fg="green").pack()

Button(root,text="Submit",command=func).pack()

root.mainloop()