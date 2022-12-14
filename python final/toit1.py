import turtle
from trait import trait
from parallelogramme import parallelogramme
import math

def toit1(x, ySol, niveau,tridi = None):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.fillcolor("red")
    turtle.begin_fill()
    yToit = ySol + niveau * 60
    trait(x-80,yToit,x+80,yToit)
    trait(x+80,yToit,x,yToit+40)
    trait(x,yToit+40,x-80,yToit)
    turtle.end_fill()
    angle_toit = math.degrees(math.atan(0.5))
    if tridi < 90:
        parallelogramme(x+40,yToit+20,89,60,tridi,angle_toit,"red")
        parallelogramme(x-40,yToit+20,89,60,tridi,-angle_toit,"red")
    else:
        parallelogramme(x-40,yToit+20,89,60,tridi,-angle_toit,"red")
        parallelogramme(x+40,yToit+20,89,60,tridi,angle_toit,"red")


if __name__ == '__main__':
    toit1(32,34,4,45)
    # On ferme la fenêtre s'il y a un clic gauche
    turtle.exitonclick()
