from random import randint
from toit1 import toit1
from toit2 import toit2
import turtle

def toit(x, ySol, niveau,tridi = None):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        ySol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Cette fonction dessine au hasard un des 2 types de toit

    '''
    toit = randint(1,2)
    if toit == 1:
        toit1(x,ySol,niveau,tridi)
    else:
        toit2(x,ySol,niveau,tridi)


if __name__ == '__main__':
    toit(70,20,1)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()