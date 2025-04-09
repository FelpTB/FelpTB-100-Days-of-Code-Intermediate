import tkinter
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- SEARCH FUNCTION ---------------------------------- #
def searcher(website):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            password = data[website]["password"]
            email = data[website]["email"]
    except FileNotFoundError:
        messagebox.showinfo(title="ERRO",message="Não há nada salvo")
    except KeyError:
        messagebox.showinfo(title="ERRO",message="Não há nenhuma senha para este site")
    else:
        messagebox.showinfo(title=website, message=f"O Email é: {email}\nA senha é: {password}")


def searchAux():
    searcher(websiteEntry.get())



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    passwordEntry.delete(0, tkinter.END)
    passwordLetters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    passwordNumbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    passwordSymbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = passwordSymbols + passwordLetters + passwordNumbers

    random.shuffle(password_list)

    senha = "".join(password_list)
    passwordEntry.insert(0, senha)
    pyperclip.copy(senha)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    websiteInfo = websiteEntry.get()
    emailInfo = emailEntry.get()
    passswordInfo = passwordEntry.get()
    new_data = {
        websiteInfo: {
            "email": emailInfo,
            "password": passswordInfo,
        }
    }

    if websiteInfo and emailInfo and passswordInfo:
        is_ok = messagebox.askokcancel(title=websiteInfo, message=f"These are the details entered\nEmail:{emailInfo}\nPassword:{passswordInfo}\n It´s ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                websiteEntry.delete(0, tkinter.END)
                passwordEntry.delete(0, tkinter.END)
    else:
        messagebox.showinfo(title="404",message="Don't let any field empty!")



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

#canva
canva = tkinter.Canvas(width=200, height=208)
img = tkinter.PhotoImage(file="logo.png")
canva.create_image(100,104,image=img)
canva.grid(column=1,row=0)

#buttons
generate = tkinter.Button(text="Generate Password",width=14, command=generate)
add = tkinter.Button(text="Add",width=43,command=save)
search = tkinter.Button(text="Search",width=14,command=searchAux)

generate.grid(column=2,row=3)
add.grid(column=1,row=4,columnspan=2)
search.grid(column=2,row=1)

#labels
website = tkinter.Label(text="Website:")
email = tkinter.Label(text="E-mail/Username:")
password = tkinter.Label(text="Password:")

website.grid(column=0,row=1)
email.grid(column=0,row=2)
password.grid(column=0,row=3)

#inputs
websiteEntry = tkinter.Entry(width=33)
emailEntry = tkinter.Entry(width=51)
passwordEntry = tkinter.Entry(width=33)

websiteEntry.grid(column=1,row=1)
emailEntry.grid(column=1,row=2,columnspan=2)
passwordEntry.grid(column=1,row=3)

#Ja comceça clicado
websiteEntry.focus()

#Ja comeca escrito
emailEntry.insert(0,"felipe.baldim@sou.unifal-mg.edu.br")


window.mainloop()