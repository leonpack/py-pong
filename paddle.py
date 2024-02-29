from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position, 0)
        self.paddle_speed = 35

    def go_up(self):
        if self.ycor() < 235:
            new_ypos = self.ycor() + self.paddle_speed
            self.goto(self.xcor(), new_ypos)

    def go_down(self):
        if self.ycor() > -235:    
            new_ypos = self.ycor() - self.paddle_speed
            self.goto(self.xcor(), new_ypos)