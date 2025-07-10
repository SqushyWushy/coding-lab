import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Solar System")
screen.tracer(0)  # Turn off automatic animation

# Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)
sun.penup()


# Planet setup function
def create_planet(color, distance, size, speed):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    planet.distance = distance
    planet.angle = 0
    planet.speed = speed
    return planet


# Planets: Mercury, Venus, Earth, Mars
planets = [
    create_planet("gray", 40, 0.3, 0.04),  # Mercury
    create_planet("orange", 70, 0.5, 0.03),  # Venus
    create_planet("blue", 100, 0.6, 0.02),  # Earth
    create_planet("red", 140, 0.5, 0.015),  # Mars
]


# Orbit drawing (optional)
def draw_orbit(radius):
    orbit = turtle.Turtle()
    orbit.hideturtle()
    orbit.speed(0)
    orbit.color("white")
    orbit.penup()
    orbit.goto(0, -radius)
    orbit.pendown()
    orbit.circle(radius)


for planet in planets:
    draw_orbit(planet.distance)

# Simulation loop
while True:
    for planet in planets:
        x = planet.distance * math.cos(planet.angle)
        y = planet.distance * math.sin(planet.angle)
        planet.goto(x, y)
        planet.angle += planet.speed
    screen.update()
    time.sleep(0.01)
