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
    turtle.fillcolor("light blue")
    turtle.pencolor("light blue")
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.end_fill()
    # balcon
    turtle.pencolor("black")
    rectangle(x,y,40,30)
    for barreau in range(-3,4):
        trait(x+5*barreau,y,x+5*barreau,y+30)


if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()