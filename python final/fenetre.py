from rectangle import rectangle
import turtle
import datetime as dt
from random import randint

def fenetre(x,y,heure_force = None):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    heure = dt.datetime.now().hour
    if heure_force != None:
        heure = heure_force
    if heure > 8 and heure < 20:
        rectangle(x,y,30,30,"light blue")
    else:
        on = randint(0,1)
        if on == 1:
            rectangle(x, y, 30, 30, "gold")
        else:
            rectangle(x, y, 30, 30, "dark blue")

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

