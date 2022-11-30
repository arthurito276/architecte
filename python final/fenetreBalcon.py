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

    turtle.pendown()
    turtle.pencolor("blue")
    rectangle(0,0,30,30)



    # balcon


    turtle.pendown()
    turtle.pencolor("black")
    rectangle(0,0,50,-30)
    rectangle(0,0,40,-30)
    rectangle(0,0,30,-30)
    rectangle(0,0,20,-30)
    rectangle(0,0,10,-30)
    rectangle(0,0,0,-30)



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()