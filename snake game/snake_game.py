import turtle
from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('my snake game'.title())

segments = []
for i in [(0, 0), (-20, 0), (-40, 0)]:
    segment = Turtle(shape='square')
    segment.color('white')
    segment.penup()
    segment.goto(i)
    segments.append(segment)
def food():
    global foods
    foods = Turtle()
    foods.shape('square')
    foods.color('blue')
    foods.penup()
    foods.shapesize(0.5, 0.5)
    foods.goto(random.randint(-280, 280), random.randint(-280, 280))

score_display = Turtle()
score_display.color('white')
score_display.penup()
score_display.goto(0, 270)
score_display.hideturtle()
scores = 0

is_moving = True

def snake_up():
    if segments[0].heading() != 270:
        segments[0].setheading(90)

def snake_left():
    if segments[0].heading() != 0:
        segments[0].setheading(180)

def snake_down():
    if segments[0].heading() != 90:
        segments[0].setheading(270)

def snake_right():
    if segments[0].heading() != 180:
        segments[0].setheading(0)

screen.listen()
screen.onkey(snake_up, 'Up')
screen.onkey(snake_down, 'Down')
screen.onkey(snake_right, 'Right')
screen.onkey(snake_left, 'Left')

def score():
    global scores
    scores += 1
    score_display.clear()
    score_display.write(f"Score: {scores}", align="center", font=("Courier", 16, "normal"))


def extend_snake():
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.penup()
    a=segments[-1].pos()
    new_segment.goto(a)
    segments.append(new_segment)


def is_collided():
    global is_moving
    if segments[0].distance(foods) < 15:
        new_food_x = random.randint(-280, 280)
        new_food_y = random.randint(-280, 280)
        foods.goto(new_food_x, new_food_y)
        score()
        extend_snake()
food()
while is_moving:
    screen.update()
    time.sleep(0.1)
    for seg_index in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_index - 1].xcor()
        new_y = segments[seg_index - 1].ycor()
        segments[seg_index].goto(new_x, new_y)
    segments[0].forward(20)
    is_collided()
    if segments[0].xcor() > 290 or segments[0].xcor() < -290 or segments[0].ycor() > 290 or segments[0].ycor() < -290:
        is_moving = False
        score_display.goto(0, 0)
        score_display.write("GAME OVER", align='center', font=("Courier", 24, "normal"))
    for i in segments[1:]:
        if segments[0].distance(i)<15:
            is_moving=False
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align='center', font=("Courier", 24, "normal"))


screen.exitonclick()
