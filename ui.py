import tkinter as tk
from tkinter import ttk

root = tk.Tk()


# Centering Window
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = (screen_width - width) // 2
    center_y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{center_x}+{center_y}")

# Create Window
def create_windows():
    # Windows Details
    root.title("Invoice Generator App")
    root.iconbitmap("./icon/favicon.ico")    

    # Centering Windows on Screen
    center_window(root, 800, 600)

    # Creating Windows
    root.mainloop()

# Render Windows
create_windows()

