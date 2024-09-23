import tkinter as tk
from tkinter import messagebox

msg = "Test"

def show_popup_msg(msg):
    root = tk.Tk()
    root.withdraw()  
    messagebox.showerror(msg)