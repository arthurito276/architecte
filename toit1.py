import turtle
from trait import trait

def toit1(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.begin_fill()
    yToit = ySol + niveau * 60
    trait(x-80,yToit,x+80,yToit)
    trait(x-80,yToit,x,yToit+40)
    trait(x+80,yToit,x,yToit+40)
    trait(x,yToit+40,x-80,yToit)
    trait(x,yToit+40,x+80,yToit)
    turtle.end_fill()



if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clic gauche
    turtle.exitonclick()
