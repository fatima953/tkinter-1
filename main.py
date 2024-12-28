from tkinter import *

#creat window
root = Tk()
root.title('login app')
root.geometry('400x400')


frame = Frame(master = root, height = 200, width = 360, bg = 'lightpink')

#add lable
lbl1 = Label(frame, text = 'full name', bg = 'green', fg = 'white', width = 12)
lbl2 = Label(frame, text = 'email', bg = 'green', fg = 'white', width = 12)
lbl3 = Label(frame, text = 'password', bg = 'green', fg = 'white', width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show = '*')

#function to display message
def display():
    name = name_entry.get()
    greet = 'Hey' + name
    message = '\nCongratulations for your new account!'
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg = 'gold', fg = 'black')

#add button
btn = Button(text = 'Creat account', command = display, bg = 'red')

#arrange all widgets
frame.place(x = 20, y = 0)
lbl1.place(x = 20, y = 20)
name_entry.place(x = 150, y = 20)
lbl2.place(x = 20, y = 80)
email_entry.place(x = 150, y = 80)
lbl3.place(x = 20, y = 140)
pass_entry.place(x = 150, y = 140)
btn.place(x = 130, y = 210)
textbox.place(y = 250)

root.mainloop()


