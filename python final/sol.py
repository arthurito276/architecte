# Module par sebastien chanthery

import turtle
from trait import trait
from pave import pave

# ----- Sol de la rue -----
def sol(y_sol,tridi = None):
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''
    pave(0,y_sol,840,10,100,tridi,"black")


if __name__ == '__main__':
    sol(0,30)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
