import turtle
from rectangle import rectangle
from random import randrange,randint

def ciel_nuage(h_nuage):
    turtle.pencolor("light grey")
    nb_nuages= randint(0,20)
    for nuage in range(nb_nuages):
        y_nuage = randrange(h_nuage[0],h_nuage[1])
        x_nuage = randrange(-400,400)
        rectangle(x_nuage,y_nuage,45,30,"light grey")
    turtle.pencolor("black")

def ciel_etoile():
    turtle.pencolor("white")
    for i in range(100):
        rectangle(randint(-400,400),randint(-200,300),1,1,"white")
    turtle.pencolor("black")


if __name__ == "__main__":
    turtle.bgcolor("black")
    ciel_etoile()
    ciel_nuage([150,280])
    turtle.exitonclick()