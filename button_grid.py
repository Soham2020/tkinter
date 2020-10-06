import tkinter
#define window
root = tkinter.Tk()
root.title('Buttons and Grid')
root.geometry('400x400')
#define buttons
button1 = tkinter.Button(root, text='Name', bg='red')
button1.grid(row=0, column=0)

button2 = tkinter.Button(root, text='Date', bg='blue', activebackground='yellow', fg='white')
button2.grid(row=0,column=1, ipadx='5', ipady='5', padx='15')

button3 = tkinter.Button(root, text='Hello', bg='Black', activebackground='green', fg='white', borderwidth=5)
button3.grid(row=1, column=0, columnspan=3 ,sticky='WE')
#run the window
root.mainloop()