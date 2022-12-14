import turtle
from trait import trait
from pave import pave

def toit2(x, ySol, niveau,tridi):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    pave(x,ySol + niveau * 60,140,10,60,tridi,"black")

if __name__ == '__main__':
    toit2(67,12,2,30)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()