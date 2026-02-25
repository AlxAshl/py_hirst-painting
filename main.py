import colorgram
import turtle
from turtle import Screen
import random

colors_list = [(230, 220, 208), (195, 158, 123), (138, 163, 182), (216, 226, 219), (215, 221, 228), (142, 88, 72), (78, 101, 128), (230, 217, 222), (182, 143, 157), (139, 172, 156)]

turtle.colormode(255)
turtle_1 = turtle.Turtle()
turtle_1.penup()
turtle_1.hideturtle()

for step in range (10):
    if step == 0:
        turtle_1.goto(-200, -200)
    else:
        turtle_1.left(90)
        turtle_1.forward(50)
        turtle_1.right(90)
        turtle_1.back(500)
    for _ in range(10):
        turtle_1.dot(20,random.choice(colors_list))
        turtle_1.forward(50)

screen = Screen()
screen.exitonclick()

# colors = colorgram.extract('hirst.jpg', 30)
# first_color = colors[0] #(r=230, g=220, b=208)
# rgb = first_color.rgb
# colors_list = []
# for color in colors:
#     rgb = color.rgb
#     color_tuple = (rgb.r, rgb.g, rgb.b)
#     colors_list.append(color_tuple)