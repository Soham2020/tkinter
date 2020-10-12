import tkinter

root = tkinter.Tk()
root.title('Calculator')
root.iconbitmap('wave.ico')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg="#169873")



#define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack()
button_frame.pack()


root.mainloop()