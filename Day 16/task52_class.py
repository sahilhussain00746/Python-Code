# All about Class

# Let turtle is a file and Turtle is a class

# import turtle
# # Method 1 is import a library and use the Turtle class 
# turtle_v1 = turtle.Turtle() 

# Method 2 is only import the class from a library
from turtle import Turtle
turtle_v2 = Turtle()
print(turtle_v2) #This will print the location of the class

from turtle import Screen
my_screen = Screen()
print(my_screen.canvheight) # After run the code, a screen will pop up and its size will be 300
