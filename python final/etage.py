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
    facade(x,ySol,couleur,niveau) # dessine la facade aux coordonnées x,ySol et au niveau et dans une couleur définis en argument
    # dessin des 3 Eléments
    x_elements = [x,x+42.5,x-42.5] # crée une liste contenant l'abscisse de chaque élément
    shuffle(x_elements) # mélange de façon aléatoire les éléments de la liste grâce à shuffle
    for i in range(3): # boucle qui se répetera 3, où i prendra successivement les valeurs 0, 1 et 2
        f_ou_fb = randint(0, 1) # initialise une variable contenant un entier aléatoire entre 0 et 1
        if f_ou_fb == 0: # structure conditionnelle afin de dessiner une fenetre avec ou sans balcon en fonction de la variable ci-dessus
            fenetre_balcon(x_elements[i],ySol+niveau*60) # dessine une fenetre avec un balcon aux coordonnées x,ySol et au niveau défini en argument
        else:
            fenetre(x_elements[i],ySol+20+niveau*60) # dessine une fenetre simple aux coordonnées x,ySol et au niveau défini en argument


if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()