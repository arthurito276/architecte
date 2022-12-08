# module immeuble

from couleurAleatoire import couleurAleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, ySol,tridi = None):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)

    nb_etage = randint(1,4)

    #Couleurs des éléments (aléatoire)
    turtle.colormode(255)
    couleur_facade = couleurAleatoire()
    couleur_elements= couleurAleatoire()

    # Dessin du RDC

    rdc(x,ySol,couleur_facade,couleur_elements,tridi)

    # Dessin des étages
    for niveau in range(1,nb_etage+1):
        etage(x,ySol,couleur_facade,niveau,tridi)

    # Dessin du toit
    toit(x,ySol,nb_etage+1,tridi)
    

if __name__ == '__main__':
    immeuble(0,0,30)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()