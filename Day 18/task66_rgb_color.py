import turtle as t
import random

my_turtle = t.Turtle()
my_screen = t.Screen()
t.colormode(255)

def randowm_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

my_turtle.pensize(10)
my_turtle.speed("fastest")
direction = [0, 90, 180, 270]

for _ in range(200):
    my_turtle.color(randowm_color())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))
    
my_screen.exitonclick()