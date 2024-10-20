import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("U.S. States Game")

#You can add new shape to turtle using the below command and the file path
img = "blank_states_img.gif"
screen.addshape(img)
timmy = Turtle()
timmy.shape(img)

#read the 50_states.csv file
data = pandas.read_csv("50_states.csv")

answers = []
do_play = True
scribble = Turtle()
scribble.hideturtle()
scribble.penup()
while do_play:
    answer_state = screen.textinput(title=f"{len(answers)}/50 States Correct", prompt="what's another state name").title()
    df = data[data.state == answer_state]
    if answer_state.lower() == "exit":
        break
    elif not (df.empty or answer_state in answers):
        answers.append(answer_state)
        scribble.goto(df.x.item(), df.y.item())
        scribble.write(answer_state)

screen.exitonclick()