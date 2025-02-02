import tkinter as tk
import os

# Creating the main window
root = tk.Tk()
root.title("My GUI Application")

# A sample label
label = tk.Label(root, text="Hello, World!")
label.pack()

# Check if the program is running in a console and hide it
if os.name == 'nt':  # Windows
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Running the main loop
root.mainloop()
