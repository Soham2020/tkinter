import tkinter
from tkinter import END

#function
def print_text():
    text = tkinter.Label(frame1, text=text_entry.get(), bg='yellow')
    text.pack()
    text_entry.delete(0, END)

def counter(number):
    global value
    num = tkinter.Label(frame1, text=number, bg='yellow')
    num.pack()
    value = number + 1

root = tkinter.Tk()
root.title('Entries')
root.geometry('500x500')

frame1 = tkinter.Frame(root, bg='yellow', width=500, height=250)
frame2 = tkinter.Frame(root, bg='blue', width=500, height=250)
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=(0,10))
frame1.pack_propagate(0)
#entries
text_entry = tkinter.Entry(frame2, width=20)
text_entry.grid(row=0, column=0, padx=10, pady=10)
frame2.grid_propagate(0)

# text_entry2 = tkinter.Entry(frame2, width=20)
# text_entry2.grid(row=1, column=0, padx=10, pady=10, sticky='W')
# frame2.grid_propagate(0)

#buttons and link to functions
text_Button = tkinter.Button(frame2, text='Print' ,width=5, command=print_text)
text_Button.grid(row=0, column=1)

value=0

text_Button2 = tkinter.Button(frame2, text='count', width=5, command=lambda:counter(value))
text_Button2.grid(row=1, column=0, sticky='WE', padx=10)

root.mainloop()