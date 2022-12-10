from rectangle import rectangle
import turtle
from trait import trait
from pave import pave

def lampadaire(x:float,y:float,tridi:float = None)->None:
    """Dessine un lampadaire

    Args:
        x (float): Abscisse du centre du lampadaire
        y (float): Ordonnée du centre de la base du lampadaire
        tridi (float, optional): Angle de fuite de la perspective cavalière. None par défaut.
    """
    pave(x,y,5,90,2,tridi,"black")
    pave(x,y+80,15,15,7.5,tridi,"gold")

if __name__ == "__main__":
    lampadaire(45,0,30)
    turtle.exitonclick()