import tkinter
from tkinter import messagebox
import pandas
import os
import random
import pyperclip
import json

#Password Generator

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for char in range(nr_letters)]
  password_numbers = [random.choice(numbers) for num in range(nr_numbers)]
  password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

  password_list = password_letters + password_numbers + password_symbols
  random.shuffle(password_list)

  password = "".join(password_list)

  password_input.insert(0, password)
  pyperclip.copy(password)

window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


def add():
  website = website_input.get()
  email = email_input.get()
  password = password_input.get()
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }

  if(len(email) == 0 or len(password) == 0):
    messagebox.showwarning(title='Ooops', message="Please don't leave any fields empty!")
    return

  is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

  if is_ok:
    try:
      with open('data.json', "r") as data_file:
        #Reading old data
        data = json.load(data_file)
        #Updating old data
        data.update(new_data)
    except FileNotFoundError:
      data = new_data
    finally:
      with open('data.json', 'w') as data_file:
        #Saving updated data
        json.dump(data, data_file, indent=4)
        website_input.delete(0, tkinter.END)
        password_input.delete(0, tkinter.END)


# def add():
#   row = pandas.DataFrame([[website_input.get(),email_input.get(), password_input.get()]])
#   output_path = 'my_passwords.csv'
#   row.to_csv(output_path, mode="a", header=False)

def get_password():
  try:
    with open('data.json', 'r') as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showerror(title='File not found', message="File does not exist")
  else:
    try:
      website = data[website_input.get()]
    except KeyError:
      messagebox.showerror(title="No password", message="No password for that website")
    else:
      messagebox.showinfo(title=website_input.get(), message=f"email:{website['email']} \npassword:{website['password']}")

website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)

search_button = tkinter.Button(text="Search", width=13, command=get_password)
search_button.grid(row=1, column=2)

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0)

website_input = tkinter.Entry(width=18)
website_input.grid(row=1, column=1)

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'alonzosanchez3@gmail.com')

password_input = tkinter.Entry(width=18)
password_input.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generate Password", width=13, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()