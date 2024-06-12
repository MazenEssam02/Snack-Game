from turtle import Turtle, Screen
from snake import Snake
from Food import Food
from Score import Score
import time

def game_boundaries():
    turtle = Turtle()
    turtle.color("white")
    turtle.hideturtle()
    turtle.pu()
    turtle.goto(-305, -305)
    turtle.pd()
    turtle.speed('fastest')
    for i in range(4):
        turtle.forward(610)
        turtle.left(90)
    
screen = Screen()
screen.bgcolor('black')
game_boundaries()
screen.title("Snake Game")
screen.setup(width=800, height=800)

snakes = Snake()
food = Food()
score = Score()

screen.tracer(0)
flag = 1
screen.listen()
screen.onkeypress(snakes.UP, 'Up')
screen.onkeypress(snakes.DOWN, 'Down')
screen.onkeypress(snakes.RIGHT, 'Right')
screen.onkeypress(snakes.LEFT, 'Left')
while flag:
    time.sleep(0.1)
    screen.update()
    score.update_scoreboard()
    snakes.move()
    if snakes.head.xcor() > 300 or snakes.head.xcor() < -300 or snakes.head.ycor() > 300 or snakes.head.ycor() < -300:
        score.game_over()
        score.clear_motiv()
        flag = 0
    for segments in snakes.all_snakes:
        if segments == snakes.head:
            pass

        elif snakes.head.distance(segments) < 10:
            score.game_over()
            score.clear_motiv()
            flag = 0

    if snakes.head.distance(food) < 15:
        food.generatefood()
        snakes.extend()
        score.level_up()
        score.motivation()


screen.exitonclick()
