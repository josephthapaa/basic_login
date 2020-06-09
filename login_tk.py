#simple login simulation
from tkinter import *
from tkinter import messagebox
import re
import csv




def login():
    ''' login function which takes email and pass from csv file and stores it in list
        then compares entered email & password with that in csv database  '''
    email_ = email_enter.get()
    password_ = password_enter.get()
    with open('database.csv', 'r') as f:
        reader_ = csv.DictReader(f)
        reader_list = list(reader_)
        for i in reader_list:
            if i['email'] == email_ and i['password'] == password_:
                Label(root, text = 'Logged in successfully').grid(row = 3, column = 0)
            elif i['email'] == email_ and i['password'] != password_:
                Label(root, text = 'Incorrect password').grid(row = 3, column = 0)
            else:
                Label(root, text = 'Incorrect email').grid(row = 3, column = 0)



def register():
    ''' register function which takes value from database and stores it in data list
        and then compares it to the entered email and password
        if laready in list prints already registered
        if not then writes it in csv file '''
    email = email_enter.get()
    password = password_enter.get()
    data = []
    with open('database.csv', 'r') as f:
        reader_ = csv.reader(f)
        for i in reader_:
            data.append(i)
    for j in range(0, len(data)):
        if data[j][0] == email:
            Label(root, text = 'Already registered').grid(row = 3, column = 0)
            break
    else:
        with open('database.csv', 'a') as f1:
            writer_ = csv.writer(f1, delimiter = ',', lineterminator = '\n')
            writer_.writerow([email, password])
            Label(root, text = 'Registered succesfully').grid(row = 3, column = 0)



#docstrings
# help(register)
# help(login)

#main window with tkinter
root = Tk()
root.title('login with tkinter')
root.configure(bg = 'black')

#instruction
messagebox.showinfo('Instructions', 'This is a simple simulator of login system.Improvements need to be made.You have to close program and run again after register or login for better output.I will add features and improve it soon.Thanks')

#email label and entry box
email_lbl = Label(root, text = 'Email : ', bg = 'black', fg = 'yellow')
email_lbl.grid(row = 0, column = 0)
email_enter = Entry(root, width = 20)
email_enter.grid(row = 0, column = 1)

#password label and entry box
password_lbl = Label(root, text = 'Password :  ', bg = 'black', fg = 'yellow')
password_lbl.grid(row = 1, column = 0)
password_enter = Entry(root, width = 20)
password_enter.grid(row = 1, column = 1)

#login button
login_btn = Button(root, text = 'Login', width = 20, bg = 'black', fg = 'yellow', command = login)
login_btn.grid(row = 2, column = 0)

#register button
register_btn = Button(root, text = 'Register', width = 20, bg = 'black', fg = 'yellow', command = register)
register_btn.grid(row = 2, column = 1)


#mainloop
root.mainloop()
