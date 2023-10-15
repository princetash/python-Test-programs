import turtle
import math

bob = turtle.Turtle()


# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)


# square(bob, 200)

# drawing a polygon using turtle
# n = number os sides that the polygon has

def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# polygon(bob, 7, 70)

# drawing a circle


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(bob, n, length)


circle(bob, 10)

turtle.mainloop()
