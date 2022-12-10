import turtle
from rectangle import rectangle
from pave import pave

def buisson(x:float,y:float,w:float,tridi:float=None)-> None:
    """Dessine un buisson

    Args:
        x (float): Abscisse du centre du buisson
        y (float): Ordonnée du centre de la base du buisson
        w (float): Largeur du buisson
        tridi (float, optional): Angle de fuite de la perspective cavalière. None par défaut.
    """
    pave(x,y,w,25,10,tridi,"forest green")

if __name__ == "__main__":
    buisson(6,0,40,45)
    turtle.exitonclick()