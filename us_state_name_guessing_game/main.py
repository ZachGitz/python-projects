import turtle
import pandas

screen=turtle.Screen()
screen.title("State Name Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
guess=[]
states=data.state.to_list()
missing=[]
while len(guess)<50:
    ans = screen.textinput(title=f"Guessed {len(guess)}/50",prompt="Guess State Name").title()
    if(ans=="Exit"):
        for i in states:
            if i not in guess:
                missing.append(i)
        break
    if ans in states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[ans==data.state]
        t.goto(int(state.x),int(state.y))
        t.write(ans.title())
        guess.append(ans)

dict={"states":missing}
new_data=pandas.DataFrame(dict)
new_data.to_csv("All Missing States")
screen.exitonclick()