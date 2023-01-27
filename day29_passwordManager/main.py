from tkinter import *
from tkinter import messagebox
import random
import pyperclip # this is to copy the password to the clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# code copied from Angela's day 5 "password generator"

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [letter for letter in random.choices(letters, k = nr_letters)]

    password_list += [symbol for symbol in random.choices(symbols, k = nr_symbols)]

    password_list += [number for number in random.choices(numbers, k = nr_numbers)]

    password = "".join(password_list)

    random.shuffle(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# when add is pressed the data should append to a "data.txt" file:
# the website, the username and the password
# separated by the string " | "

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    output_list = [website, username, password]
    output_text = " | ".join(output_list)+"\n"

    empty_fields = len(website) == 0 or len(username) == 0 or len(password) == 0

    if empty_fields:
        messagebox.showwarning(title = "Empty fields!", message = "Please complete the empty fields before saving.")
    else:
        user_wants_save = messagebox.askokcancel(title = website, message = f"This are the details entered:\nEmail: {username}\nPassword: {password}\nIs it OK to save?")

        if user_wants_save:
            with open("data.txt", "a") as file1:
                file1.write(output_text)

                website_entry.delete(0, END)
                username_entry.delete(0, END)
                username_entry.insert(0, "giovanni@whatever.com")
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 50)

canvas = Canvas(width = 200, height = 200)
lock_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_image)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)

username_label = Label(text = "Email/Username:")
username_label.grid(row = 2, column = 0)

password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

website_entry = Entry(width = 41)
website_entry.grid(row = 1, column = 1, columnspan = 2)
website_entry.focus() # bring the cursor here at start

username_entry = Entry(width = 41)
username_entry.grid(row = 2, column = 1, columnspan = 2)
username_entry.insert(0, "giovanni@whatever.com")

password_entry = Entry(width = 19)
password_entry.grid(row = 3, column = 1)
password = generate_password()
#password_entry.insert(0, password)

password_button = Button(text = "Generate Password", command = generate_password)
password_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 40, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)




window.mainloop()
