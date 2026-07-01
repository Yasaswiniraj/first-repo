import tkinter as tk


# ---------------- Functions ---------------- #

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


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

        if text == "=":
            command = calculate
        elif text == "C":
            command = clear
        else:
            command = lambda x=text: button_click(x)

        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 18, "bold"),
            command=command,
            bg="white",
            activebackground="#dcdcdc"
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