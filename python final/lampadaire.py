from rectangle import rectangle
import turtle

from trait import trait
def lampadaire(x,y_sol):
    turtle.fillcolor("black")
    turtle.begin_fill()
    rectangle(x,y_sol,5,90)
    turtle.end_fill()
    
    turtle.pencolor("gold")
    turtle.fillcolor("gold")
    turtle.begin_fill()
    rectangle(x,y_sol+80,15,15)
    turtle.end_fill()
    turtle.pencolor("black")

if __name__ == "__main__":
    lampadaire(45,0)
    turtle.exitonclick()