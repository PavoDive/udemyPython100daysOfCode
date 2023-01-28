# This is Angela's code from the password manager. I kept hers
# so I could focus on the json thing of today's lesson
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{"email": email, "password": password}}


    # json.dump() to write, json.load() to read and update() method to update a dictionary
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file) # load existing data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump({}, data_file)
                data = {}
        finally:
            data.update(new_data) # update with new data
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent = 4) # committing everythin to disk
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# -------------------------- DATA RETRIEVAL ----------------------- #

def retrieve():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title = "Error", message = "No data stored yet!")
    else:
        # this was my original code. However, Angela suggests that exception handling
        # is used for true exceptions. Other, more day-to-day situations should be
        # handled by if-else clauses. "If it can be solved with an if clause, don't
        # use a try-except one". So that's why it is commented.
        # try:
        #     email = data[website]["email"]
        # except KeyError:
        #     messagebox.showwarning(title = "Error", message = f"No data associated to {website}.")
        # else:
        #     password = data[website]["password"]
        #     messagebox.showwarning(title = website, message = f"Email: {email}\nPassword: {password}")
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showwarning(title = website, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title = "Error", message = f"No data associated to {website}.")


        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width = 14, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

retrieve_data_button = Button(text = "Query", width = 14, command = retrieve)
retrieve_data_button.grid(row = 1, column = 2)

window.mainloop()
