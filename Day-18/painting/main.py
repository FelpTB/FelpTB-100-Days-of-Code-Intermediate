import colorgram
import turtle as t
import random
t.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('art.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new = (r, g, b)
#    rgb_colors.append(new)
#
# print(rgb_colors)

color_list = [(224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

tim = t.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
y = -300
tim.goto(-300, y)
for _ in range(10):
    for _ in range(10):
      tim.pendown()
      tim.dot(20, random.choice(color_list))
      tim.penup()
      tim.forward(50)
    y += 50
    tim.goto(-300, y)


screen = t.Screen()
screen.exitonclick()