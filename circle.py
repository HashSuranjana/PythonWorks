import turtle
import math

t = turtle.Turtle()

colors = ["red","green","yellow","orange","pink","blue"]

radius = 10
Radius = 0


def area (r,R) :
    t.begin_fill()
    t.circle(r,180)
    t.end_fill()


    return area


for i in range(8) :

    if i<len(colors) :

        t.fillcolor(colors[i])

    else :

        t.fillcolor(colors[i-6])


    area(radius,Radius)
    radius += 10
    Radius +=10

turtle.done()