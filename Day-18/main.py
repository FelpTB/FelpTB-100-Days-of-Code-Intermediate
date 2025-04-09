from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red","green")
cores = [
    "red", "green", "blue", "orange", "purple", "pink", "brown", "yellow", "cyan", "magenta",
    "gold", "silver", "violet", "indigo", "maroon", "lime", "teal", "navy", "peachpuff", "turquoise",
    "tomato", "peru", "plum", "sienna", "thistle", "mediumslateblue", "darkseagreen", "slategray", "chocolate", "darkkhaki",
    "coral", "darkred", "darkgreen", "darkblue", "darkorange", "darkorchid", "darkcyan", "darkmagenta", "darkgoldenrod", "darkolivegreen",
    "deeppink", "deepskyblue", "dodgerblue", "firebrick", "forestgreen", "fuchsia", "goldenrod", "greenyellow", "hotpink", "indianred"
]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     random_color = (r, g, b)
#     return random_color


#Formas geométricas
# x = 120
# j = 3
# while j <= 20:
#     i = 0
#     timmy.color(random.choice(cores))
#     while i < j:
#         timmy.forward(20)
#         timmy.left(x)
#         i += 1
#     j += 1
#     x = 360/j


#Caminho aleatório
# timmy.width(5)
# while True:
#     i = random.randint(1,2)
#     timmy.color(random.choice(cores))
#     match i:
#       case 1:
#          timmy.left(90)
#       case 2:
#          timmy.right(90)
#     timmy.forward(30)


timmy.speed("fastest")
def draw_spirograph(size):
    for _ in range(int(360/size)):
        timmy.color(random.choice(cores))
        timmy.circle(100)
        heading = timmy.heading()
        timmy.setheading(heading+size)

draw_spirograph(1)


# for _ in range(15):
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)


screen = Screen()
screen.exitonclick()