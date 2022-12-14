from rectangle import rectangle
import turtle
from parallelogramme import parallelogramme

def pave(x:float,y:float,w:float,h:float,d:float,angle:float,c_remplissage=None)-> None:
    """Dessine un pavé

    Args:
        x (float): Abscisse du centre de la base du pavé
        y (float): Ordonnée du centre de la base du pavé
        w (float): Largeur de la base du pavé
        h (float): Hauteur du pavé
        d (float): Profondeur du pavé
        angle (float): Angle de fuite du pavé
        c_remplissage (optional): Couleur de remplissage du pavé. None par défaut.
    """
    rectangle(x,y,w,h,c_remplissage)
    if angle != None:
        if angle < 180:
            parallelogramme(x,y+h,w,d,angle,0,c_remplissage)
        if angle > 90:
            parallelogramme(x-w/2,y+h/2,h,d,angle,90,c_remplissage)
        elif angle < 90:
            parallelogramme(x+w/2,y+h/2,h,d,angle,90,c_remplissage)            


if __name__ == "__main__":
    pave(4,5,140,100,50,180,"blue")
    turtle.exitonclick()