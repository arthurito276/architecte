from rectangle import rectangle
import turtle

from trait import trait
def lampadaire(x,y_sol):
    rectangle(x,y_sol,5,90,"black")
    rectangle(x,y_sol+80,15,15,"gold")

if __name__ == "__main__":
    lampadaire(45,0)
    turtle.exitonclick()