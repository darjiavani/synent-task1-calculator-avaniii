import tkinter as tk

# function to update expression
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

# function to clear
def clear():
    entry.delete(0, tk.END)

# function to calculate
def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# window
root = tk.Tk()
root.title("AVANI'S CALCULATOR")
root.geometry("300x400")

# entry box
entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# buttons frame
frame = tk.Frame(root)
frame.pack()

# buttons layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: calculate() if x == '=' else press(x)
        tk.Button(row_frame, text=btn, font=("Arial", 14),
                  command=action).pack(side="left", expand=True, fill="both")
        
       

# clear button
tk.Button(root, text="C", font=("Arial", 14), command=clear, bg="red", fg="white").pack(fill="both")
 # Backspace button
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])
    tk.Button(root, text="⌫", command=backspace).pack(fill="both")
root.mainloop()