import tkinter
from tkinter import StringVar
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

input_field.grid(row=0, column = 0)
output_field.grid(row=0, column=2)
equal_field.grid(row=0, column=1)

input_field.insert(0, "Enter your Quantity")

metric_list = ["femto", "pico", "nano", "micor", "milli", "centi", "deci", "kilo", "hecto", "mega", "giga", "tera"]
input_choice = StringVar()
output_choice = StringVar()
input_drop = tkinter.OptionMenu(root, input_choice, *metric_list)
output_drop = tkinter.OptionMenu(root, output_choice, *metric_list)
to_Label = tkinter.Label(root, text="to")

input_drop.grid(row=1, column=0)
to_Label.grid(row=1, column=1)
output_drop.grid(row=1, column=2)

input_choice.set("centi")
output_choice.set('milli')


convert_button = tkinter.Button(root, text="Convert", bg="#DBB4AD")
convert_button.grid(row=2, column=0, columnspan=3)

root.mainloop()