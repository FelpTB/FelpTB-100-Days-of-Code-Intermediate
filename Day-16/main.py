import turtle
import anther_module
from turtle import Turtle, Screen
import prettytable
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu","Charmander","Squirtle"])
table.add_column("Type", ["Electric","Fire","Water"])
table.align = "l"
print(table)

# print(anther_module.anoter_variable)
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red","Green")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
