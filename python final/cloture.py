import turtle
from rectangle import rectangle
from pave import pave

def cloture(x,y_sol,w,tridi = None):
    turtle.pencolor("peru")
    pave(x,y_sol+10,w,5,2,tridi,"peru")
    pave(x,y_sol+25,w,5,2,tridi,"peru")
    nb_planche = w // 6
    turtle.pencolor("black")
    for x_planche in range(x-w//2,x+w//2+1,10):
        pave(x_planche,y_sol,5,35,2,tridi,"peru")
        



if __name__ == "__main__":
    cloture(0,0,80,45)
    turtle.exitonclick()