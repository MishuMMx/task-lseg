import tkinter as tk
from tkinter import filedialog

def select_folder():
    # Hide the root window
    root = tk.Tk()
    root.withdraw()

    # Show folder selection dialog
    selected_folder = filedialog.askdirectory(title="Select Folder")

    # Return the selected folder path
    return selected_folder

