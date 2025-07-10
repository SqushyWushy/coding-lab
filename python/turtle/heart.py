import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Draw the heart
heart = turtle.Turtle()
heart.color("red")
heart.pensize(3)
heart.speed(1)

heart.begin_fill()
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)
heart.left(120)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()
heart.hideturtle()

# Write the text
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("black")
text.goto(0, 60)
text.write("T + J", align="center", font=("Arial", 28, "bold"))

# Add confetti around the heart
confetti = turtle.Turtle()
confetti.hideturtle()
confetti.penup()
confetti.speed(0)
colors = ["gold", "blue", "green", "purple", "orange", "hot pink"]

for _ in range(100):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    confetti.goto(x, y)
    confetti.dot(random.randint(5, 12), random.choice(colors))

# Add sparkle burst effect
sparkle = turtle.Turtle()
sparkle.hideturtle()
sparkle.speed(0)
sparkle.pensize(2)


def draw_star(x, y, size, color):
    sparkle.penup()
    sparkle.goto(x, y)
    sparkle.setheading(0)
    sparkle.pendown()
    sparkle.color(color)
    for _ in range(5):
        sparkle.forward(size)
        sparkle.right(144)


for _ in range(10):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    size = random.randint(10, 25)
    color = random.choice(colors)
    draw_star(x, y, size, color)

# Keep window open
screen.mainloop()
