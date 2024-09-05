import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
class UI():

    entries: list[tk.Entry]
    ingredient_list: list[str]
    FILE_PATH: str

    def __init__(self):

        #create the main window 
        self.window = tk.Tk()
        self.window.title("Recipe Book")

        #file path
        FILE_PATH = "C:/Users/subotovic/Desktop/Code/Einkaufsliste/food.txt"
        
        #define instance variables
        self.flag: bool = False
        self.i = 0
        self.ingredient_list = []

        #parse the file
        self.parse_ingredients(FILE_PATH)

        #define string variables for the entries 
        self.vars = [tk.StringVar() for var in range(10)]
        self.combvar = tk.StringVar()
        self.combvar1 = tk.StringVar()

        #define the entries in the window
        self.entries = [tk.Entry(self.window, textvariable=self.vars[i]) for i in range(5)]

        #position self.entries 
        self.define_entries()

        state = self.entries[0]

        #bind buttons
        self.bind_button()

        #define the labels in the window
        self.define_labels()

        #define a button 
        self.define_buttons()

        #define a combobox
        self.define_combobox()
    
        # Start the event loop.
        self.window.mainloop()

    def define_entries(self):
        self.entries[0].grid(row = 0, column = 1, padx=5, pady=5)
        self.entries[1].grid(row = 3, column = 1, padx=5, pady=5)
        self.entries[2].grid(row = 4, column = 1, padx=5, pady=5)
        self.entries[3].grid(row = 5, column = 1, padx=5, pady=5)
        self.entries[4].grid(row = 6, column = 1, padx=5, pady=5)

    def define_labels(self):
        #define the labels in the window
        tk.Label(self.window, text = "Enter the recipe name: ").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the recipe category: ").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the ingredient: ").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the ingredient subcategory (optional): ").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "Enter the amount: ").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(self.window, text = "in g").grid(row = 4, column = 2)
        tk.Label(self.window, text = "in ml").grid(row = 5, column = 2)
        tk.Label(self.window, text = "in units").grid(row = 6, column= 2)

    def bind_button(self):
        self.window.bind('<Return>', self.handle_button_press)

    def define_combobox(self):
        #define a combobox
        self.c0 = ttk.Combobox(self.window, values=self.ingredient_list,  textvariable=self.combvar)
        self.c1 = ttk.Combobox(self.window, values=["breakfast", "dinner"], textvariable=self.combvar1)

        self.c0.grid(row = 2, column = 1)
        self.c1.grid(row = 1, column = 1)

    def define_buttons(self):
        #define a button 
        button = tk.Button(text="Next ingredient", command=self.handle_button_press)
        button.grid(row = 7, column = 1, pady=10)

    def parse_ingredients(self, text: str) -> None:
        #open the file
        with open(text, "r", encoding="utf-8") as file:
            for line in file:
                self.ingredient_list.append(line.strip())

    def get_state(self, entry):
        pass

    def disable_entry(self, event):
        #once button is pressed save the variable data to the list
        dir = "C:/Users/subotovic/Desktop/Code/Einkaufsliste/ingredient.txt"
        if not os.path.exists(dir):
            with open(dir, 'w') as f:
                f.write('')  # create an empty file

        #write the recipe name if the 
        with open(dir, "a") as f:
            if self.flag == False:
                f.write("recipe name: " + self.vars[0].get() + "\n")
                f.write("category: " + self.combvar1.get() + "\n")
                #disable the state of the self.entries and combobox
                self.entries[0].config(state="disabled")
                self.c1.config(state="disabled")
                self.flag = True

            f.write("ingredient: " + self.combvar.get() + "\n")
            f.write("subcategory: " + self.vars[1].get() + "\n")
            if self.vars[2].get() != "":
                f.write("ammount: " + self.vars[2].get() + " g \n")
            elif self.vars[3].get() != "":
                f.write("ammount: " + self.vars[3].get() + " ml \n")
            elif self.vars[4].get() != "":
                f.write("ammount: " + self.vars[4].get() + " units \n")

        [entry.delete(0, tk.END) for entry in self.entries[1:]]

    #after the button is pressed save the variable data in 
    #specific format and reset the inactive windows
    def handle_button_press(self, event = None):
        #once button is pressed save the variable data to the list
        dir = "C:/Users/subotovic/Desktop/Code/Einkaufsliste/ingredient.txt"
        if not os.path.exists(dir):
            with open(dir, 'w') as f:
                f.write('')  # create an empty file

        #if any of the fields are empty do not execute the function further just return 
        if any([var == "" for var in\
            [self.vars[0].get(), self.combvar1.get(), self.combvar.get()]]):
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return

        #write the recipe name if the 
        with open(dir, "a") as f:
            if self.flag == False:
                f.write("recipe name: " + self.vars[0].get() + "\n")
                f.write("category: " + self.combvar1.get() + "\n")
                #disable the state of the self.entries and combobox
                self.entries[0].config(state="disabled")
                self.c1.config(state="disabled")
                self.flag = True

            f.write("ingredient: " + self.combvar.get() + "\n")
            f.write("subcategory: " + self.vars[1].get() + "\n")
            if self.vars[2].get() != "":
                f.write("ammount: " + self.vars[2].get() + " g \n")
            elif self.vars[3].get() != "":
                f.write("ammount: " + self.vars[3].get() + " ml \n")
            elif self.vars[4].get() != "":
                f.write("ammount: " + self.vars[4].get() + " units \n")

        [entry.delete(0, tk.END) for entry in self.entries[1:]]

        #disable the buttons and self.entries and clear them 

if __name__ == "__main__":
    ui_instance = UI()