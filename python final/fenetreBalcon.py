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
    turtle.fillcolor("light blue")#La je change la couleur du pinceau pourla mettre en bleu
    turtle.pencolor("light blue")
    turtle.begin_fill()#ici c'est  pour remplir le contenue de la fenetre pour pas que ça reste blanc
    rectangle(x,y,30,50)#je defini la taille de la fenetre
    turtle.end_fill()
    # balcon
    turtle.pencolor("black")#je remet la couleur par defaut
    rectangle(x,y,40,30)#je donne la taille du balcon
    for barreau in range(-3,4):
        trait(x+5*barreau,y,x+5*barreau,y+30)#j'utilise une fonction repetitive pour diminuer le nombre de ligne


if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()