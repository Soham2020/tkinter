import tkinter
from tkinter import BOTH
root = tkinter.Tk()
root.title('Frames')
root.geometry('400x400')
#pack frames onto root
frame1 = tkinter.Frame(root, bg='orange')
frame2 = tkinter.LabelFrame(root, text='Soham Das', borderwidth=10, bg='light blue', fg='red')
frame3 = tkinter.Frame(root, bg='green')

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True, padx=10, pady=10)
frame3.pack(fill=BOTH, expand=True)
#pack frames
tkinter.Label(frame1, text='Hello').pack()
tkinter.Button(frame1, text='World', bg='black', activebackground='white').pack()
#grid frames
tkinter.Label(frame3, text='Soham').grid(row=0, column=0)
tkinter.Label(frame3, text='Soham').grid(row=2, column=2)
tkinter.Button(frame2, text='test', bg='yellow').grid(row=0,column=2, sticky='WE')
root.mainloop()