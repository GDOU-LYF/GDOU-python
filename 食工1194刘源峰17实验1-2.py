import turtle
t=turtle.Pen()
turtle.bgcolor("black")
sides=2
colors=["red","yellow","blue","orange","green"]
for x in range(270):
    t.pencolor(colors[x%sides])
    t.forward(x*2)
    t.left(360/sides+1)
    t.width(x*sides/150)
