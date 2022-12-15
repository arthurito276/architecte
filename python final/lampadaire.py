from rectangle import rectangle
import turtle
from trait import trait
import datetime as dt
from pave import pave

def lampadaire(x:float,y:float,tridi:float = None,heure_force:int = None)->None:
    """Dessine un lampadaire allumé ou éteint en fonction de l'heure

    Args:
        x (float): Abscisse du centre du lampadaire
        y (float): Ordonnée du centre de la base du lampadaire
        tridi (float, optional): Angle de fuite de la perspective cavalière. None par défaut.
        heure_force (int,optional): Force l'heure. None par défaut
    """
    pave(x,y,5,90,2,tridi,"black") # Dessine le poteau du lampadaire
    heure = dt.datetime.now().hour # Récupère l'heure du système
    if heure_force != None: # Vérifie si l'heure doit être forcée
        heure = heure_force # Force l'heure
    if heure < 8 or heure > 20 : # Choisit si le lampadaire sera allumé ou éteint en fonction de l'heure
        pave(x,y+80,15,15,10,tridi,"gold") # Dessine l'ampoule allumé
    else:
        pave(x,y+80,15,15,10,tridi,"light blue") # Dessine l'ampoule éteinte

if __name__ == "__main__":
    lampadaire(45,0,30,4)
    turtle.exitonclick()