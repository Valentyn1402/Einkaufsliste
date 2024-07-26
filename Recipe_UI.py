from tkinter import *
import tkinter as tk
from tkinter import ttk
import os

#create the main window 
window = tk.Tk()
window.title("Recipe Book")

flag: bool = False

i = 0

#define string variables for the entries 
vars = [tk.StringVar() for var in range(10)]
combvar = tk.StringVar()
combvar1 = tk.StringVar()

#define the entries in the window
entries = [tk.Entry(window, textvariable=vars[i]) for i in range(5)]

entries[0].grid(row = 0, column = 1, padx=5, pady=5)
entries[1].grid(row = 3, column = 1, padx=5, pady=5)
entries[2].grid(row = 4, column = 1, padx=5, pady=5)
entries[3].grid(row = 5, column = 1, padx=5, pady=5)
entries[4].grid(row = 6, column = 1, padx=5, pady=5)

def get_state(entry):
    pass

def disable_entry(event, previous_state = entries[0]):
    if current_entry == "disabled":
        previous_state = current_entry
        i += 1
        current_entry = entries[i]
    else:
        current_entry = previous_state
    current_entry.config(state="disabled")

#after the button is pressed save the variable data in 
#specific format and reset the inactive windows
def handle_button_press():
    global flag
    #once button is pressed save the variable data to the list
    dir = "ingredient.txt"
    if not os.path.exists(dir):
        with open(dir, 'w') as f:
            f.write('')  # create an empty file

    #write the recipe name if the 
    with open(dir, "a") as f:
        if flag == False:
            f.write("recipe name: " + vars[0].get() + "\n")
            f.write("category: " + combvar1.get() + "\n")
            #disable the state of the entries and combobox
            entries[0].config(state="disabled")
            c1.config(state="disabled")
            flag = True

        f.write("ingredient: " + combvar.get() + "\n")
        f.write("subcategory: " + vars[1].get() + "\n")
        if vars[2].get() != "":
            f.write("ammount: " + vars[2].get() + "\n")
        elif vars[3].get() != "":
            f.write("ammount: " + vars[3].get() + "\n")
        elif vars[4].get() != "":
            f.write("ammount: " + vars[4].get() + "\n")

    [entry.delete(0, tk.END) for entry in entries[1:]]

    #disable the buttons and entries and clear them 

#bind Enter key to disable_entry function
window.bind('<Return>', disable_entry) 

#define the labels in the window
tk.Label(window, text = "Enter the recipe name: ").grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the recipe category: ").grid(row=1, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the ingredient: ").grid(row=2, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the ingredient subcategory (optional): ").grid(row=3, column=0, padx=5, pady=5)
tk.Label(window, text = "Enter the amount: ").grid(row=4, column=0, padx=5, pady=5)
tk.Label(window, text = "in g").grid(row = 4, column = 2)
tk.Label(window, text = "in ml").grid(row = 5, column = 2)
tk.Label(window, text = "in units").grid(row = 6, column= 2)

#define a button 
button = tk.Button(text="Next ingredient", command=handle_button_press)
button.grid(row = 7, column = 1, pady=10)

#define a combobox
c0 = ttk.Combobox(window, values=["Op1", "Op2", "Op3"],  textvariable=combvar)
c1 = ttk.Combobox(window, values=["Breakfast", "Dinner"], textvariable=combvar1)

c0.grid(row = 2, column = 1)
c1.grid(row = 1, column = 1)

# Start the event loop.
window.mainloop()