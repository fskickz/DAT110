import turtle
import random
stjerner = int(input("Hvor mange stjerner?"))
turtle.speed(0)
turtle.bgcolor("black")
turtle.penup()
turtle.backward(350)
turtle.pendown()
for i in range(0,stjerner):
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()
    for left in range(0, 360, 90):
        for colors in ["red","magenta", "blue", "cyan", "green", "yellow"]:
            turtle.color(colors)
            turtle.forward(50)
            turtle.backward(50)
            turtle.left(15)
turtle.done()
