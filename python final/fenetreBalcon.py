import turtle
from trait import trait
import datetime as dt
from random import randint
from pave import pave

def fenetre_balcon(x,y,tridi=None,heure_force = None):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    heure = dt.datetime.now().hour
    if heure_force != None:
        heure = heure_force
    if heure > 8 and heure < 20:
        pave(x,y,30,50,2,tridi,"light blue")
    else:
        on = randint(0, 1)
        if on == 1:
            pave(x, y, 30, 50, 2, tridi, "gold")
        else:
            pave(x, y, 30, 50, 2, tridi, "dark blue")

    # balcon
    pave(x,y,40,30,2,tridi,None)
    for barreau in range(-4,5):
        trait(x+5*barreau,y,x+5*barreau,y+30)


if __name__ == '__main__':
    fenetre_balcon(0,0,30,3)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

