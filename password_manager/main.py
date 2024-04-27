# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    passENt.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    web=webEnt.get()
    eml=emailEnt.get()
    passwrd=passENt.get()
    if len(web)==0 or len(eml)==0 or len(passwrd)==0:
        messagebox.showinfo(title="Oops..",message="Fill all the fields!!")
    else:
        is_ok=messagebox.askokcancel(title=web,message=f"These are the details: \n Email: {eml} \n Password: {passwrd} \n Is it ok to save?")
        webEnt.delete(0, END)
        passENt.delete(0, END)
        emailEnt.delete(0, END)
        if is_ok:
            file= open("passwords.txt" ,"a")
            file.write(f"{web} || {eml} || {passwrd} \n")
            file.close()
        else:
             return



# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
window = Tk()

window.config(padx=50, pady=50)

website_label = Label(text="Website:")
canvas = Canvas(width=200, height=200)

email = Label(text="Email/Username:")
webEnt = Entry(width=35)
passw = Label(text="Password:")
passENt = Entry(width=21)
emailEnt = Entry(width=35)
gen = Button(text="GeneratePassword",command=gen_pass)
add = Button(text="Add", width=36,command=save_pass)




pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)


website_label.grid(row=1, column=0)
website_label.config(font="bold")


email.config(font="bold")
email.grid(row=2, column=0)


passw.config(font="bold")
passw.grid(row=3, column=0)


webEnt.grid(row=1, column=1, columnspan=2)
webEnt.focus()

emailEnt.grid(row=2, column=1, columnspan=2)


passENt.grid(row=3, column=1, columnspan=2)


gen.grid(row=3, column=3)


add.grid(row=4, column=1, columnspan=2)

window.mainloop()