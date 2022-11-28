import turtle
from trait import trait

def toit2(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.pensize(10)
    yToit = ySol + niveau * 60
    trait(x-70,yToit,x+70,yToit)

if __name__ == '__main__':
    toit2(67,12,2)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()