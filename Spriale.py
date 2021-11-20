import turtle

colors = ['red', 'purple', 'blue','green', 'orange', 'yellow']
t=turtle.Pen()
turtle.bgcolor('black')
turtle.speed(2)
for a in range(180):
    t.pencolor(colors[a%6])
    t.width(a/180+1)
    t.forward(a)
    t.left(59)
turtle.done()