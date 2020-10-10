import tkinter
from tkinter import ttk
root = tkinter.Tk()
root.title('Metric Helper')
root.iconbitmap('wave.ico')
# root.geometry('500x500')
root.config(bg='#C5D86D')
root.resizable(0,0)

#define functions
#define entry
input_field = tkinter.Entry(root, width=20)
output_field = tkinter.Entry(root, width=20)
equal_field = tkinter.Label(root, text="=", bg="#1B998B")

input_field.grid(row=0, column = 0, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)
equal_field.grid(row=0, column=1, padx=10, pady=10)

input_field.insert(0, "Enter your Quantity")

metric_list = ["femto", "pico", "nano", "micor", "milli", "centi", "deci", "kilo", "hecto", "mega", "giga", "tera"]
input_combobox = ttk.Combobox(root, value=metric_list, justify='center')
to_Label = tkinter.Label(root, text="to")
output_combobox = ttk.Combobox(root, value=metric_list, justify='center')

input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_Label.grid(row=1, column=1)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

input_combobox.set("centi")
output_combobox.set('milli')


convert_button = tkinter.Button(root, text="Convert", bg="#DBB4AD")
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

root.mainloop()