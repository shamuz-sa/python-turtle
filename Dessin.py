import turtle
t=turtle.Turtle()
turtle.Screen().bgcolor("black")

for i in range(20):
    t.color("white")
    t.pensize(1)
    t.circle(80, steps=5)
    t.right(100)

turtle.done()
