import turtle
from rectangle import rectangle
from pave import pave

def buisson(x,ySol,w,tridi=None):
    pave(x,ySol,w,25,10,tridi,"forest green")

if __name__ == "__main__":
    buisson(6,0,40,45)
    turtle.exitonclick()