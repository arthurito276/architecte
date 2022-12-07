from rectangle import rectangle
import turtle
def buisson(x,ySol,w):
    turtle.fillcolor("green")
    turtle.begin_fill()
    rectangle(x,ySol,w,20)
    turtle.end_fill()

buisson(6,0,25)
turtle.exitonclick()