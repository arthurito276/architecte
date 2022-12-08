import turtle
from rectangle import rectangle
from trait import trait
from pave import pave

def fenetre_balcon(x,y,tridi=None):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    if tridi != None:
        pave(x,y,30,50,2,tridi,"light blue")
    else:
        rectangle(x,y,30,50,"light blue")#je defini la taille de la fenetre

    # balcon
    if tridi != None:
        pave(x,y,40,30,2,tridi,None)
    else:
        rectangle(x,y,40,30)#je donne la taille du balcon
    for barreau in range(-3,4):
        trait(x+5*barreau,y,x+5*barreau,y+30)#j'utilise une fonction repetitive pour diminuer le nombre de ligne


if __name__ == '__main__':
    fenetre_balcon(0,0,30)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()