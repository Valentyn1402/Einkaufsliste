import tkinter as tk
from tkinter import *

#create the main window 
window = Tk()
window.title("Hello World")


def handle_button_press():
    window.destroy()

#define the labels in the window
x1 = Label(window, text = "Enter the ingredient").grid(row=0)
x1 = Label(window, text = "Enter the ammount").grid(row=1)
  

#define the entries in the window
a = Entry(window)
b = Entry(window)
b1 = Entry(window)
b2 = Entry(window)
b3 = Entry(window)

a.grid(row = 0, column = 1)
b.grid(row = 1, column = 1)

button = tk.Button(text="My simple app.", command=handle_button_press)
# button.pack()

# Start the event loop.
window.mainloop()