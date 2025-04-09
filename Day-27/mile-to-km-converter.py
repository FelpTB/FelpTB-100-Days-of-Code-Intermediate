from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=100, height=100)
window.config(padx=50 ,pady=50)


#Layout da interface
miles = Label(text="Miles")
km = Label(text="Km")
equalTo = Label(text="Is equal to")
miles.grid(row=0, column=2)
km.grid(row=1, column=2)
equalTo.grid(row=1, column=0)

#Configuração do resultado
result = Label(text="0")
result.grid(row=1, column=1)

#Configuração do botão
def convert():
    d = int(input.get())
    result.config(text=(round((d*1.6), 2)))
button = Button(text="Convert", command=convert)
button.grid(row=2, column=1)


#Configuração da entrada
input = Entry()
input.grid(row=0, column=1)


window.mainloop()