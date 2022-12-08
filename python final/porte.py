import turtle
from rectangle import rectangle
from pave import pave

def porte(x,y,couleur,tridi = None):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    '''
    if tridi != None:
        pave(x,y,30,50,2,tridi,couleur)
    else:
        rectangle(x,y,30,50,couleur)



if __name__ == '__main__':
    porte(0,0,"red",30)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
