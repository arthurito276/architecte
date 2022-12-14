import turtle
from rectangle import rectangle
from trait import trait
import datetime as dt
from random import randint

def fenetre_balcon(x,y,heure_force = None):
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
        rectangle(x,y,30,50,"light blue") #trace un rectangle de dimension 30/50 de couleur bleue claire
    else:
        on = randint(0, 1)
        if on == 1:
            rectangle(x, y, 30, 50, "gold")
        else:
            rectangle(x, y, 30, 50, "dark blue")

    # balcon
    rectangle(x,y,50,30)# trace un rectangle vide
    for barreau in range(-4,5):
        trait(x+5*barreau,y,x+5*barreau,y+30)# boucle pour tracer les barreaux


if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

