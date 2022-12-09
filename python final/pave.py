from rectangle import rectangle
import turtle
from parallelogramme import parallelogramme

def pave(x,y,w,h,d,angle,c_remplissage):
    if angle != None:
        parallelogramme(x,y+h,w,d,angle,0,c_remplissage)
        if angle > 90:
            parallelogramme(x-w/2,y+h/2,w,d,angle,90,c_remplissage)
        else:
                parallelogramme(x+w/2,y+h/2,h,d,angle,90,c_remplissage)
    else:
        rectangle(x,y,w,h,c_remplissage)


if __name__ == "__main__":
    pave(4,5,140,100,23,30,"blue")
    turtle.exitonclick()