from tkinter import *
root = Tk()
canvas_width = 800
canvas_height = 500
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
can_widget.create_line(0,0,200,200,fill = "red")
root.mainloop()