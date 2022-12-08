import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
from buisson import buisson
from cloture import cloture
from lampadaire import lampadaire
# ------------------------------
# ------------------------------
# ------------------------------

def main(tridi = None):
    turtle.setup(800, 600)
    turtle.speed(2)
    # On définit la hauteur du sol
    y_sol = -200
    # Dessin du sol de la rue
    sol(y_sol,tridi)
    # Dessin des 4 immeubles
    if tridi==None or tridi<90:
        for x_immeuble in range(-282,283,188):
            immeuble(x_immeuble,y_sol,tridi)
    
    
    #
    '''for x_element in range(-376,377,188):
        choix_element = randint(0,1)
        if choix_element==0:
            cloture(x_element,y_sol,48)
        else:
            buisson(x_element,y_sol,48)
        lampadaire(x_element,y_sol)
        '''

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main(45)



