from tkinter import *

def show_frame(level):
    # Current frame ko destroy karte hain
    for widget in main_frame.winfo_children():
        widget.destroy()

    if level == 1:
        # Level 1 ke liye frame
        new_frame = Frame(main_frame)
        new_frame.pack(fill="both", expand=True)

        Label(new_frame, text="This is Level 1").pack(pady=20)
        Button(new_frame, text="Go to Level 2", command=lambda: show_frame(2)).pack(pady=10)
        Button(new_frame, text="Back", command=show_main_frame).pack(pady=10)

    elif level == 2:
        # Level 2 ke liye frame
        new_frame = Frame(main_frame)
        new_frame.pack(fill="both", expand=True)

        Label(new_frame, text="This is Level 2").pack(pady=20)
        Button(new_frame, text="Go to Level 3", command=lambda: show_frame(3)).pack(pady=10)
        Button(new_frame, text="Back", command=lambda: show_frame(1)).pack(pady=10)

    elif level == 3:
        # Level 3 ke liye frame
        new_frame = Frame(main_frame)
        new_frame.pack(fill="both", expand=True)

        Label(new_frame, text="This is Level 3").pack(pady=20)
        Button(new_frame, text="Back", command=lambda: show_frame(2)).pack(pady=10)

def show_main_frame():
    # Main frame pehle waapas laate hain
    for widget in main_frame.winfo_children():
        widget.destroy()

    Label(main_frame, text="Main Window").pack(pady=20)
    Button(main_frame, text="Go to Level 1", command=lambda: show_frame(1)).pack(pady=10)

root = Tk()
root.title("Multi-Level Window App")
root.geometry("300x200")

main_frame = Frame(root)
main_frame.pack(fill="both", expand=True)

show_main_frame()

root.mainloop()
