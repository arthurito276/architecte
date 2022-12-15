import turtle
import datetime as dt
from astre import astre
from nuage_etoile import ciel_nuage,ciel_etoile


def ciel(heure_force:int = None,tridi:float = None):
    """Assemble et dessine les différents éléments du ciel.

    Args:
        heure_force (int, optional): Force l'heure à laquelle le ciel va être configuré. None par défaut.
        tridi (float, optional): Angle de la perspective cavalière. None par défaut.
    """
    heure = dt.datetime.now().hour # Récupère de l'heure du système
    if heure_force != None: # Vérifie si l'heure doit être forcée
        heure = heure_force # Force l'heure
    turtle.colormode(255) # Modifie le mode de couleur de turtle
    if heure > 20 or heure < 7: # Modifie les éléments en fonction de l'heure
        turtle.bgcolor("black") # Change la couleur de l'arrière plan en noir
        ciel_etoile() # Dessine les étoiles
    else:
        turtle.bgcolor("sky blue") # Change la couleur de l'arrière plan en bleu ciel
        ciel_nuage([150,280],tridi) # Dessine des nuages dont l'ordonnée est comprise entre 150 et 280
    astre(heure,tridi) # Dessine un astre



if __name__ == "__main__":
    ciel(8)
    turtle.exitonclick()
