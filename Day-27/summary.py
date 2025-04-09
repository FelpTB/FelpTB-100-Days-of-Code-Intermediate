from tkinter import *

window = Tk()

window.title("GUI")
window.minsize(width=500, height=300)
clicks = 0




# Label

# label = Label(text="Labelll", font=("Arial",24,"bold"))
# #label.pack(side="left")
# label.pack(side="top")
# #label.pack(side="bottom")
#
# label.config(text="Lable Aqui")

#Entry
# input = Entry()
# input.pack()

#Button
# def click():
#     print("click")
#     text = input.get()
#     label.config(text=text)
#
#
# button = Button(text="botão", command=click)
# button.pack()


#Text
# texto = Text(height=5, width=30)
# texto.focus()
# texto.insert(END,"Texto de exemplo com multiplas linhas")
# print(texto.get("1.0",END))
# texto.pack()

#Spinbox
# def spinbox_used():
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


#Scale

# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()


#Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

#Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

#Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


#pack
# pack = Label(text="Pack")
# pack.pack(side="left")

#Place
# place = Label(text="Place")
# place.place(x=0,y=0)

#Grid
grid = Label(text="Grid")
grid.grid(column=0, row=0)
grid2 = Label(text="Grid2")
grid2.grid(column=1, row=1)
grid3 = Label(text="Grid3")
grid3.grid(column=2, row=0)
grid4 = Label(text="Grid4")
grid4.grid(column=3, row=3)
grid5 = Label(text="Grid5")
grid5.grid(column=1, row=0)



window.mainloop()