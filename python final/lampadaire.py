from rectangle import rectangle
import turtle
from trait import trait
import datetime as dt

def lampadaire(x,y_sol,heure_force = None):
    rectangle(x,y_sol,5,90,"black")
    heure = dt.datetime.now().hour
    if heure_force != None:
        heure = heure_force
    if heure < 8 or heure > 20 :
        rectangle(x,y_sol+80,15,15,"gold")
    else:
        rectangle(x,y_sol+80,15,15,"light blue")

if __name__ == "__main__":
    lampadaire(45,0,4)
    turtle.exitonclick()