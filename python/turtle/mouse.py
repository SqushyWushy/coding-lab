import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.title("Scared Turtle 🐢💨")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Setup turtle
runner = turtle.Turtle()
runner.shape("turtle")
runner.color("lime")
runner.penup()
runner.speed(0)


# Move turtle to random spot
def move_turtle_randomly():
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    runner.goto(x, y)


# Distance between turtle and mouse
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Trigger when mouse moves
def on_mouse_move(x, y):
    t_x, t_y = runner.pos()
    if distance(x, y, t_x, t_y) < 100:  # Too close!
        move_turtle_randomly()


# Track mouse movement
screen.onscreenclick(lambda x, y: None)  # (Bug workaround)
screen.getcanvas().bind(
    "<Motion>", lambda event: on_mouse_move(event.x - 400, 300 - event.y)
)

# Start with turtle in the center
runner.goto(0, 0)

# Keep screen open
screen.mainloop()
