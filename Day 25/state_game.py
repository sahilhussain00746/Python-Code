import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_States = data.state.to_list()

guess_state = []

while len(guess_state ) < 50:
    answer_State = screen.textinput(title=f"{len(guess_state)}/50 Guess", prompt="Name the State").title()
    
    if answer_State == "Exit":
        missing_state = []
        for state in all_States:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_know.csv")
        print(missing_state)
        break
    elif answer_State in all_States:
        guess_state.append(answer_State)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_State]
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(answer_State)
