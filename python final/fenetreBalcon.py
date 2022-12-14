import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    turtle.fillcolor("light blue") # défini la couleur de remplissage sur bleu clair
    turtle.begin_fill() # commence le remplissage
    rectangle(x,y,30,50) # dessine la porte fenêtre aux coordonnées x,y de largeur 30 et de hauteur 50
    turtle.end_fill() # termine le remplissage

    # balcon
    rectangle(x,y,40,30) #trace le contour du balcon aux coordonnées x,y de largeur 40 et de hauteur 30
    for barreau in range(-3,4): # boucle pour tracer les barreaux du balcon
        trait(x+5*barreau,y,x+5*barreau,y+30)# trace chaque barreau dont l'abscisse varie en fonction du compteur de la boucle


if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()