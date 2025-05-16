import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# This function gets the user entry from the input field.
def get_user_entry():
    return user_entry.get()

# This function validates the user input.
def validate_user_input():
    """Return the validated user entry value.
    
    This function calls the get_user_entry function to retrieve the user's input.
    It then attempts to convert the input to a float using the convert_user_entry function.
    If the conversion is successful, it means the input is a valid float.
    Otherwise, it raises a SyntaxError and displays an error message.
    """
    user_entry = get_user_entry() 
    try:
        user_entry = convert_user_entry()
        return user_entry
    except:
        messagebox.showerror("SyntaxError", "Input invalid")

# This function converts the user entry to a float value.
def convert_user_entry():
    user_entry = get_user_entry()
    return float(user_entry)

# This function handles edge cases for Celsius unit.
def validate_celsius_unit():
    user_entry = validate_user_input()
    if user_entry < -273.15:
        messagebox.showerror("ValueError", "Celsius unit accepts only numbers greater than or equal to -273.15")
    else:  
        return user_entry

# This function handles edge cases for Fahrenheit unit.
def validate_fahrenheit_unit():
    user_entry = validate_user_input()
    if user_entry < -459.67:
        messagebox.showerror("ValueError", "Fahrenheit unit accepts only numbers greater than or equal to -(459.67)")
    else:
        return user_entry

# This function handles edge cases for Kelvin unit.
def validate_kelvin_unit():
    user_entry = validate_user_input()
    if user_entry < 0:
        messagebox.showerror("ValueError", "Kelvin unit accepts only positive values")
    else:
        return user_entry

# This function checks the user's selected unit from the ComboBox.
def check_user_entry():
    """Initiate the conversion function after checking the selected unit.
    
    This function retrieves the selected unit from the ComboBox,
    then calls the appropriate conversion function based on the selection.
    If no unit is selected, it raises an error.
    """
    selected_unit = Combo.get()
    if selected_unit == "Celsius":
        fahrenheit_value, kelvin_value = convert_from_celsius() 
        first_unit_name.config(text="Fahrenheit:")
        first_unit_values.config(text=fahrenheit_value)
        second_unit_name.config(text="Kelvin:")
        second_unit_values.config(text=kelvin_value)
    
    elif selected_unit == "Fahrenheit":
        celsius_value, kelvin_value = convert_from_fahrenheit()
        
        first_unit_name.config(text="Celsius:")
        first_unit_values.config(text=celsius_value)
        
        second_unit_name.config(text="Kelvin:")
        second_unit_values.config(text=kelvin_value)
        
    elif selected_unit == "Kelvin":
        celsius_value, fahrenheit_value = convert_from_kelvin()
        
        first_unit_name.config(text="Celsius:")
        first_unit_values.config(text=celsius_value)
        
        second_unit_name.config(text="Fahrenheit:")
        second_unit_values.config(text=fahrenheit_value)
        
    else:
        messagebox.showerror("Error", "Please choose a unit")

# This function converts the user entry from Celsius to Fahrenheit and Kelvin.
def convert_from_celsius():
    user_entry = validate_celsius_unit()

    x = float((9/5) * user_entry + 32)
    fahrenheit_value = "{:.2f}".format(x)
    
    y = float(user_entry + 273.15)
    kelvin_value = "{:.2f}".format(y)
    
    return fahrenheit_value, kelvin_value

# This function converts the user entry from Fahrenheit to Celsius and Kelvin.
def convert_from_fahrenheit():
    user_entry = validate_fahrenheit_unit()
    
    x = float((5/9) * (user_entry - 32))
    celsius_value = "{:.2f}".format(x)
    
    y = float((5/9) * (user_entry - 32) + 273.15)
    kelvin_value = "{:.2f}".format(y)
    
    return celsius_value, kelvin_value

# This function converts the user entry from Kelvin to Celsius and Fahrenheit.
def convert_from_kelvin():
    user_entry = validate_kelvin_unit()
        
    x = float(user_entry - 273.15)
    celsius_value = "{:.2f}".format(x)
    
    y = float((9/5) * (user_entry - 273.15) + 32)
    fahrenheit_value = "{:.2f}".format(y)
    
    return celsius_value, fahrenheit_value
 
# Initialize the GUI and build the widgets.
root = tk.Tk()
root.title("Temperature Converter")
root.minsize(200, 200)
root.configure(background="#FFF5EE")
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
  
user_input_label = tk.Label(root, text="Input")
user_input_label.grid(row=0, column=0)
user_input_label.configure(background="#FFF5EE")

user_entry = tk.Entry(root, background="#FFE5B4")
user_entry.grid(row=0, column=1)

selected_unit = ["Celsius", "Fahrenheit", "Kelvin"]
Combo = ttk.Combobox(root, values=selected_unit)
Combo.set("Unit")
Combo.grid(row=0, column=2, padx=5, pady=5)

convertor_button = tk.Button(root, width=10, background="#FFE5B4", text="Convert", command=check_user_entry)
convertor_button.grid(row=4, columnspan=3, padx=20, pady=20)

first_unit_name = tk.Label(root, text="____")
first_unit_name.grid(row=2, column=1, padx=15, pady=10)
first_unit_name.configure(background="#FFF5EE")

first_unit_values = tk.Label(root, text="____")
first_unit_values.grid(row=2, column=2)
first_unit_values.configure(background="#FFF5EE")

second_unit_name = tk.Label(root, text="____")
second_unit_name.grid(row=3, column=1, padx=15, pady=10)
second_unit_name.configure(background="#FFF5EE")

second_unit_values = tk.Label(root, text="____")
second_unit_values.grid(row=3, column=2)
second_unit_values.configure(background="#FFF5EE")

root.mainloop()
