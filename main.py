from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("My Snake Game")
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score = Score()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

game = True

while game:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()
    
    #detect collision with food
    if my_snake.segments[0].distance(my_food) < 15: #each segments are turtles
        my_food.move()
        my_score.increase_score()
        my_snake.extend_snake()
    
    #detect collision with wall
    if my_snake.segments[0].xcor() > 290 or my_snake.segments[0].xcor() < -290 or my_snake.segments[0].ycor() > 290 or my_snake.segments[0].ycor() < -290:
        my_score.reset_score()
        my_snake.reset_snake()
    
    
    #detect collision with tail
    for segment in my_snake.segments[1:]: #using slicing here. [1:0] -> looping except the 1st segment ([0]) since that is the head
        if my_snake.segments[0].distance(segment) < 10:
            my_score.reset_score()
            my_snake.reset_snake()
        
        



        


    
    




my_screen.exitonclick()
