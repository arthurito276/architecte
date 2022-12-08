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
    yToit = ySol + niveau * 60
    if tridi != None:
        pave(x,yToit,140,10,60,tridi,"black")
    else:
        turtle.pensize(10)
        trait(x-70,yToit,x+70,yToit)
        turtle.pensize(1)

if __name__ == '__main__':
    toit2(67,12,2,30)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()