from tkinter import *


def click():
    button['font'] = 'Arial 16'
    button['fg'] = 'red' 
    button['bg'] = 'lightgreen'


root = Tk()
root.geometry('400x200')
root.title("Button у Tkinter")
label1 = Label(root, text="Вітаємо", bg='lightgreen')
label1.pack()
button = Button(text='Натисни на мене', command=click, bg='yellow')
button.pack(pady=30)
root.mainloop()
