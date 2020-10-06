import tkinter

root = tkinter.Tk()
root.title('Radio button')
root.geometry('500x500')

input_frame = tkinter.Frame(root, width=500, height=250, bg='orange')
output_frame = tkinter.Frame(root, width=400, height=300)
input_frame.pack()
output_frame.pack()

radio1 = tkinter.Radiobutton(input_frame, text='Option 1', bg='orange')
radio1.grid(row=0, column=0)
input_frame.grid_propagate(0)

radio2 = tkinter.Radiobutton(input_frame, text='Option 1', bg='orange')
radio2.grid(row=0, column=1)
input_frame.grid_propagate(0)

root.mainloop()