from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_screen = Screen()

colors = ["red", "blue", "green", "yellow", "orange", "purple", "black", "purple"]

def draw(rotation):
    angle = 360/rotation
    for _ in range(rotation):
        my_turtle.forward(100)
        my_turtle.right(angle)
        
        
for i in range(3, 11):
    my_turtle.color(random.choice(colors))
    draw(i)



my_screen.exitonclick()