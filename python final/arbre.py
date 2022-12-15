import turtle
from pave import pave

def arbre(x:float,y:float,tridi:float=None):
    """Dessine un arbre

    Args:
        x (float): Abscisse du centre du tronc
        y (float): Ordonnée de la base du tronc
        tridi (float, optional): Angle de la perspective cavalière. None par défaut.
    """
    # dessin du tronc
    pave(x,y,7.5,50,3,tridi,"brown")
    # dessin des feuilles
    pave(x,y+45,30,30,10,tridi,"forest green")

if __name__ == "__main__":
    arbre(34,34,30)
    turtle.exitonclick()