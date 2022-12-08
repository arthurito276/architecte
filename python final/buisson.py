from rectangle import rectangle
from pave import pave
import turtle

def buisson(x,ySol,w,tridi=None):
    if tridi != None:
        pave(x,ySol,w,25,10,tridi,"forest green")
    else:  
        rectangle(x,ySol,w,20,"forest green")
    

if __name__ == "__main__":
    buisson(6,0,40,45)
    turtle.exitonclick()