from rectangle import rectangle
import turtle
from parallelogramme import parallelogramme

def pave(x,y,w,h,d,angle,c_remplissage):
    rectangle(x,y,w,h,c_remplissage)
    if angle != None:
        if angle < 180:
            parallelogramme(x,y+h,w,d,angle,0,c_remplissage)
        if angle > 90:
            parallelogramme(x-w/2,y+h/2,h,d,angle,90,c_remplissage)
        elif angle < 90:
            parallelogramme(x+w/2,y+h/2,h,d,angle,90,c_remplissage)            


if __name__ == "__main__":
    pave(4,5,140,100,50,180,"blue")
    turtle.exitonclick()