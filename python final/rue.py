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

def main(tridi = None,heure_force = None):
    turtle.setup(800, 600)
    # On définit la hauteur du sol
    y_sol = -200
    # Dessin du ciel
    ciel(heure_force,tridi)
    # Dessin du sol de la rue
    sol(y_sol,tridi)
    # Détermine dans quel ordre vont être dessinés les éléments
    if tridi==None or tridi<90: 
        step = 1                
    else:                       
        step = -1               
    # Crée des listes contenants les abscisses des immeubles et des éléments
    x_immeubles = [i for i in range(-282*step,283*step,188*step)]
    x_elements = [i for i in range(-376*step,377*step,188*step)]
    x_immeubles.append(None) # Afin d'itérer plus bas sur les deux listes en même temps, elles doivent avoir
                             # le même nombre d'élément, on ajoute un élément "None" pour équilibrer.
    #Dessin des immeubles en partant du "fond" de la rue
    for x_immeuble,x_element in zip(x_immeubles,x_elements):
        choix_element = randint(0,1) # Choisit aléatoirement un chiffre entre 0 et 1
        arbre(x_element,y_sol,tridi) # Dessine un arbre
        if choix_element==0: # Vérifie si l'élement à dessiner doit être une cloture
            cloture(x_element,y_sol,48,tridi) # Dessine une cloture
        else: #Sinon c'est un buisson
            buisson(x_element,y_sol,48,tridi) # Dessine un buisson
        lampadaire(x_element,y_sol,tridi,heure_force) # Dessine un lampadaire
        if x_immeuble != None: # Vérifie qu'il faille dessiner un immeuble 
            immeuble(x_immeuble,y_sol,tridi,heure_force) # Dessine un immeuble
        
    
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main(15,4)



