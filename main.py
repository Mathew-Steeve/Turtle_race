from turtle import Turtle, Screen
import random

jam = [Turtle() for i in range(6)]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)


colors = ['blue', 'yellow', 'orange', 'red', 'green', 'violet']

user_choice = screen.textinput(title='want to bet', prompt="Which color is your bet ?")
for k in range(6):
    jam[k].shape('turtle')
    jam[k].color(colors[k])
    jam[k].penup()
y = 0
for j in range(6):
    jam[j].goto(-230, -100+y)
    y += 50
if user_choice:
    is_race_on = True
while is_race_on:
    for turtle in jam:
        if turtle.xcor() > 230:
            is_race_on = False
            color = turtle.pencolor()
            if user_choice == color:
                print(f"You win ! The winning color is {color}.")

            else:
                print(f"You lose .The winning color is {color}.")
        
        forward = random.randint(0, 10)
        turtle.forward(forward)

screen.exitonclick()
