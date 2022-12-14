import turtle
from rectangle import rectangle
from pave import pave

def facade(x, ySol, couleur, niveau,tridi=None):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        ySol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
    pave(x,ySol+niveau*60,140,60,60,tridi,couleur)

if __name__ == '__main__':
    facade(0,0,"red",0,30)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()