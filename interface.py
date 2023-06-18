from cgitb import text
from tkinter import *
from tkinter import ttk
from service import *


def click_button():
    name = entry_name.get()
    passw = entry_pass.get()
    entry_name.delete(0, END)
    entry_pass.delete(0, END)
    connect()
    temp = getUser(name, passw)
    if isinstance(temp, Error):
        label[text] = f'User {temp.text}'
    else:
        label[text] = f"User {temp.login}"
    close()

def close():
    root.destroy()
    

root = Tk()
root.title("Auth")
root.geometry("300x250") 
root.config(bg="skyblue")

label = Label(anchor=N, text="enter your creds", cursor="heart")
label.pack(padx=8, pady=8)

label_name = Label(text="login")
label_name.pack(anchor=W, padx=8, pady=8)

entry_name = ttk.Entry()
entry_name.pack(anchor=NW, padx=8, pady=8)

label_pass = Label(text="pass")
label_pass.pack(anchor=W, padx=8, pady=8)

entry_pass = ttk.Entry()
entry_pass.pack(anchor=NW, padx=8, pady=8)

btn = ttk.Button(text="Commit", command=click_button)
btn.pack(anchor=S, padx=8, pady=8)

root.mainloop()
