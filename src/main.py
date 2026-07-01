import tkinter as tk
from functools import partial


# ---------------- Functions ---------------- #

def set_display(value):
    """Clear display and set new value."""
    display.delete(0, tk.END)
    display.insert(tk.END, str(value))


def button_click(value):
    """Append value to current display."""
    current = display.get()
    set_display(current + value)


def clear():
    """Clear the display."""
    set_display("")


def backspace():
    """Remove last character from display."""
    current = display.get()
    set_display(current[:-1])


def calculate():
    """Evaluate the expression in the display."""
    try:
        result = eval(display.get())
        set_display(result)
    except (ValueError, SyntaxError, TypeError, ZeroDivisionError):
        set_display("Error")


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Calculator")
root.geometry("330x450")
root.resizable(False, False)

# ---------------- Display ---------------- #

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)

display.pack(fill="x", padx=10, pady=15)

# Bind keyboard events
root.bind("<Return>", lambda e: calculate())
root.bind("<BackSpace>", lambda e: backspace())
root.bind("<Escape>", lambda e: clear())

# Bind number and operator keys
for i in range(10):
    root.bind(str(i), lambda e, x=str(i): button_click(x))

root.bind("+", lambda e: button_click("+"))
root.bind("-", lambda e: button_click("-"))
root.bind("*", lambda e: button_click("*"))
root.bind("/", lambda e: button_click("/"))
root.bind(".", lambda e: button_click("."))

# ---------------- Button Frame ---------------- #

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in range(4):
    for col in range(4):
        text = buttons[row][col]

        # Determine command and styling
        if text == "=":
            command = calculate
            bg_color = "#90EE90"
        elif text == "C":
            command = clear
            bg_color = "#FFB6C6"
        else:
            command = partial(button_click, text)
            bg_color = "white"

        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 18, "bold"),
            command=command,
            bg=bg_color,
            activebackground="#dcdcdc",
            relief=tk.RAISED,
            bd=2
        )

        button.grid(
            row=row,
            column=col,
            padx=5,
            pady=5,
            sticky="nsew"
        )

# Make buttons expand equally
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
