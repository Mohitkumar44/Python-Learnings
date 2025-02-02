import tkinter as tk

class SlidingFrameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sliding Frame Example")
        self.geometry("600x400")

        self.frame = tk.Frame(self, width=100, height=100, bg="blue")
        self.frame.place(x=0, y=150)

        self.slide_button = tk.Button(self, text="Slide Frame", command=self.start_slide)
        self.slide_button.pack(pady=20)

    def start_slide(self):
        # Define the target position (end_x, end_y)
        end_x = 400
        end_y = 150
        self.animate_slide(self.frame, self.frame.winfo_x(), end_x, self.frame.winfo_y(), end_y, 10)

    def animate_slide(self, widget, start_x, end_x, start_y, end_y, step):
        dx = end_x - start_x
        dy = end_y - start_y
        distance = (dx**2 + dy**2)**0.5
        if distance > step:
            step_x = step * dx / distance
            step_y = step * dy / distance
            new_x = start_x + step_x
            new_y = start_y + step_y
            widget.place(x=new_x, y=new_y)
            self.after(10, self.animate_slide, widget, new_x, end_x, new_y, end_y, step)
        else:
            widget.place(x=end_x, y=end_y)

if __name__ == "__main__":
    app = SlidingFrameApp()
    app.mainloop()
