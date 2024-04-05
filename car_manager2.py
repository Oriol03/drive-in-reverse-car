from turtle import Turtle
import  random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION=[-212.5,-127.5,-42.5,42.5,127.5,212.5]

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.move_speed=0.09
        self.out_race=0
        
    def create_car(self):
        random_chance=random.randint(1,10)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=3,stretch_wid=2)
            new_car.penup()
            new_car.seth(270)
            new_color=random.choice(COLORS)
            new_car.color(new_color)
            rand_x=random.choice(STARTING_POSITION)
            
            new_car.goto(rand_x,300)
            self.all_cars.append(new_car)
            
        
        
    def move_car(self):
        for car in self.all_cars:
            car.fd(STARTING_MOVE_DISTANCE)