from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_screen = Screen()
my_turtle.pensize(10)
my_turtle.speed("fastest")

colors = ["red", "blue", "green", "yellow", "orange", "purple", "black", "purple"]
direction = [0, 90, 180, 270]

for _ in range(200):
    my_turtle.color(random.choice(colors))
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))
    
my_screen.exitonclick()