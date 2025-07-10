import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]


def draw_star(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pencolor(random.choice(colors))

    for _ in range(5):
        pen.forward(50)
        pen.right(144)


screen.onscreenclick(draw_star)
screen.mainloop()
