from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.pensize(5)
        self.goto(-250,260)
        self.level=1
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.write(f"Level {self.level}",font=FONT)
        
    def game_over(self):
        self.goto(-50,0)
        self.write("Game over", font=FONT)
        
