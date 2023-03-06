import turtle
from turtle import Screen
from score import Score
import time
from snake import Snake
from food import Food

screen = Screen()
scoreboard = Score()
screen.title("Snake game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.collision()
        scoreboard.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()

turtle.exitonclick()
