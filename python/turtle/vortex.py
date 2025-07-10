import turtle
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

colors = ["red", "orange", "yellow", "lime", "cyan", "blue", "purple", "white"]

# Draw illusion
for i in range(200):
    pen.pencolor(colors[i % len(colors)])
    pen.circle(100)
    pen.right(10)  # Rotate a little
    pen.forward(5)  # Move slightly forward

screen.mainloop()
