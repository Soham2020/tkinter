import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL
root = tkinter.Tk()
root.title('Calculator')
root.iconbitmap('wave.ico')
root.geometry('300x400')
root.resizable(0,0)
root.config(bg="#002A32")

#define functions
def submit_number(number):
    display.insert(END, number)
    if "." in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    global first_number
    global operation
    operation = operator
    first_number = display.get()
    display.delete(0, END)
    #Dispable all operator buttons until equal or clear is pressed
    add_button.config(state=DISABLED)
    substract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    decimal_button.config(state=NORMAL)


#define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(50,20))
button_frame.pack(padx=2, pady=5)

#layout for display frame
display = tkinter.Entry(display_frame, font=30, width=50, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

#define button frames
clear_button = tkinter.Button(button_frame, text="CLEAR", bg="#169873", font=18)
quit_button = tkinter.Button(button_frame, text="QUIT", bg="#169873", font=18, command=root.destroy)

inverse_button = tkinter.Button(button_frame, text="1/x", bg="#169873", font=18)
square_button = tkinter.Button(button_frame, text="x^2", bg="#169873", font=18)
exponent_button = tkinter.Button(button_frame, text="x^n", bg="#169873", font=18, command=lambda : operate("exponent"))
divide_button = tkinter.Button(button_frame, text=" / ", bg="#169873", font=18, command=lambda : operate("divide"))
multiply_button = tkinter.Button(button_frame, text="*", bg="#169873", font=18, command=lambda : operate("multiply"))
substract_button = tkinter.Button(button_frame, text="-", bg="#169873", font=18, command=lambda : operate("substract"))
add_button = tkinter.Button(button_frame, text="+", bg="#169873", font=18, command=lambda : operate("add"))
equal_button = tkinter.Button(button_frame, text="=", bg="#169873", font=18)
decimal_button = tkinter.Button(button_frame, text=".", bg="#169873", font=18, command=lambda : submit_number("."))
negate_button = tkinter.Button(button_frame, text="+/-", bg="#169873", font=18)

nine_button = tkinter.Button(button_frame, text="9", bg="black", fg="white", font=18, command=lambda : submit_number(9))
eight_button = tkinter.Button(button_frame, text="8", bg="black", fg="white", font=18, command=lambda : submit_number(8))
seven_button = tkinter.Button(button_frame, text="7", bg="black", fg="white", font=18, command=lambda : submit_number(7))
six_button = tkinter.Button(button_frame, text="6", bg="black", fg="white", font=18, command=lambda : submit_number(6))
five_button = tkinter.Button(button_frame, text="5", bg="black", fg="white", font=18, command=lambda : submit_number(5))
four_button = tkinter.Button(button_frame, text="4", bg="black", fg="white", font=18, command=lambda : submit_number(4))
three_button = tkinter.Button(button_frame, text="3", bg="black", fg="white", font=18, command=lambda : submit_number(3))
two_button = tkinter.Button(button_frame, text="2", bg="black", fg="white", font=18, command=lambda : submit_number(2))
one_button = tkinter.Button(button_frame, text="1", bg="black", fg="white", font=18, command=lambda : submit_number(1))
zero_button = tkinter.Button(button_frame, text="0", bg="black", fg="white", font=18, command=lambda : submit_number(0))

#First row
clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")
 #Second row
inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")
#Third row (Add padding to create the size of the columns)
seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)
#Fourth row
four_button.grid(row=3, column=0, pady=1, sticky="WE")
five_button.grid(row=3, column=1, pady=1, sticky="WE")
six_button.grid(row=3, column=2, pady=1, sticky="WE")
substract_button.grid(row=3, column=3, pady=1, sticky="WE")
 #Fifth row
one_button.grid(row=4, column=0, pady=1, sticky="WE")
two_button.grid(row=4, column=1, pady=1, sticky="WE")
three_button.grid(row=4, column=2, pady=1, sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")
#Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky="WE")
zero_button.grid(row=5, column=1, pady=1, sticky="WE")
decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")


root.mainloop()