#Jonathan Veltri
#CS-175L
#Stop Sign



import turtle
import math

turtle.setup(400, 400)

t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(-50, -100)
t.pendown()
t.color("red")
t.shape("turtle")
t.begin_fill()
for x in range (8):
    t.forward(100)
    t.left(45)
t.end_fill()
t.penup()
t.goto(-70, 10)
t.pendown
t.color("white")
t.write("STOP", font=("Ariel", "40"))
t.hideturtle
turtle.done()