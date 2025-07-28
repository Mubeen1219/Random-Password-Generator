import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # Clipboard integration

# Generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        char_pool = ""
        if var_letters.get():
            char_pool += string.ascii_letters
        if var_numbers.get():
            char_pool += string.digits
        if var_symbols.get():
            char_pool += string.punctuation

        if not char_pool:
            messagebox.showerror("Input Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(char_pool) for _ in range(length))
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for length.")

# Copy password
def copy_password():
    password = result_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# GUI Setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.configure(bg="#f0f0f0")

tk.Label(window, text="Password Length:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(window, font=("Arial", 12))
length_entry.pack()

# Character type options
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(window, text="Include Letters", variable=var_letters, bg="#f0f0f0").pack()
tk.Checkbutton(window, text="Include Numbers", variable=var_numbers, bg="#f0f0f0").pack()
tk.Checkbutton(window, text="Include Symbols", variable=var_symbols, bg="#f0f0f0").pack()

tk.Button(window, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

result_var = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result_var, font=("Arial", 12), width=30, justify="center")
result_entry.pack(pady=5)

tk.Button(window, text="Copy to Clipboard", command=copy_password, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=10)

window.mainloop()
