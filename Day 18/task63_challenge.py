from turtle import Turtle,  Screen
turtle = Turtle()

for i in range(10):
    turtle.forward(20)    
    turtle.penup()        
    turtle.forward(10)    
    turtle.pendown()     
    
screen = Screen()
screen.exitonclick()

