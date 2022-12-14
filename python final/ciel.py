import turtle
import datetime as dt
from astre import astre
from nuage_etoile import ciel_nuage


def ciel():
    heure = dt.datetime.now().hour
    minute = dt.datetime.now().minute
    heure = 8
    if heure > 20 or heure < 7:
        c_ciel = "dark blue"
    elif heure >= 7 and heure <= 9:
        c_ciel = (float(10+heure*2),float(50+heure*3),float(100+heure*3))
        turtle.bgcolor(int(10+heure*2),int(50+heure*3),int(100+heure*3))

if __name__ == "__main__":
    ciel()
    turtle.exitonclick()
