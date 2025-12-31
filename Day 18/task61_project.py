# Here We are working on turtle module
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red", "blue")

# Making a square using turtle

for move in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)



my_screen = Screen()
my_screen.exitonclick()