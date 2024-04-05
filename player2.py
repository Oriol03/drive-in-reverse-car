from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__() 
        self.penup()
        
        self.shape("turtle")
        self.color("white")
        self.speed(0)
        self.shapesize(stretch_len=2,stretch_wid=2)
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        self.seth(90)
        self.fd(MOVE_DISTANCE)
    def move_down(self):
        self.seth(270)
        self.fd(MOVE_DISTANCE) 
    def move_right(self):
        self.seth(0)
        self.fd(MOVE_DISTANCE)
    def move_left(self):
        self.seth(180)
        self.fd(MOVE_DISTANCE)   
        
    def is_finish_race(self):
        if self.ycor()> FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False 