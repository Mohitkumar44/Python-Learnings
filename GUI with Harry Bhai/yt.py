import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("YouTube-like GUI")
root.geometry("800x600")

# Header
header_frame = tk.Frame(root, bg="red", height=50)
header_frame.pack(fill=tk.X, side=tk.TOP)

logo_label = tk.Label(header_frame, text="YouTube", font=("Arial", 24), bg="red", fg="white")
logo_label.pack(side=tk.LEFT, padx=20)

search_frame = tk.Frame(header_frame, bg="white")
search_frame.pack(side=tk.LEFT, padx=20, fill=tk.X, expand=True)

search_entry = tk.Entry(search_frame, font=("Arial", 16))
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

search_button = tk.Button(search_frame, text="Search", font=("Arial", 16))
search_button.pack(side=tk.RIGHT)

# Sidebar
sidebar_frame = tk.Frame(root, bg="lightgray", width=200)
sidebar_frame.pack(fill=tk.Y, side=tk.LEFT)

sidebar_button = tk.Button(sidebar_frame, text="Home", font=("Arial", 16), bg="lightgray")
sidebar_button.pack(fill=tk.X)

sidebar_button = tk.Button(sidebar_frame, text="Subscriptions", font=("Arial", 16), bg="lightgray")
sidebar_button.pack(fill=tk.X)

# Main content area
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

video_frame = tk.Frame(content_frame, bg="black", height=200)
video_frame.pack(fill=tk.X, pady=10)

video_label = tk.Label(video_frame, text="Video Player", bg="black", fg="white", font=("Arial", 20))
video_label.pack()

# Footer
footer_frame = tk.Frame(root, bg="gray", height=30)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

footer_label = tk.Label(footer_frame, text="Footer", bg="gray", fg="white", font=("Arial", 12))
footer_label.pack()

# Run the application
root.mainloop()
