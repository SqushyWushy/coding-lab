import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("red")
screen.title("Spiral Vibes")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Generate rainbow colors (0-1 floats)
num_colors = 360
colors = [colorsys.hsv_to_rgb(h / num_colors, 1, 1) for h in range(num_colors)]

# Draw spiral
for i in range(500):
    pen.pencolor(colors[i % num_colors])  # Now using 0-1 floats!
    pen.forward(i * 0.5)
    pen.right(59)

# Keep window open
turtle.done()
