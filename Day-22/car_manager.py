COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager():
    
    def __init__(self):
        # super().__init__()
        self.all_cars=[]
    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y= random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)