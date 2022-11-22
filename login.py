import tkinter
from tkinter import messagebox
from tkinter import Toplevel

from subprocess import call


window = tkinter.Tk()
window.title("poemSize LogIn")
window.geometry("420x288")
window.resizable(0, 0)


def login():
    print("Button is clicked")
    username = username_entry.get()
    password = password_entry.get()
    print(username, password)
    messagebox.showinfo(title="Error", message="Invalid username or password")


def registration():
    print("reg")
    rw = Toplevel(window)
    rw.title("Registration")
    rw.geometry("322x228")
    rw.resizable(0, 0)

    def save_user():
        print("saved")
        name = r_username_entry.get()
        pw = r_password_entry.get()
        file = open("users.txt", "w")
        file.write(name)
        file.write("|")
        file.write(pw+"\n")
        print(name, pw)

    # Widgets
    registration_label = tkinter.Label(rw, text="Registration", font=("Algerian", 28))
    r_username_label = tkinter.Label(rw, text="User", font=("Papyrus", 14))
    r_username_entry = tkinter.Entry(rw, font=("Ink Free", 14))
    r_password_label = tkinter.Label(rw, text="Password", font=("Papyrus", 14))
    r_password_entry = tkinter.Entry(rw, font=("Ink Free", 14))
    r_button = tkinter.Button(rw, text="Register", font=("Papyrus", 12), command=save_user)

    # Widget placing
    registration_label.grid(row=0, column=0, columnspan=2, padx="8", sticky="e")
    r_username_label.grid(row=1, column=0)
    r_username_entry.grid(row=1, column=1)
    r_password_label.grid(row=2, column=0)
    r_password_entry.grid(row=2, column=1)
    r_button.grid(row=3, column=1, padx="8", sticky="e")


frame = tkinter.Frame()
# Widgets
login_label = tkinter.Label(frame, text="LogIn", font=("Algerian", 28))
username_label = tkinter.Label(frame, text="User", font=("Papyrus", 14))
username_entry = tkinter.Entry(frame, font=("Ink Free", 14))
password_label = tkinter.Label(frame, text="Password", font=("Papyrus", 14))
password_entry = tkinter.Entry(frame, font=("Ink Free", 14), show="*")
login_button = tkinter.Button(frame, text="Enter", font=("Papyrus", 12), command=login)
registration_button = tkinter.Button(frame, text="Registration", font=("Papyrus", 12), command=registration)

# Widget placing
login_label.grid(row=0, column=0, columnspan=2, padx="8", sticky="e")
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
registration_button.grid(row=3, column=0, columnspan=1, padx="8", sticky="e")
login_button.grid(row=3, column=1, columnspan=1, padx="16", pady="8", sticky="e")

frame.place(x=40, y=30)

window.mainloop()

