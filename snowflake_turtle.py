from turtle import *
import random


shape("turtle")
speed(5)
#pencolor("white")
colors = ["blue", "purple", "cyan", "white", "yellow", "red", "green", "orange"]
pensize(6)
#Screen().bgcolor("turquoise")
Screen().bgcolor("black")

def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def snowflake_arm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)

def snowflake():
    for x in range(0,18):
        color(random.choice(colors))
        snowflake_arm()
        right(20)

snowflake()

Screen().exitonclick()
