import math
from rectangle import rectangle
import turtle
import datetime as dt

def astre():
    heure = dt.datetime.now().hour
    if heure > 8 and heure < 20:
        x_astre = (800/12)*(heure-12)
        y_astre = x_astre**2

if __name__ == "__main__":
    astre()