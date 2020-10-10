import tkinter

root = tkinter.Tk()
root.title('To-do App')
root.iconbitmap('wave.ico')
root.geometry('500x300')
root.config(bg='#14BDEB')
root.resizable(0,0)

#create frames
input_frame = tkinter.Frame(root)
output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#create input layout
list_entry = tkinter.Entry(input_frame, borderwidth=3)
list_add_button = tkinter.Button(input_frame, text='Add', bg="#DCCDE8", borderwidth=2)
list_entry.grid(row=0, column=0)
list_add_button.grid(row=0, column=1)

root.mainloop()