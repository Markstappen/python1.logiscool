familly_names= ["kosondi","karampalasis"]
names=["luc","alex","stefan","nicola","alexandros","marcel"]
for familly_name in familly_names:
    for name in names:
        print(name+" "+ familly_name)

import turtle
turtle.getscreen()
pen=turtle.Turtle()
pen.color('black')
pen.fillcolor("red")
pen.begin_fill()
for i in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()
pen.fillcolor("brown")
pen.begin_fill
pen.left(90)
pen.forward(100)
pen.right(30)
for i in range(3):
    pen.forward(100)
    pen.right(120)
pen.end_fill()








turtle.exitonclick()