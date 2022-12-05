from facade import facade
from random import shuffle
from porte import porte
from fenetre import fenetre
import turtle

def rdc(x, ySol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        ySol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
    facade(x, ySol, c_facade,0)

    # Construit les 3 éléments (1 porte et 2 fenetres)
    x_elements = [x,x+35,x-35]
    shuffle(x_elements)
    fenetre(x_elements[0],ySol+20)
    fenetre(x_elements[1],ySol+20)
    porte(x_elements[2],ySol,c_porte)
if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()