import tkinter

root = tkinter.Tk()
root.title('To-do App')
root.iconbitmap('wave.ico')
root.geometry('500x300')
root.config(bg='#14BDEB')
root.resizable(0,0)

#create frames
input_frame = tkinter.Frame(root, bg='#14BDEB')
output_frame = tkinter.Frame(root, bg='#14BDEB')
button_frame = tkinter.Frame(root, bg='#14BDEB')
input_frame.pack()
output_frame.pack()
button_frame.pack()

#create input layout
list_entry = tkinter.Entry(input_frame, borderwidth=3, width=35)
list_add_button = tkinter.Button(input_frame, text='Add', bg="#DCCDE8", borderwidth=3)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5)

#create output layout
my_listbox = tkinter.Listbox(output_frame, width=75,height=14)
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

#create button frame
list_remove_button = tkinter.Button(button_frame, text="Remove", bg="#DCCDE8", borderwidth=2)
list_clear_button = tkinter.Button(button_frame, text="Clear", bg="#DCCDE8", borderwidth=2)
save_button = tkinter.Button(button_frame, text="Save", bg='#DCCDE8', borderwidth=2)
quit_button = tkinter.Button(button_frame, text="Close", bg="#DCCDE8", borderwidth=2, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10)
quit_button.grid(row=0, column=3, padx=2, pady=10)


root.mainloop()