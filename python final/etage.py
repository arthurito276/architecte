from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetreBalcon import fenetre_balcon
import turtle

def etage(x, ySol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        ySol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    facade(x,ySol,couleur,niveau)
    # dessin des 3 Eléments
    x_elements = [x,x+42.5,x-42.5]
    shuffle(x_elements)
    for i in range(3):
        f_ou_fb = randint(0, 1)
        if f_ou_fb == 0:
            fenetre_balcon(x_elements[i],ySol+niveau*60)
        else:
            fenetre(x_elements[i],ySol+20+niveau*60)


if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()