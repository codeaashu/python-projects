import tkinter as tk

def decimal_to_binary():
    try:
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b", "")
        output_label.config(text=f"Binary: {binary_num}")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a decimal number.")

def binary_to_decimal():
    try:
        binary_num = input_field.get()
        decimal_num = int(binary_num, 2)
        output_label.config(text=f"Decimal: {decimal_num}")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a valid binary number.")

def clear_output():
    output_label.config(text="")

root = tk.Tk()
root.title("Binary-Decimal Converter")

menu_frame = tk.Frame(root)
menu_frame.pack()

decimal_to_binary_button = tk.Button(menu_frame, text="Decimal to Binary", command=decimal_to_binary)
decimal_to_binary_button.pack(side=tk.LEFT)

binary_to_decimal_button = tk.Button(menu_frame, text="Binary to Decimal", command=binary_to_decimal)
binary_to_decimal_button.pack(side=tk.LEFT)

clear_button = tk.Button(root, text="Clear", command=clear_output)
clear_button.pack()

input_field = tk.Entry(root)
input_field.pack()

convert_button = tk.Button(root, text="Convert", command=lambda: None)  # Placeholder for now
convert_button.pack()

output_label = tk.Label(root, text="", pady=10)
output_label.pack()

root.mainloop()