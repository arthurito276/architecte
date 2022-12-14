import turtle
import datetime as dt
from astre import astre
from nuage_etoile import ciel_nuage,ciel_etoile


def ciel(heure_force = None):
    heure = dt.datetime.now().hour
    if heure_force != None:
        heure = heure_force
    turtle.colormode(255)
    if heure > 20 or heure < 7:
        c_ciel = "black"
        ciel_etoile()
    elif heure >= 7 and heure <= 9:
        c_ciel = (135+60*(heure-8),206+24*(heure-8),235+10*(heure-8))
        turtle.bgcolor(c_ciel)
        ciel_etoile()
    else:
        turtle.bgcolor("sky blue")
        ciel_nuage([150,280])
    astre(heure_force)



if __name__ == "__main__":
    ciel(8)
    turtle.exitonclick()
