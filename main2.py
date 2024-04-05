import time
from turtle import Screen, Turtle
from player2 import Player
from car_manager2 import CarManager
from scoreboard2 import Scoreboard
import random


screen=Screen()
screen.setup(width=510, height=600)
screen.bgcolor("black")
screen.title("drive in reverse")
screen.tracer(0)

position_terrain=[(-165,-300),(-80,-300),(5,-300),(90,-300),(175,-300)]
for position in position_terrain:
    ligne=Turtle()
    ligne.hideturtle()
    ligne.pensize(3)
    ligne.color("white")
    ligne.penup()
    ligne.seth(90)
    ligne.goto(position)
    while ligne.ycor()< 300:
        ligne.pendown()
        ligne.fd(10)
        ligne.penup()
        ligne.fd(10)



car=CarManager()
player=Player()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")
screen.onkey(player.move_right,"Right")
screen.onkey(player.move_left,"Left")
        
game_on=True

while game_on:
    screen.update()
    time.sleep(car.move_speed)
    car.create_car()
    car.move_car()

    scoreboard.show_score()
    # Detection with car
    
    for each_car in car.all_cars:
        if player.distance(each_car)  < 40:
            game_on=False
            scoreboard.game_over()
       
        if each_car.ycor()< -320 and (each_car in  car.all_cars):
            car.out_race+=1  
            car.all_cars.remove(each_car)
            each_car.clear()
    
    
    if car.out_race==0:
        pass
    elif car.out_race%5 == 0:
        scoreboard.level+=1
        car.move_speed*=0.9
        car.out_race=0


screen.exitonclick()