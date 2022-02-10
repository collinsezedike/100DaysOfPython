import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD RETRIEVER ------------------------------- #


def find_password():
    inputted_website = website_entry.get()
    try:
        with open("data.json") as password_archive:
            archive = json.load(password_archive)
            retrieved_email = archive[inputted_website]["email"]
            retrieved_password = archive[inputted_website]["password"]
    except KeyError:
        if len(inputted_website) == 0:
            messagebox.showinfo(title="No Input", message="You haven't made any entry in  the website file")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {inputted_website} exists")
    except FileNotFoundError:
        messagebox.showinfo(title="No data file found", message="You haven't saved any passwords, yet")
    else:
        messagebox.showinfo(title=inputted_website, message=f"Email: {retrieved_email}"
                                                            f"\nPassword: {retrieved_password}")
        pyperclip.copy(retrieved_password)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    lower = list("abcdefghijklmnopqrstuvwxyz")
    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("~!@#$%^&*()_+-=[]")

    chars_lists = [lower, upper, numbers, symbols]
    random_password = ""
    for _ in range(12):
        random_password += random.choice(random.choice(chars_lists))
    # paste password on the password entry
    password_entry.delete(0, END)
    password_entry.insert(END, string=random_password)
    # copy password to clipboard
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    inputted_website = website_entry.get()
    inputted_email = email_entry.get()
    inputted_password = password_entry.get()

    # json requires a dictionary
    data_dict = {
        inputted_website: {
            "email": inputted_email,
            "password": inputted_password,
        },
    }

    # check if there is any empty entry
    if len(inputted_website) == 0 or len(inputted_email) == 0 or len(inputted_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=inputted_website,
                                       message=f"These are the details entered: \nEmail: {inputted_email} "
                                               f"\nPassword: {inputted_password} \nis it ok to save?")
        if is_ok:
            try:
                password_archive = open("data.json", "r")
                # to read a json file
                archive = json.load(password_archive)
                # to append to a json file
                archive.update(data_dict)
            except FileNotFoundError:
                password_archive = open("data.json", "w")
                json.dump(data_dict, password_archive, indent=4)
            else:
                password_archive = open("data.json", "w")
                # to write to a json file
                json.dump(archive, password_archive, indent=4)
            finally:
                password_archive.close()

                # clear the inputs
                website_entry.delete(0, END)
                password_entry.delete(0, END)

                # place the cursor back at website entry
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Your Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
IMAGE = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=IMAGE)
canvas.grid(row=0, column=1)

# Website label
website = Label(text="Website:")
website.grid(column=0, row=1)
# Website input
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1, column=1)

# Email label
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
# Email input
email_entry = Entry(width=53)
email_entry.insert(END, "johndoe@email.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password label
password = Label(text="Password:")
password.grid(row=3, column=0)
# Password input
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)
# Generate password button
generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# Add button
add = Button(text="Add", width=45, command=save_password)
add.grid(row=4, column=1, columnspan=2)

# Search button
search = Button(text="Search", command=find_password)
search.config(padx=35)
search.grid(row=1, column=2)

window.mainloop()
