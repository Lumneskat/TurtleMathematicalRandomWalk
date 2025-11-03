import random
from turtle import Turtle, Screen, colormode
from random import Random

def random_color():

    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

def direction_choose():
    x = 0
    y = 0
    direction = random.randint(1,4)

    if direction == 1:
        x += 1
    elif direction == 2:
        x += -1
    elif direction == 3:
        y += 1
    elif direction == 4:
        y -= 1
    return x, y

def move(direction, dic_directions, move_amount):

    if direction == (1,0):
        my_turtle.setheading(dic_directions["east"])
        my_turtle.forward(move_amount)
    elif direction == (-1,0):
        my_turtle.setheading(dic_directions["west"])
        my_turtle.forward(move_amount)
    elif direction == (0,1):
        my_turtle.setheading(dic_directions["south"])
        my_turtle.forward(move_amount)
    elif direction == (0,-1):
        my_turtle.setheading(dic_directions["north"])
        my_turtle.forward(move_amount)

def step_made(steps):
    steps += 1
    return steps


colormode(255)

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(10)
my_turtle.speed(100)

directions = {"north": 90, "east": 0, "south": 270, "west": 180}

steps_made = 0
move_distance = 20
move_direction = 0, 0

my_turtle.penup()
my_turtle.setpos(0,0)
my_turtle.pendown()

while steps_made <= 500:

    my_turtle.color(random_color())
    move_direction = direction_choose()
    move(move_direction, directions, move_distance)
    steps_made = step_made(steps_made)




screen = Screen()
screen.exitonclick()