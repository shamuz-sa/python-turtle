import turtle
t=turtle.Turtle()
t.left(90)
t.penup()
t.goto(0, -100)
t.pendown()
turtle.Screen().bgcolor("black")
t.pencolor("white")
t.speed(0)

def tree(l):
    if(l<10):
        return
    else:
        t.forward(l)
        t.left(30)
        tree(3*l/4)
        t.right(60)
        tree(3*l/4)
        t.left(30)
        t.backward(l)

        
tree(100)
turtle.done()