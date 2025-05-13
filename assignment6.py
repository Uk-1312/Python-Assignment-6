# calculator.py

import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            screen.set("")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create main window
root = tk.Tk()
root.geometry("400x500")
root.title("Simple Calculator")

# Entry field for display
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, relief=tk.SUNKEN, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Define button layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief=tk.RAISED, bd=5)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

# Start the application
root.mainloop()
