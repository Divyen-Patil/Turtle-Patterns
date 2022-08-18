import turtle
turtle.pensize(5)
turtle.speed(10)
turtle.bgcolor('Black')

for i in range(10):
    for colours in['yellow','red','pink','blue','white','green']:
        turtle.color(colours)
        turtle.circle(130)
        turtle.left(100)
turtle.hideturtle()        
        
                    