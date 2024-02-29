from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from tkinter import messagebox

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

scoreboard = Scoreboard()
paddle_left = Paddle(-350)
paddle_right = Paddle(350)
ball = Ball()

screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if scoreboard.l_score == 7 or scoreboard.r_score == 7:
        if scoreboard.l_score > scoreboard.r_score:
            messagebox.showinfo("Game Over","Left Win")
        else:
            messagebox.showinfo("Game Over","Right Win")
        break
    
    if ball.xcor() > 390:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.r_point()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
