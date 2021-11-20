import turtle 
import math

t=turtle.Turtle()
turtle.Screen().bgcolor('black')
t.pencolor('white')
t.speed(0)

for i in range(2000):
    t.forward(10)
    t.left(math.sin(i/10)*25)
    t.left(20)


turtle.done()