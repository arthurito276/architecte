from rectangle import rectangle
import turtle
from trait import trait
from pave import pave

def lampadaire(x,y_sol,tridi = None):
    if tridi != None:
        pave(x,y_sol,5,90,2,tridi,"black")
        pave(x,y_sol+80,15,15,7,tridi,"gold")
    else:
        rectangle(x,y_sol,5,90,"black")
        rectangle(x,y_sol+80,15,15,"gold")

if __name__ == "__main__":
    lampadaire(45,0,30)
    turtle.exitonclick()