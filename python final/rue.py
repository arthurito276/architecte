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
        step = 1
    else:
        step = -1
    x_immeubles = [i for i in range(-282*step,283*step,188*step)]
    x_elements = [i for i in range(-376*step,377*step,188*step)]
    x_immeubles.append(None) #type:ignore
    for x_immeuble,x_element in zip(x_immeubles,x_elements):
        choix_element = randint(0,1)
        if choix_element==0:
            cloture(x_element,y_sol,48,tridi)
        else:
            buisson(x_element,y_sol,48,tridi)
        lampadaire(x_element,y_sol,tridi)
        if x_immeuble != None:
            immeuble(x_immeuble,y_sol,tridi)
        
    
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main()



