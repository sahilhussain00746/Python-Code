import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 192, 203), (128, 0, 128), (0, 255, 255), (0, 128, 128), (0, 0, 0), (255, 255, 255), (128, 128, 128), (139, 0, 0), (0, 100, 0), (0, 0, 139), (47, 79, 79), (25, 25, 25), (231, 76, 60), (46, 204, 113), (52, 152, 219), (155, 89, 182), (241, 196, 15), (230, 126, 34), (26, 188, 156), (149, 165, 166), (255, 99, 71), (154, 205, 50), (72, 61, 139), (255, 20, 147), (70, 130, 180), (244, 164, 96), (34, 139, 34), (178, 34, 34), (218, 112, 214), (95, 158, 160), (255, 140, 0), (75, 0, 130), (60, 179, 113), (210, 105, 30), (123, 104, 238), (176, 224, 230), (152, 251, 152), (240, 128, 128), (255, 215, 0), (199, 21, 133), (0, 191, 255), (46, 139, 87), (255, 69, 0), (112, 128, 144)]

tim.speed("fastest")
tim.penup() 
tim.hideturtle() # this will hide the turtle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

numbers_of_dots = 100

for dot_count in range(1, numbers_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)        
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()