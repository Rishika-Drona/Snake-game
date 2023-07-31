#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
import random

w = 500
h = 500
fs = 10
d = 100  # milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def r():
    global snake, turn, ballX, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    turn = "up"
    ballX = nun()
    food.goto(ballX)
    hall()

def hall():
    global turn

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[turn][0]
    new_head[1] = snake[-1][1] + offsets[turn][1]

    if new_head in snake[:-1]:  
        r()
    else:
        snake.append(new_head)

        if not ball():
            snake.pop(0)  

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()
 #clears all the stamps

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
 #updates the turtle.screen screen

        turtle.ontimer(hall, d)

def ball():
    global ballX
    if dist(snake[-1], ballX) < 20:
        ballX = nun()
        food.goto(ballX)
        return True
    return False

def nun():
    x = random.randint(- w / 2 + fs, w / 2 - fs)
    y = random.randint(- h / 2 + fs, h / 2 - fs)
    return (x, y)

def dist(poos1, poos2):
    x1, y1 = poos1
    x2, y2 = poos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global turn
    if turn != "down":
        turn = "up"

def go_right():
    global turn
    if turn != "left":
        turn = "right"

def go_down():
    global turn
    if turn != "up":
        turn = "down"

def go_left():
    global turn
    if turn != "right":
        turn = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("snake")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.shapesize(fs / 20) 
food.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

r()
turtle.done()


# In[ ]:




