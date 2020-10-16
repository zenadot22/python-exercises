import tkinter as tk 
#from tkinter import messagebox 
from functools import partial 


# Declaration of global variable 
temperature = "Celsius"

# getting drop down value 
def store_temp(set_temp): 
	global temperature
	temperature = set_temp 

# Conversion of temperature 
def call_convert(label, input): 
	temp = input.get() 
	
	if temperature == 'Celsius': 
		
		# Converting celsius temperature to fahrenheit 
		f = float((float(temp) * 9 / 5) + 32) 
		label.config(text ="%.1f Fahrenheit" % f) 
		#messagebox.showinfo("Temperature Converter", 
							#"Successfully converted to Fahrenheit ", ) 
		
	if temperature == 'Fahrenheit': 
		
		# Converting fahrenheit temperature to celcius
		
		c = float((float(temp) - 32) * 5 / 9) 
		label.config(text ="%.1f Celsius" % c) 
		#messagebox.showinfo("Temperature Converter", 
							#"Successfully converted to Celsius ") 
	return


# creating Tk window 
root = tk.Tk() 

# setting geometry of tk window 
root.geometry("300x150") 

# Using title() to display a message in the 
# dialogue box of the message in the title bar 
root.title('Temperature Converter') 

# Lay out widgets 
root.grid_columnconfigure(1, weight = 1) 
root.grid_rowconfigure(1, weight = 1) 

inputNumber = tk.StringVar() 
var = tk.StringVar() 

# label and entry field 
input_label = tk.Label(root, text ="Enter temperature\n") 
input_entry = tk.Entry(root, textvariable = inputNumber) 
input_label.grid(row = 1) 
input_entry.grid(row = 1, column = 1) 
output_label = tk.Label(root) 
output_label.grid(row = 3, columnspan = 4) 


# drop down setup 
dropDownList = ["Celsius", "Fahrenheit"] 
drop_down = tk.OptionMenu(root, var, *dropDownList, 
						command = store_temp) 
var.set(dropDownList[0]) 
drop_down.grid(row = 1, column = 2) 

# button widget 
call_convert = partial(call_convert, output_label, 
					inputNumber) 
convert_button = tk.Button(root, text ="Calculate Conversion", 
						command = call_convert) 
convert_button.grid(row = 2, columnspan = 2) 


# runs tkinter program infinitely 
root.mainloop() 
