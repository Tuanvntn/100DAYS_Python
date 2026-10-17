from turtle import Turtle
import random


COLORS = ["red", "black", "blue", "pink", "yellow", "brown"]
STARING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2



class Car_manager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("car_chinh_size.gif")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()

            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.setheading(180)

            self.all_cars.append(new_car)


    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



