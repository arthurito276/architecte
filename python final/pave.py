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
    rectangle(x,y,w,h,c_remplissage) # Dessine le rectangle, première face du pavé
    if angle != None: # Dessine les autres faces si l'angle est différent de None
        if angle < 180: # Vérifie si la face du haut doit être tracée
            parallelogramme(x,y+h,w,d,angle,0,c_remplissage) # Trace la face du haut
        if angle > 90: # Vérifie si la face visible est celle de gauche 
            parallelogramme(x-w/2,y+h/2,h,d,angle,90,c_remplissage) # Trace la face de gauche
        elif angle < 90: # Vérifie si la face visible est celle de droite
            parallelogramme(x+w/2,y+h/2,h,d,angle,90,c_remplissage) # Trace la face de droite   


if __name__ == "__main__":
    pave(4,5,140,100,50,180,"blue")
    turtle.exitonclick()