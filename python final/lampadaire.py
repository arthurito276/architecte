from rectangle import rectangle
import turtle
from trait import trait
import datetime as dt
from pave import pave

def lampadaire(x:float,y:float,tridi:float = None,heure_force = None)->None:
    """Dessine un lampadaire

    Args:
        x (float): Abscisse du centre du lampadaire
        y (float): Ordonnée du centre de la base du lampadaire
        tridi (float, optional): Angle de fuite de la perspective cavalière. None par défaut.
    """
    pave(x,y,5,90,2,tridi,"black")
    heure = dt.datetime.now().hour
    if heure_force != None:
        heure = heure_force
    if heure < 8 or heure > 20 :
        pave(x,y+80,15,15,10,tridi,"gold")
    else:
        pave(x,y+80,15,15,10,tridi,"light blue")

if __name__ == "__main__":
    lampadaire(45,0,30,4)
    turtle.exitonclick()