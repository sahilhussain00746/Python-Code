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


my_turtle.speed("fastest")
direction = [0, 90, 180, 270]

# for _ in range(100):
#     my_turtle.color(randowm_color())
#     my_turtle.circle(100)
#     my_turtle.setheading(my_turtle.heading() + 10)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        my_turtle.color(randowm_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)
        
draw_spirograph(10)
    
my_screen.exitonclick()