import math
from rectangle import rectangle
import turtle
import datetime as dt

def astre():
    heure = dt.datetime.now().hour
    x_astre = (800/12)*(heure-12)
    y_astre = -1*(heure-12)**2+250
    print(x_astre,y_astre)
    if heure > 8 and heure < 20:
        rectangle(x_astre,y_astre,40,40,"gold")
    else:
        rectangle(x_astre,y_astre,40,40,"grey")

if __name__ == "__main__":
    astre()
    turtle.exitonclick()