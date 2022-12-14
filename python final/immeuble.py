# module immeuble

from couleurAleatoire import couleurAleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, ySol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)

    nb_etage = randint(1,4) # Détermine de façon aléatoire le nombre d'étages et le stocke dans une variable

    #Couleurs des éléments (aléatoire)
    turtle.colormode(255) # Défini le mode de couleur de turtle sur 255
    couleur_facade = couleurAleatoire() # Défini la couleur de la facade aléatoirement
    couleur_elements= couleurAleatoire() # Défini la couleur des éléments aléatoirement

    # Dessin du RDC

    rdc(x,ySol,couleur_facade,couleur_elements) # Dessine le rdc aux coordonnées x,ySol avec les couleurs définies plus haut

    # Dessin des étages
    for niveau in range(1,nb_etage+1): # boucle qui s'exécutera en fonction du nombre d'étages
        etage(x,ySol,couleur_facade,niveau) # Dessine un étage aux coordonnées x,ySol avec la couleur de la facade plus haut et le niveau

    # Dessin du toit
    toit(x,ySol,nb_etage+1) # Dessine un toit qui sera choisi aléatoirement
    

if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()