import math
from pave import pave
import turtle
import datetime as dt

def astre(heure_force:int = None,tridi:float = None):
    """Dessine un astre en fonction de l'heure du système, soit la Lune, soit le Soleil

    Args:
        heure_force (int, optional): Force l'heure à laquelle doit être positionné l'astre. None par défaut.
        tridi (float, optional): Angle de la perspective cavalière. None par défaut.
    """
    heure = dt.datetime.now().hour # Récupère de l'heure du système
    if heure_force != None: # Vérifie si l'heure doit être forcée
        heure = heure_force # Force l'heure
    x_astre = (800/12)*(heure-12) # Détermine l'abscisse de l'astre
    y_astre = -1*(heure-12)**2+250 # Détermine l'ordonnée de l'astre
    
    if heure < 8 or heure > 20: # Choisit entre la Lune et le Soleil en fonction de l'heure.
        pave(x_astre,y_astre,40,40,15,tridi,"light grey") # Dessine une Lune aux coordonnées x_astre et y_astre 40x40x15
    else:
        pave(x_astre,y_astre,40,40,15,tridi,"gold") # Dessine un Soleil aux coordonnées x_astre et y_astre 40x40x15

if __name__ == "__main__":
    for heure in range(0,25):
        astre(heure,30)
    turtle.exitonclick()