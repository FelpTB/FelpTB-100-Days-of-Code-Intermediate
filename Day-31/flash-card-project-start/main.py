import tkinter
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
card_atual = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ----------------------SWITCH WORDS--------------------- #


def switch_words():
    global card_atual, flip_timer
    window.after_cancel(flip_timer)
    card_atual = random.choice(to_learn)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(word, text=card_atual["French"])
    canvas.itemconfig(language, text="French")
    flip_timer = window.after(3000, func=flipcard)

def flipcard():
    global card_atual
    card_atual = random.choice(to_learn)
    canvas.itemconfig(word, text=card_atual["English"])
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(card, image=card_back_img)

def not_learned():
    to_learn.remove(card_atual)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    switch_words()



# ----------------------UI INTERFACE--------------------- #


window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flipcard)


#Cards
canvas = tkinter.Canvas(width=800, height=526)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")

card = canvas.create_image(400,263,image=card_front_img)
canvas.grid(column=0,row=1, columnspan=2)


#buttons
right_image = tkinter.PhotoImage(file="images/right.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")


right = tkinter.Button(image=right_image, highlightthickness=0, command=switch_words)
wrong = tkinter.Button(image=wrong_image, highlightthickness=0, command=not_learned)


right.grid(column=0,row=2)
wrong.grid(column=1,row=2)




#Texts
language = canvas.create_text(400,150,text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400,263,text="Trouve", font=("Arial", 60, "bold"))



window.mainloop()

