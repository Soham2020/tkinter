import tkinter
from tkinter import BOTH
#define window
root = tkinter.Tk('Labels Basics!')
root.title('Lables basics')
root.config(bg='blue')
root.geometry('400x400')

#widgets
label_1 = tkinter.Label(root, text='Hello World')
label_1.pack()

label_2 = tkinter.Label(root, text='Hello I am Soham Das', font=('Arial', 20, 'bold'))
label_2.config(bg='red')
label_2.pack(padx='10', pady='20', ipadx='10', ipady='10', anchor='s')

label_3 = tkinter.Label(root, text='Hello, I am Das')
label_3.config(bg='yellow')
label_3.pack(fill=BOTH, expand=True, padx='15', pady='15')
#run the window
root.mainloop()