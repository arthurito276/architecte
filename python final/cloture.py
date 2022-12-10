import turtle
from rectangle import rectangle
from pave import pave

def cloture(x:float,y:float,w:float,tridi:float = None) -> None:
    """Dessine une cloture

    Args:
        x (float): Abscisse du centre de la cloture
        y (float): Ordonnée du centre de la base de la cloture
        w (float): Largeur de la cloture
        tridi (float, optional): Angle de fuite de la perspective cavalière. None par défaut.
    """
    turtle.pencolor("peru")
    pave(x,y+10,w,5,2,tridi,"peru")
    pave(x,y+25,w,5,2,tridi,"peru")
    nb_planche = w // 6
    turtle.pencolor("black")
    for x_planche in range(x-w//2,x+w//2+1,10):
        pave(x_planche,y,5,35,2,tridi,"peru")
        



if __name__ == "__main__":
    cloture(0,0,80,45)
    turtle.exitonclick()