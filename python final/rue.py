import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
from buisson import buisson
from cloture import cloture
from lampadaire import lampadaire
from arbre import arbre
from ciel import ciel
# ------------------------------
# ------------------------------
# ------------------------------

def main(heure_force = None):
    turtle.setup(800, 600)
    turtle.speed(2)
    # On définit la hauteur du sol
    y_sol = -200
    # Dessin du sol de la rue
    sol(y_sol)
    #ciel
    ciel(heure_force)
    # Dessin des 4 immeubles
    for x_immeuble in range(-282,283,188):
        immeuble(x_immeuble,y_sol,heure_force)
    #
    for x_element in range(-376,377,188):
        choix_element = randint(0,1)
        arbre(x_element,y_sol,60,50)
        if choix_element==0:
            cloture(x_element,y_sol,48)
        else:
            buisson(x_element,y_sol,48)
        lampadaire(x_element+10,y_sol,heure_force)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main(6)



