import turtle
import pandas
import tkinter as tk
from tkinter import messagebox

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
allStates = data.state.to_list()


#Escreve o nome do estado na coordenada certa
def escreve(resposta):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    estado = data[data['state'] == resposta]
    t.goto(estado.x.item(), estado.y.item())
    t.write(resposta)

def exibir_mensagem(mensagem):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    messagebox.showinfo("Informação", mensagem)
    root.destroy()  # Destrói a janela principal

score = 0
error = 0
while score < 50 and error < 5:

    answer_state = screen.textinput(title=f"Score:{score}/50, Errors:{error}/5",
                                    prompt="What's another state name?").title()

    if answer_state in allStates:
        escreve(answer_state)
        score += 1
    else:
        error += 1

if score >= 50:
    exibir_mensagem("You Win!")
else:
    exibir_mensagem(f"Your final score is: {score}")




#Pegar as coodenadas dos estados
# def mouse_coord(x ,y):
#     print(x, y)
#
#
# turtle.onscreenclick(mouse_coord)
# turtle.mainloop()

screen.exitonclick()