import num2words as n2w
from tkinter import *
from tkinter import messagebox

def num_to_words():
    try:
        given_num = float(num.get())
        num_in_word = n2w.num2words(given_num)
        display.config(text=str(num_in_word).capitalize())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = Tk()
root.title("Numbers to Words")
root.geometry("700x500")  # Adjusted window size

num = StringVar()

# Center title
title = Label(root, text="Number to Words Converter", fg="Blue", font=("Arial", 20, 'bold'))
title.pack(pady=10)

# Frame for formats to improve alignment
format_frame = Frame(root)
format_frame.pack(anchor="w", padx=30, pady=(10, 0))

formats_label = Label(format_frame, text="Formats supported:", fg="green", font=("Arial", 10, 'bold'))
formats_label.grid(row=0, column=0, sticky="w")

# Descriptions with more spacing
Label(format_frame, text="1. Positives", fg="green", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=20)
Label(format_frame, text="2. Negatives", fg="green", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=20)
Label(format_frame, text="3. Zeros", fg="green", font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=20)
Label(format_frame, text="4. Floating points/decimals/fractions", fg="green", font=("Arial", 10)).grid(row=4, column=0, sticky="w", padx=20)

# Frame for entry and label
entry_frame = Frame(root)
entry_frame.pack(pady=20)

num_entry_label = Label(entry_frame, text="Enter a number:", fg="Blue", font=("Arial", 15, 'bold'))
num_entry_label.grid(row=0, column=0, sticky="e", padx=10)

num_entry = Entry(entry_frame, textvariable=num, width=30)
num_entry.grid(row=0, column=1, padx=10)

# Calculate button
btn = Button(root, text="Calculate", fg="green", font=("Arial", 10, 'bold'), command=num_to_words)
btn.pack(pady=10)

# Display result
display = Label(root, text="", fg="black", font=("Arial", 12, 'bold'))
display.pack(pady=20)

# Load image for icon if available
try:
    photo = PhotoImage(file=r"D:\vidyaPY\Beginner-Python-Projects-main\Num2Words\number.png")
    root.iconphoto(False, photo)
except Exception as e:
    print("Image for icon not found:", e)

root.mainloop()
