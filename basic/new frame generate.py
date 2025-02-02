from tkinter import *

def show_new_frame():
    # Pehle se existing frame ko destroy karte hain agar hai toh
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Nayi window ke liye ek frame create karte hain
    new_frame = Frame(main_frame)
    new_frame.pack(fill="both", expand=True)

    label = Label(new_frame, text="This is the new window in the same window!")
    label.pack(pady=20)

    back_button = Button(new_frame, text="Go Back", command=show_main_frame)
    back_button.pack(pady=10)

def show_main_frame():
    # Main frame pehle waapas laate hain
    for widget in main_frame.winfo_children():
        widget.destroy()

    main_label = Label(main_frame, text="Main Window")
    main_label.pack(pady=20)

    new_window_button = Button(main_frame, text="Open New Window", command=show_new_frame)
    new_window_button.pack(pady=10)

root = Tk()
root.title("Single Window App")
root.geometry("300x200")

main_frame = Frame(root)
main_frame.pack(fill="both", expand=True)

show_main_frame()

root.mainloop()
