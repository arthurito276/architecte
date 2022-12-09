from rectangle import rectangle
import turtle
from trait import trait
from pave import pave

def lampadaire(x,y_sol,tridi = None):
    pave(x,y_sol,5,90,2,tridi,"black")
    pave(x,y_sol+80,15,15,7.5,tridi,"gold")

if __name__ == "__main__":
    lampadaire(45,0,30)
    turtle.exitonclick()