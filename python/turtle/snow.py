import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
fractal = turtle.Turtle()
fractal.speed(0)
fractal.color("cyan")
fractal.pensize(2)


# Koch curve function
def koch(length, level):
    if level == 0:
        fractal.forward(length)
    else:
        length /= 3.0
        koch(length, level - 1)
        fractal.left(60)
        koch(length, level - 1)
        fractal.right(120)
        koch(length, level - 1)
        fractal.left(60)
        koch(length, level - 1)


# Draw the Koch Snowflake
def draw_koch_snowflake(size, level):
    fractal.penup()
    fractal.goto(-size / 2, size / 3)
    fractal.pendown()
    for _ in range(3):
        koch(size, level)
        fractal.right(120)


draw_koch_snowflake(300, 4)  # size, recursion level

fractal.hideturtle()
screen.mainloop()
