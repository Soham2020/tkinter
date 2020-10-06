import tkinter
# define window
root = tkinter.Tk()
root.title('Hello')             #tittle of the window
root.geometry('300x300')        #dimension of the window
root.config(bg='black')         #bg color of the window

#second window
top = tkinter.Toplevel()
top.title('World')
top.geometry('150x150')
top.config(bg='#fff')
#run the window in the main loop
root.mainloop()