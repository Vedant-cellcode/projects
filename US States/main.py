import pandas as pd
from turtle import Turtle, Screen

states = Turtle()
state1=Turtle()
#made 2 objects:1-For showing the image of map that is states.shape(image) 2- For writing the name of states
# if the same object is used for showing the image of map and writing the name of states then after 1st guess the screen becomes white
screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
states.shape(image)
data = pd.read_csv('50_states.csv')
state_name=[]
missing_states = []
while len(state_name)<=50:
    answer = screen.textinput(title=f'{len(state_name)}/50 are correct, US State Game',prompt='Guess the state').title()
    all_states = data.state.to_list()
    if answer =='Exit':
        state1.hideturtle()
        missing_states=[s for s in all_states if s not in state_name]
        print(missing_states)
        break
    if answer in all_states:
        state_name.append(answer)
        guess = data[data.state == answer]
        guess_x = (guess.x.item())
        guess_y = (guess.y.item())
        state1.hideturtle()
        state1.penup()
        state1.goto(guess_x, guess_y)
        state1.write(answer)
df=pd.DataFrame(missing_states)
df.to_csv('not guessed states')
screen.exitonclick()
