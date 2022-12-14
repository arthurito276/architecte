import turtle
from pave import pave

def arbre(x,y,tridi=None):
    pave(x,y,7.5,50,3,tridi,"brown")
    pave(x,y+45,30,30,10,tridi,"forest green")

if __name__ == "__main__":
    arbre(34,34,30)
    turtle.exitonclick()