import math
from pave import pave
import turtle
import datetime as dt

def astre(heure_force = None,tridi = None):
    heure = dt.datetime.now().hour
    if heure_force != None:
        heure = heure_force
    x_astre = (800/12)*(heure-12)
    y_astre = -1*(heure-12)**2+250
    if heure > 8 and heure < 20:
        pave(x_astre,y_astre,40,40,15,tridi,"gold")
    else:
        pave(x_astre,y_astre,40,40,15,tridi,"grey")

if __name__ == "__main__":
    for heure in range(0,25):
        astre(heure,30)
    turtle.exitonclick()