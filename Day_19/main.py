from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
random.shuffle(colors)

for turtle_index in range(0,6):
    my_t = Turtle(shape="turtle")
    my_t.color(colors[turtle_index])
    my_t.penup()
    my_t.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(my_t)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your {user_bet} Turtle are win")
            else:
                print(f"Your {user_bet} Turtle are lose")
                print(f"{winning_color} Turtle win")
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)




screen.exitonclick()



