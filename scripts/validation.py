from tkinter import messagebox

def validate_input_string(input_string: str):
    if input_string:
        try:
            float(input_string)
            # label.config(
            #     text=f"Valid numeric value: {input_data}",
            #     foreground="green",
            # )
        except ValueError:
            # label.config(
            #     text=f'Numeric value expected, got "{input_data}"',
            #     foreground="red",
            # )
            print("error")
            messagebox.showwarning("Warning", "Do not use any special characters or numbers!")

def validate_input_number(input_number: str):
    if input_number:
        try:
            float(input_number)
            # label.config(
            #     text=f"Valid numeric value: {input_data}",
            #     foreground="green",
            # )
        except ValueError:
            # label.config(
            #     text=f'Numeric value expected, got "{input_data}"',
            #   
            print("error") 
            messagebox.showwarning("Warning", "Do not use any special characters or numbers!")