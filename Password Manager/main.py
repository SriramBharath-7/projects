from tkinter import *
import ctypes
from tkinter import messagebox
import pyperclip
from random import *
import json
FONT =("Cascadia Mono",10,"normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

  password_list = password_numbers + password_letters + password_symbols
  shuffle(password_list)

  password = "".join(password_list)
  pass_entry.insert(0,password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website:{
            "email":username,
            "password":password,
        }
    }

    if len(website) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty")

    else:

        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)

        finally:
            website_entry.delete(0,END)
            pass_entry.delete(0,END)


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data Found!")

    else:

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email / Username: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

ctypes.windll.shcore.SetProcessDpiAwareness(True)
window = Tk()
window.minsize(800,520)
window.title("Password Manager")
window.config(padx=30,pady=50)

canvas = Canvas(height=200,width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= img)
canvas.place(x=250,y=0)

# Labels
website_label = Label(text="Website:",font=FONT)
website_label.place(x=80,y=200)
email_label = Label(text="Email/Username:",font=FONT)
email_label.place(x=80,y=250)
password_label = Label(text="Password:",font=FONT)
password_label.place(x=80,y=300)

# Entries
website_entry = Entry(width=35)
website_entry.place(x=200,y=205)
email_entry = Entry(width=35)
email_entry.place(x=270,y=255)
email_entry.insert(0,"srirambharath7@gmail.com")
pass_entry = Entry(width=24)
pass_entry.place(x=200,y=305)

# Buttons
gen_pass = Button(text="Generate Password",command=generate_password)
gen_pass.place(x=458,y=300)
add_button = Button(text="Add",width=53,command=save)
add_button.place(x=80,y=355)
search = Button(text="Search",command=find_password)
search.place(x=558,y=200)

window.mainloop()