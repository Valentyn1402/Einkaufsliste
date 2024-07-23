from tkinter import *
import tkinter as tk
from tkinter import ttk

#create the main window 
window = tk.Tk()
window.title("Recipe Book")

def handle_button_press():
    window.destroy()

#define the labels in the window
tk.Label(window, text = "Enter the recipe name: ").grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the recipe category: ").grid(row=1, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the ingredient: ").grid(row=2, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the ingredient subcategory (optional): ").grid(row=3, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the amount: ").grid(row=4, column=0, padx=5, pady=5)
tk.Label(window, text = "in g").grid(row = 4, column = 2)
tk.Label(window, text = "in ml").grid(row = 5, column = 2)
tk.Label(window, text = "in units").grid(row = 6, column= 2)

#define the entries in the window
b0 = tk.Entry(window)
b1 = tk.Entry(window)
b2 = tk.Entry(window)
b3 = tk.Entry(window)
b4 = tk.Entry(window)

b0.grid(row = 0, column = 1, padx=5, pady=5)
b1.grid(row = 3, column = 1, padx=5, pady=5)
b2.grid(row = 4, column = 1, padx=5, pady=5)
b3.grid(row = 5, column = 1, padx=5, pady=5)
b4.grid(row = 6, column = 1, padx=5, pady=5)

#define a button 
button = tk.Button(text="Next ingredient", command=handle_button_press)
button.grid(row = 7, column = 1, pady=10)

#define a combobox
c0 = ttk.Combobox(window, values=["Op1", "Op2", "Op3"])
c1 = ttk.Combobox(window, values=["Breakfast", "Dinner"])

c0.grid(row = 2, column = 1)
c1.grid(row = 1, column = 1)

# Start the event loop.
window.mainloop()