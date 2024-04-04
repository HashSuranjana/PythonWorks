import turtle
t = turtle.Turtle()

def square(color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


#Creating Windows Logo

t.screen.bgcolor("black")
t.pensize(3)
square("green")
t.pencolor("black")
t.backward(110)
square("red")
t.pencolor("black")
t.right(90)
t.forward(110)
t.left(90)
square("blue")
t.forward(100)
t.pencolor("black")
t.forward(10)
square("yellow")

t.pencolor("black")
t.right(90)
t.forward(40)
t.pensize(10)
t.left(90)
t.pencolor("white")

#Creating XP Name

t.right(45)
t.forward(40)
t.right(90)
t.forward(40)
t.backward(80)
t.forward(40)
t.left(90)
t.forward(40)

t.penup()
t.left(45)
t.forward(20)
t.left(90)
t.pendown()

t.forward(56.5685)
t.penup()
t.backward(28.2842)
t.pendown()
t.right(90)
t.forward(15)
t.circle(14.1421,180)
t.forward(6)
t.penup()

turtle.done()










































