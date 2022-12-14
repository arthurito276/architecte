import turtle
import datetime as dt
from astre import astre
from nuage_etoile import ciel_nuage,ciel_etoile


def ciel(heure_force = None,tridi = None):
    heure = dt.datetime.now().hour
    if heure_force != None:
        heure = heure_force
    turtle.colormode(255)
    if heure > 20 or heure < 7:
        turtle.bgcolor("black")
        ciel_etoile()
    else:
        turtle.bgcolor("sky blue")
        ciel_nuage([150,280],tridi)
    astre(heure,tridi)



if __name__ == "__main__":
    ciel(8)
    turtle.exitonclick()
