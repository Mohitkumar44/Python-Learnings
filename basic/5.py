from tkinter import *

def open_new_window():
    # Create a new Toplevel window
    new_window = Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")

    # Add a label to the new window
    label = Label(new_window, text="This is a new window", pady=20)
    label.pack()

    # Add a button to close the new window
    close_button = Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

# Main window
root = Tk()
root.title("Main Window")
root.geometry("400x300")

# Button to open a new Toplevel window
open_window_button = Button(root, text="Open New Window", command=open_new_window)
open_window_button.pack(pady=50)

root.mainloop()
