import turtle as t
import random



my_turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

my_turtle.speed("fastest")
my_turtle.setheading(225)
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dot = 100
for _ in range(1, number_of_dot + 1):
    my_turtle.dot(20,random_color())
    my_turtle.forward(50)
    if _ % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)






screen = t.Screen()
screen.exitonclick()
