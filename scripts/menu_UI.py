import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from grocceries_UI import Grocceries
# import customtkinter as ctk 


class App(ctk.CTk):

    def __init__(self) -> None:

        super().__init__()

        ctk.set_appearance_mode("dark")

        self.geometry('700x400')
        self.title("Food App")

        ctk.CTkButton(self, text = "Generate groccerie list").pack(expand = True, side = "left")
        ctk.CTkButton(self, text = "Add Recipe").pack(expand = True, side = "right")
        

        # initialize variables 
        self.groccerie_ui = None


        # self.root = tk.Tk()
        # self.root.title("App")
        # self.root.option_add('*tearOff', tk.FALSE)
        # menubar = tk.Menu(self.root)
        # self.menu_file = tk.Menu(menubar)
        # self.menu_edit = tk.Menu(menubar)
        # self.add_edit_options()
        # self.add_file_options()
        # menubar.add_cascade(menu=self.menu_file, label='File')
        # menubar.add_cascade(menu=self.menu_edit, label='Edit')
        # self.root.config(menu=menubar)

        self.mainloop()


    def add_edit_options(self):
        self.menu_edit.add_command(label="Remove or edit recipe", command = lambda: print("Edit"))
        self.menu_edit.add_command(label="Rate recipes", command = lambda: print("Edit"))

    def add_file_options(self):
        self.menu_file.add_command(label="Generate groccerie list", command=self.open_recipe_generator)

    def open_recipe_generator(self):
        self.groccerie_ui = Grocceries()



if  __name__ == "__main__" :
    ui = App()
